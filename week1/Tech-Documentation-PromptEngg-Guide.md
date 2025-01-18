# Technical Documentation Prompt Engineering Guide

## 1. Basic vs Enhanced Prompts

### Basic Prompts (Less Effective)
```plaintext
Write documentation for a login function.

Write API documentation for user registration.

Document error handling for database connections.
```

### Enhanced Prompts (More Effective)
```plaintext
Act as a senior technical writer with expertise in Python. Write comprehensive documentation for a login function following these guidelines:
- Start with a brief overview of the function's purpose
- List all parameters with their types and descriptions
- Describe the return value and its format
- Document all possible exceptions
- Include security considerations
- Add Python code examples
- Follow Google's developer documentation style guide

Context: This function is part of a web application's authentication system.
```

## 2. Real-World Examples

### Example 1: Function Documentation

Basic Prompt:
```plaintext
Document this function:

def process_payment(amount, card_details):
    # Payment processing logic
    pass
```

Enhanced Prompt:
```plaintext
Act as a senior technical writer for a financial software company. Write comprehensive documentation for the following payment processing function. Follow these guidelines:
- Use clear, precise language suitable for financial software
- Include all security considerations for handling payment data
- Document error cases and exception handling
- Add example usage with dummy data
- Follow PCI compliance documentation requirements

Function to document:

def process_payment(amount: float, card_details: Dict[str, str]) -> Dict[str, Any]:
    # Payment processing logic
    pass
```

Example Output:
```python
def process_payment(amount: float, card_details: Dict[str, str]) -> Dict[str, Any]:
    """
    Process a secure payment transaction using the provided card details.

    Args:
        amount (float): The payment amount in dollars. Must be greater than 0.
        card_details (Dict[str, str]): A dictionary containing card information:
            - 'number': Encrypted card number
            - 'expiry': Card expiration date (MM/YY)
            - 'cvv': Card verification value
            - 'zip_code': Billing ZIP code

    Returns:
        Dict[str, Any]: Transaction result containing:
            - 'transaction_id': Unique transaction identifier
            - 'status': 'success' or 'failed'
            - 'timestamp': Transaction timestamp
            - 'error_message': Error description (if failed)

    Raises:
        ValueError: If amount is <= 0 or card details are invalid
        PaymentProcessingError: If payment processor connection fails
        SecurityValidationError: If encryption validation fails

    Security Considerations:
        - Card details are encrypted in transit and at rest
        - CVV is never stored
        - All transactions are logged for audit
        - Automated fraud detection is applied

    Example:
        >>> card_details = {
        ...     'number': 'encrypted_card_number',
        ...     'expiry': '12/25',
        ...     'cvv': '123',
        ...     'zip_code': '94043'
        ... }
        >>> result = process_payment(99.99, card_details)
        >>> print(result['status'])
        'success'
    """
```

### Example 2: API Documentation

Few-shot Learning Prompt:
```plaintext
Here are two examples of well-documented API endpoints:

Example 1:
POST /api/v1/users/verify
Verify user email address using a verification token.

Request Body:
{
    "token": string (required) - Email verification token
}

Response:
200 OK
{
    "verified": boolean,
    "user_id": string
}

Error Responses:
400 Bad Request - Invalid token format
404 Not Found - Token not found or expired
500 Internal Server Error - Verification service unavailable

Example 2:
GET /api/v1/products/{product_id}/inventory
Get current inventory levels for a specific product.

Parameters:
- product_id: string (required) - Unique product identifier

Response:
200 OK
{
    "product_id": string,
    "quantity": integer,
    "last_updated": ISO8601 timestamp,
    "warehouse_id": string
}

Error Responses:
404 Not Found - Product not found
403 Forbidden - Insufficient permissions

Using the same style and detail level, document the following API endpoint:
POST /api/v1/orders
Create a new order in the system.
```

### Example 3: Error Handling Pattern Documentation

```plaintext
Act as a senior technical writer specializing in error handling best practices. Document the error handling pattern for a microservices-based e-commerce system. Include:

1. Standard error response format
2. Error categorization approach
3. Logging requirements
4. Client retry recommendations
5. Example error scenarios and responses

Target audience: Backend developers with experience in distributed systems.
```

## 3. Advanced Prompting Techniques

### Role and Context Setting
```plaintext
Act as a technical documentation expert who:
- Has 10+ years of experience in API documentation
- Specializes in OpenAPI/Swagger specifications
- Works in highly regulated industries

Your task is to document the following healthcare API endpoint...
```

### Output Format Control
```plaintext
Document the following database schema using this structure:
1. Schema Overview
   - Purpose
   - Relationships
2. Table Definitions
   - Columns
   - Constraints
   - Indexes
3. Example Queries
4. Performance Considerations

Schema to document:
[Schema details...]
```

### Multi-step Documentation
```plaintext
Let's document this authentication system in steps:

Step 1: Document the user registration flow
[Previous response used as context]

Step 2: Document the login process
[Previous response used as context]

Step 3: Document the password reset flow
[Previous response used as context]

For each step, provide:
- Technical overview
- Security considerations
- Implementation examples
- Testing guidelines
```

## Best Practices

1. Always specify the target audience
2. Include context about the broader system
3. Request specific examples where helpful
4. Use consistent terminology
5. Ask for security considerations when relevant
6. Specify documentation style guide to follow
7. Include validation criteria for the documentation

## Exercise Templates

1. Function Documentation Exercise:
```plaintext
Document this function using Google's style guide:
[Insert function code]

Required sections:
- Overview
- Parameters
- Returns
- Raises
- Example Usage
- Security Notes (if applicable)
```

2. API Documentation Exercise:
```plaintext
Document this API endpoint following OpenAPI 3.0 guidelines:
[Insert API details]

Include:
- Request/Response examples
- Error scenarios
- Rate limiting details
- Authentication requirements
```

3. Error Handling Exercise:
```plaintext
Design and document an error handling strategy for:
[Insert system description]

Cover:
- Error categorization
- Logging strategy
- Client retry policy
- Example error responses
```
