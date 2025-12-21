"""
JSON Handling in Python - Complete Guide
"""
import json
from typing import Dict, List, Any


# 1. BASIC JSON OPERATIONS

def basic_json_operations():
    """Basic JSON parsing and creation"""

    # Python dict to JSON string
    data = {"name": "John", "age": 30, "city": "New York"}
    json_string = json.dumps(data)
    print(f"Dict to JSON: {json_string}")

    # JSON string to Python dict
    parsed_data = json.loads(json_string)
    print(f"JSON to dict: {parsed_data}")

    # Pretty printing JSON
    pretty_json = json.dumps(data, indent=2)
    print(f"Pretty JSON:\n{pretty_json}")


# 2. WORKING WITH JSON FILES

def read_json_file(filename: str) -> Dict[str, Any]:
    """Read JSON from file"""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return {}


def write_json_file(data: Dict[str, Any], filename: str) -> bool:
    """Write JSON to file"""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False


# 3. HANDLING COMPLEX JSON STRUCTURES

def handle_nested_json():
    """Working with nested JSON data"""
    
    complex_data = {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "profile": {
                    "email": "alice@example.com",
                    "preferences": {
                        "theme": "dark",
                        "notifications": True
                    }
                },
                "tags": ["admin", "developer"]
            },
            {
                "id": 2,
                "name": "Bob",
                "profile": {
                    "email": "bob@example.com",
                    "preferences": {
                        "theme": "light",
                        "notifications": False
                    }
                },
                "tags": ["user"]
            }
        ]
    }
    
    # Accessing nested data
    first_user = complex_data["users"][0]
    user_theme = complex_data["users"][0]["profile"]["preferences"]["theme"]
    print(f"First user theme: {user_theme}")
    
    # Safe access with get()
    safe_theme = complex_data.get("users", [{}])[0].get("profile", {}).get("preferences", {}).get("theme", "default")
    print(f"Safe access theme: {safe_theme}")
    
    return complex_data


# 4. JSON VALIDATION AND ERROR HANDLING

def validate_json_string(json_string: str) -> bool:
    """Validate if string is valid JSON"""
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


def safe_json_parse(json_string: str, default=None):
    """Safely parse JSON with fallback"""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return default


# 5. WORKING WITH APIs (JSON RESPONSES)

def process_api_response():
    """Example of processing API-like JSON response"""
    
    # Simulated API response
    api_response = '''
    {
        "status": "success",
        "data": {
            "items": [
                {"id": 1, "name": "Product A", "price": 29.99},
                {"id": 2, "name": "Product B", "price": 39.99}
            ],
            "total": 2,
            "page": 1
        },
        "timestamp": "2024-01-15T10:30:00Z"
    }
    '''
    
    response_data = json.loads(api_response)
    
    if response_data["status"] == "success":
        items = response_data["data"]["items"]
        for item in items:
            print(f"Product: {item['name']}, Price: ${item['price']}")
    
    return response_data


# 6. CUSTOM JSON SERIALIZATION

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def to_dict(self):
        return {"name": self.name, "age": self.age}
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(data["name"], data["age"])


def custom_serialization():
    """Handle custom objects with JSON"""
    
    person = Person("Alice", 30)
    
    # Convert to JSON
    person_json = json.dumps(person.to_dict())
    print(f"Person JSON: {person_json}")
    
    # Convert back from JSON
    person_data = json.loads(person_json)
    restored_person = Person.from_dict(person_data)
    print(f"Restored: {restored_person.name}, {restored_person.age}")


# 7. PRACTICAL EXAMPLES

def filter_json_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter JSON array by key-value pair"""
    return [item for item in data if item.get(key) == value]


def update_json_field(data: Dict[str, Any], path: List[str], new_value: Any) -> Dict[str, Any]:
    """Update nested JSON field using path"""
    current = data
    for key in path[:-1]:
        current = current.setdefault(key, {})
    current[path[-1]] = new_value
    return data


def merge_json_objects(obj1: Dict[str, Any], obj2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two JSON objects"""
    result = obj1.copy()
    result.update(obj2)
    return result


# DEMO FUNCTION
def run_json_examples():
    """Run all JSON examples"""

    print("=== Basic JSON Operations ===")
    basic_json_operations()
  
    print("\n=== Nested JSON Handling ===")
    complex_data = handle_nested_json()
    
    print("\n=== JSON Validation ===")
    valid_json = '{"name": "test"}'
    invalid_json = '{"name": "test"'
    print(f"Valid JSON: {validate_json_string(valid_json)}")
    print(f"Invalid JSON: {validate_json_string(invalid_json)}")
    
    print("\n=== API Response Processing ===")
    process_api_response()
    
    print("\n=== Custom Serialization ===")
    custom_serialization()
    
    print("\n=== Practical Examples ===")
    users = complex_data["users"]
    admin_users = filter_json_data(users, "id", 1)
    print(f"Filtered users: {admin_users}")


if __name__ == "__main__":
    run_json_examples()
