# server.py
from vllm import LLM, SamplingParams
from fastapi import FastAPI
import uvicorn
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_and_merge_model():
    """
    Load base model and LoRA weights from HuggingFace, merge them, and save locally
    """
    print("Loading base model...")
    # First load the base model
    base_model = AutoModelForCausalLM.from_pretrained(
        "mistralai/mistral-7b-v0.1",
        torch_dtype=torch.float16,
        device_map="auto"
    )
    
    print("Loading LoRA adapter...")
    # Load the LoRA model
    peft_model = PeftModel.from_pretrained(
        base_model,
        "goaiguru/mistral-technical-docs",
        torch_dtype=torch.float16,
        is_trainable=False
    )
    
    print("Merging models...")
    # Merge LoRA weights with base model
    merged_model = peft_model.merge_and_unload()
    
    print("Saving merged model...")
    # Save the merged model
    merged_model.save_pretrained("./merged_model")
    
    print("Saving tokenizer...")
    # Save tokenizer
    tokenizer = AutoTokenizer.from_pretrained("mistralai/mistral-7b-v0.1")
    tokenizer.save_pretrained("./merged_model")
    
    print("Models merged and saved!")
    return "./merged_model"

app = FastAPI()

print("Starting model loading and merging process...")
# Merge models and get path
merged_model_path = load_and_merge_model()

print("Initializing vLLM...")
# Initialize vLLM with merged model
llm = LLM(
    model=merged_model_path,
    tensor_parallel_size=1,  # Adjust based on number of GPUs
    gpu_memory_utilization=0.90,
    max_num_batched_tokens=32768,
    max_model_len=32768,
    trust_remote_code=True
)

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=256
)

@app.post("/generate")
async def generate_text(request: dict):
    prompts = request.get("prompts", [])
    outputs = llm.generate(prompts, sampling_params)
    
    responses = []
    for output in outputs:
        responses.append({
            "generated_text": output.outputs[0].text,
            "num_tokens": len(output.outputs[0].token_ids)
        })
    
    return {"responses": responses}

if __name__ == "__main__":
    print("Starting FastAPI server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
