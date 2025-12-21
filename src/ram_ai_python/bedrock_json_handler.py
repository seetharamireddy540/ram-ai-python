"""
Practical JSON Handling for AWS Bedrock Responses
"""
import json
import boto3
from typing import Dict, List, Any, Optional


def parse_bedrock_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse and extract useful information from Bedrock API response
    """
    parsed = {
        "role": response.get("role"),
        "stop_reason": response.get("stopReason"),
        "usage": response.get("usage", {}),
        "content": [],
        "tool_use": []
    }
    
    # Extract content blocks
    for content_block in response.get("output", {}).get("message", {}).get("content", []):
        if "text" in content_block:
            parsed["content"].append({
                "type": "text",
                "text": content_block["text"]
            })
        elif "toolUse" in content_block:
            parsed["tool_use"].append({
                "id": content_block["toolUse"].get("toolUseId"),
                "name": content_block["toolUse"].get("name"),
                "input": content_block["toolUse"].get("input", {})
            })
    
    return parsed


def extract_tool_calls(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract tool calls from Bedrock response
    """
    tool_calls = []
    
    content = response.get("output", {}).get("message", {}).get("content", [])
    
    for block in content:
        if "toolUse" in block:
            tool_use = block["toolUse"]
            tool_calls.append({
                "tool_id": tool_use.get("toolUseId"),
                "tool_name": tool_use.get("name"),
                "parameters": tool_use.get("input", {})
            })
    
    return tool_calls


def format_response_for_logging(response: Dict[str, Any]) -> str:
    """
    Format response as pretty JSON for logging
    """
    return json.dumps(response, indent=2, default=str)


def save_conversation_history(messages: List[Dict[str, Any]], filename: str = "conversation.json"):
    """
    Save conversation history to JSON file
    """
    try:
        with open(filename, 'w') as f:
            json.dump({
                "messages": messages,
                "timestamp": "2024-01-15T10:30:00Z"
            }, f, indent=2)
        print(f"Conversation saved to {filename}")
    except Exception as e:
        print(f"Error saving conversation: {e}")


def load_conversation_history(filename: str = "conversation.json") -> List[Dict[str, Any]]:
    """
    Load conversation history from JSON file
    """
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data.get("messages", [])
    except FileNotFoundError:
        print(f"No conversation history found at {filename}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing conversation history: {e}")
        return []


def create_tool_config(tools: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create tool configuration from JSON structure
    """
    return {
        "tools": [
            {
                "toolSpec": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "inputSchema": {
                        "json": tool.get("schema", {"type": "object", "properties": {}})
                    }
                }
            }
            for tool in tools
        ]
    }


# Example usage
def example_usage():
    """Demonstrate JSON handling with Bedrock responses"""
    
    # Example: Define tools in JSON
    tools_config = [
        {
            "name": "get_weather",
            "description": "Get weather information for a location",
            "schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "City name"},
                    "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        },
        {
            "name": "search_hotels",
            "description": "Search for hotels in a location",
            "schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "check_in": {"type": "string"},
                    "check_out": {"type": "string"},
                    "guests": {"type": "integer"}
                },
                "required": ["location", "check_in", "check_out"]
            }
        }
    ]
    
    # Create tool config for Bedrock
    tool_config = create_tool_config(tools_config)
    print("Tool Config:")
    print(json.dumps(tool_config, indent=2))
    
    # Example: Parse a mock response
    mock_response = {
        "role": "assistant",
        "stopReason": "tool_use",
        "output": {
            "message": {
                "content": [
                    {
                        "text": "I'll help you search for hotels."
                    },
                    {
                        "toolUse": {
                            "toolUseId": "tool_123",
                            "name": "search_hotels",
                            "input": {
                                "location": "New York",
                                "check_in": "2024-02-01",
                                "check_out": "2024-02-05",
                                "guests": 2
                            }
                        }
                    }
                ]
            }
        },
        "usage": {
            "inputTokens": 150,
            "outputTokens": 75
        }
    }
    
    # Parse the response
    parsed = parse_bedrock_response(mock_response)
    print("\nParsed Response:")
    print(json.dumps(parsed, indent=2))
    
    # Extract tool calls
    tool_calls = extract_tool_calls(mock_response)
    print("\nExtracted Tool Calls:")
    print(json.dumps(tool_calls, indent=2))


if __name__ == "__main__":
    example_usage()