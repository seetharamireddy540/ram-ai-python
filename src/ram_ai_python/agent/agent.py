import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")


def ask_ai(user_input):
    # This is a simplified version of the tool-use loop
    response = client.converse(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        messages=[{"role": "user", "content": [{"text": user_input}]}],
        toolConfig={
            "tools": [{
                "toolSpec": {
                    "name": "check_hotel_availability",
                    "description": "Get a list of hotels",
                    "inputSchema": {"json": {"type": "object", "properties": {}}}
                }
            }]
        }
    )
    return response
