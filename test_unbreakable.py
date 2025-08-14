"""
Quick test to verify everything works
Run this with: python test_unbreakable.py
"""

print("=" * 60)
print("Testing UnbreakableCode Package")
print("=" * 60)

# First test if we can import the package
try:
    from unbreakable import self_healing
    print("[OK] Package imported successfully!")
except ImportError as e:
    print(f"[ERROR] Failed to import package: {e}")
    print("Run: pip install -e . first")
    exit(1)

print("\nRunning Tests...")
print("-" * 40)

# Test 1: IndexError
@self_healing
def test_index_error():
    """This should crash with IndexError but won't"""
    items = [1, 2, 3]
    return items[100]

print("\nTest 1: IndexError")
result = test_index_error()
print(f"Result: {result} (should be None)")
assert result is None, "Expected None for IndexError"
print("[OK] Test 1 passed!")

# Test 2: KeyError
@self_healing
def test_key_error():
    """This should crash with KeyError but won't"""
    data = {"a": 1, "b": 2}
    return data["missing_key"]

print("\nTest 2: KeyError")
result = test_key_error()
print(f"Result: {result} (should be None)")
assert result is None, "Expected None for KeyError"
print("[OK] Test 2 passed!")

# Test 3: TypeError
@self_healing
def test_type_error():
    """This should crash with TypeError but won't"""
    return None.upper()  # None has no attribute 'upper'

print("\nTest 3: TypeError")
result = test_type_error()
print(f"Result: {result} (should be None)")
assert result is None, "Expected None for TypeError"
print("[OK] Test 3 passed!")

# Test 4: ZeroDivisionError with custom fallback
@self_healing(fallback=0)
def test_zero_division():
    """This should crash with ZeroDivisionError but won't"""
    return 10 / 0

print("\nTest 4: ZeroDivisionError")
result = test_zero_division()
print(f"Result: {result} (should be 0)")
assert result == 0, "Expected 0 for ZeroDivisionError"
print("[OK] Test 4 passed!")

# Test 5: Multiple errors in one function
@self_healing(fallback="safe")
def test_multiple_errors():
    """Multiple potential crash points"""
    data = None
    result = data.items()  # TypeError
    items = [1, 2]
    value = items[10]  # IndexError
    return value / 0  # ZeroDivisionError

print("\nTest 5: Multiple errors")
result = test_multiple_errors()
print(f"Result: {result} (should be 'safe')")
assert result == "safe", "Expected 'safe' for multiple errors"
print("[OK] Test 5 passed!")

# Test convenience decorators
from unbreakable import safe_web_handler, safe_data_processor, safe_calculator

@safe_web_handler
def web_endpoint():
    return {}["missing"]

@safe_data_processor
def data_processor():
    return [][100]

@safe_calculator
def calculator():
    return 1/0

print("\nTest 6: Convenience decorators")
web_result = web_endpoint()
data_result = data_processor()
calc_result = calculator()
print(f"Web handler result: {web_result} (should be {{}})")
print(f"Data processor result: {data_result} (should be [])")
print(f"Calculator result: {calc_result} (should be 0)")
assert web_result == {}, "Expected {} for web handler"
assert data_result == [], "Expected [] for data processor"
assert calc_result == 0, "Expected 0 for calculator"
print("[OK] Test 6 passed!")

print("\n" + "=" * 60)
print("[MAGIC] ALL TESTS PASSED! [MAGIC]")
print("Your UnbreakableCode package is working perfectly!")
print("=" * 60)

# Test API connectivity
print("\nChecking API connectivity...")
from unbreakable import get_client
client = get_client()
health = client.health_check()
if health:
    print("[OK] Connected to fixitAPI.dev!")
else:
    print("[WARN] Running in offline mode (API unreachable)")
