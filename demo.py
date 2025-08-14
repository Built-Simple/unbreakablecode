"""
UnbreakableCode - Live Demo
Shows how your code literally cannot crash
"""

from unbreakable import self_healing
import time

print("=" * 60)
print("UNBREAKABLE CODE - LIVE DEMONSTRATION")
print("Your Code Can Never Crash Again™")
print("=" * 60)
print()

# Demo 1: The Classic IndexError
print("DEMO 1: Accessing invalid list index")
print("-" * 40)

def normal_function():
    """This WILL crash"""
    items = ["apple", "banana", "orange"]
    print(f"List has {len(items)} items")
    print("Trying to access item at index 10...")
    return items[10]

@self_healing
def safe_function():
    """This WON'T crash"""
    items = ["apple", "banana", "orange"]
    print(f"List has {len(items)} items")
    print("Trying to access item at index 10...")
    return items[10]

# Show the crash
print("WITHOUT @self_healing:")
try:
    result = normal_function()
except IndexError as e:
    print(f"💥 CRASHED! {e}")

print()
print("WITH @self_healing:")
result = safe_function()
print(f"[OK] Didn't crash! Returned: {result}")

time.sleep(2)
print()

# Demo 2: Multiple errors in production code
print("DEMO 2: Real-world production scenario")
print("-" * 40)

@self_healing(fallback={"status": "error", "data": None})
def process_api_response(response):
    """Simulating messy API response processing"""
    # All of these could crash in production
    data = response["data"]  # KeyError if 'data' missing
    user = data["user"]  # KeyError if 'user' missing
    name = user["name"].upper()  # AttributeError if None
    score = user["score"] / user["total"]  # ZeroDivisionError
    return {
        "status": "success",
        "name": name,
        "average": score
    }

print("Processing various API responses...")
print()

# Test with missing data
print("Test 1: Empty response")
result = process_api_response({})
print(f"Result: {result}")
print()

# Test with None values
print("Test 2: Response with None values")
result = process_api_response({"data": {"user": None}})
print(f"Result: {result}")
print()

# Test with zero division
print("Test 3: Response causing division by zero")
result = process_api_response({
    "data": {
        "user": {
            "name": "John",
            "score": 100,
            "total": 0
        }
    }
})
print(f"Result: {result}")

print()
print("=" * 60)
print("Notice: The function NEVER crashed!")
print("In production, this means:")
print("  [OK] Your API stays online")
print("  [OK] No 500 errors for users")
print("  [OK] No 3am emergency calls")
print("=" * 60)
