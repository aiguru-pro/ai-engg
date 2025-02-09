# Harvey Legal AI: Example Query Processing Flow

## Sample Case: Delaware Corporate Law Question

### 1. Initial User Input
```
Input: "What are the key Delaware court decisions regarding director fiduciary duties in merger contexts, particularly regarding conflicts of interest?"
```

### 2. Pre-Processing & Query Analysis
**Input Parsing:**
```json
{
    "query_type": "case_law_research",
    "jurisdiction": "Delaware",
    "legal_domain": "corporate_law",
    "sub_topic": "fiduciary_duties",
    "context": "mergers",
    "specific_focus": "conflicts_of_interest"
}
```

**Context Enrichment:**
```json
{
    "relevant_areas": [
        "director_duties",
        "merger_litigation",
        "conflict_of_interest",
        "business_judgment_rule"
    ],
    "time_scope": "all_relevant_precedents",
    "court_hierarchy": [
        "Delaware Supreme Court",
        "Delaware Court of Chancery"
    ]
}
```

### 3. Case Law Model Processing

**Initial Search Parameters:**
```json
{
    "primary_sources": {
        "jurisdictions": ["Delaware"],
        "courts": [
            "Delaware Supreme Court",
            "Delaware Court of Chancery"
        ],
        "topic_filters": [
            "fiduciary duty",
            "merger",
            "director conflict"
        ]
    },
    "date_range": "all",
    "relevance_threshold": 0.85
}
```

**Retrieved Cases Sample:**
```json
{
    "key_cases": [
        {
            "case": "Revlon, Inc. v. MacAndrews & Forbes Holdings, Inc.",
            "citation": "506 A.2d 173 (Del. 1986)",
            "relevance_score": 0.95,
            "key_principle": "Enhanced scrutiny in change of control"
        },
        {
            "case": "Weinberger v. UOP, Inc.",
            "citation": "457 A.2d 701 (Del. 1983)",
            "relevance_score": 0.92,
            "key_principle": "Entire fairness standard"
        }
    ]
}
```

### 4. Analysis Generation

**Initial Draft Structure:**
```json
{
    "sections": [
        {
            "topic": "Standard of Review Framework",
            "cases": ["Business Judgment Rule", "Enhanced Scrutiny", "Entire Fairness"],
            "precedents": ["Aronson", "Revlon", "Weinberger"]
        },
        {
            "topic": "Conflict Scenarios",
            "cases": ["Direct Conflicts", "Indirect Benefits"],
            "precedents": ["Technicolor", "El Paso"]
        }
    ]
}
```

**Chain-of-Thought Reasoning:**
```text
1. Begin with fundamental standard of review framework
2. Explain how standards escalate with conflict severity
3. Provide specific examples from key cases
4. Detail modern applications and exceptions
5. Conclude with practical implications
```

### 5. Response Generation

**Draft Response:**
```text
Delaware courts have developed a sophisticated framework for analyzing director fiduciary duties in merger contexts, particularly regarding conflicts of interest:

1. Standard of Review Framework:
   - Business Judgment Rule: [Case details and application]
   - Enhanced Scrutiny: Revlon, Inc. v. MacAndrews & Forbes Holdings (506 A.2d 173)
   - Entire Fairness: Weinberger v. UOP, Inc. (457 A.2d 701)

[Additional content including case analysis and principles]
```

### 6. Quality Assurance Check

**Verification Points:**
```json
{
    "citation_check": {
        "all_cases_verified": true,
        "citations_accurate": true,
        "pin_cites_verified": true
    },
    "content_validation": {
        "principle_accuracy": true,
        "logical_flow": true,
        "completeness": true
    },
    "hallucination_check": {
        "cases_exist": true,
        "principles_accurate": true,
        "holdings_verified": true
    }
}
```

### 7. Final Response

```text
Delaware courts have established several landmark decisions regarding director fiduciary duties in merger contexts, particularly concerning conflicts of interest. Here is a comprehensive analysis supported by key precedents:

1. Foundational Standards (Weinberger v. UOP, Inc., 457 A.2d 701 (Del. 1983))
   The Delaware Supreme Court established that when directors have conflicts of interest in a merger, the transaction must satisfy the "entire fairness" standard, requiring both fair dealing and fair price.

2. Enhanced Scrutiny Contexts (Revlon, Inc. v. MacAndrews & Forbes Holdings, Inc., 506 A.2d 173 (Del. 1986))
   In change-of-control transactions, directors must secure the best value reasonably available for stockholders.

[Additional detailed analysis with citations...]

This framework continues to evolve through recent decisions, but these core principles remain fundamental to Delaware merger jurisprudence.
```

### 8. Logging & Metrics

```json
{
    "query_metrics": {
        "processing_time": "1.2s",
        "cases_reviewed": 127,
        "confidence_score": 0.94,
        "citations_included": 8,
        "source_verification": "complete"
    },
    "model_performance": {
        "hallucination_check": "passed",
        "citation_accuracy": "100%",
        "principle_accuracy": "verified"
    }
}
```

## Key Features Demonstrated in This Flow:

1. **Accurate Case Law Integration**
   - Demonstrates Harvey's 83% increase in factual responses
   - Shows proper citation and verification

2. **Comprehensive Analysis**
   - Illustrates why attorneys preferred the custom model's output 97% of the time
   - Shows depth and nuance in legal reasoning

3. **Quality Assurance**
   - Demonstrates hallucination reduction
   - Shows citation verification process

4. **Practical Application**
   - Shows how the system handles complex legal queries
   - Demonstrates integration of multiple cases and principles

---

*Note: This example flow is based on Harvey's documented capabilities and actual performance metrics. The specific response format and internal processing details may vary in the actual implementation.*
