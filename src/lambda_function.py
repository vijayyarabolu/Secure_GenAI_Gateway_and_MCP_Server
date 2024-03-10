import json
import boto3
import logging
import os

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize Bedrock client
# Note: In a real deployment, this requires AWS credentials and Bedrock access enabled
bedrock = boto3.client(service_name='bedrock-runtime')

def sanitize_input(prompt):
    """
    Basic sanitization to prevent PII or malicious injection.
    In a real app, this would use a more sophisticated library (e.g., Microsoft Presidio).
    """
    blocked_words = ["password", "secret_key", "ssn"]
    for word in blocked_words:
        if word in prompt.lower():
            raise ValueError(f"Security Alert: Blocked content detected: {word}")
    return prompt

def lambda_handler(event, context):
    """
    Main handler for the GenAI Gateway.
    """
    logger.info("Received event: %s", json.dumps(event))
    
    try:
        # 1. Parse Input
        body = json.loads(event.get('body', '{}'))
        prompt = body.get('prompt', '')
        
        if not prompt:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No prompt provided'})
            }

        # 2. Security Check (Sanitization)
        logger.info("Sanitizing input...")
        clean_prompt = sanitize_input(prompt)
        
        # 3. Call Bedrock (Mocking for now if not deployed)
        # We construct the payload for Claude 3 Sonnet
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "messages": [
                {
                    "role": "user",
                    "content": [{"type": "text", "text": clean_prompt}]
                }
            ]
        }
        
        # Uncomment this to actually call Bedrock when deployed
        # response = bedrock.invoke_model(
        #     modelId='anthropic.claude-3-sonnet-20240229-v1:0',
        #     body=json.dumps(payload)
        # )
        # result = json.loads(response['body'].read())
        
        # MOCK RESPONSE for local testing/portfolio
        result = {
            "content": [{"text": f"This is a mocked response from the Secure Gateway. You asked: {clean_prompt}"}]
        }
        
        # 4. Return Response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'status': 'success',
                'data': result
            })
        }
        
    except ValueError as e:
        logger.warning(f"Security Violation: {str(e)}")
        return {
            'statusCode': 403,
            'body': json.dumps({'error': str(e)})
        }
    except Exception as e:
        logger.error(f"Internal Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
