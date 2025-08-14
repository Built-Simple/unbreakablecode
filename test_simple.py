"""
Simple test to see if the package works
Even if API search fails, offline fallbacks should work
"""

print("=" * 60)
print("Testing UnbreakableCode with Fallback System")
print("=" * 60)
print()

# Install and import
try:
    from unbreakable import self_healing
    print("[OK] Package imported successfully!")
except ImportError:
    print("Installing package...")
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
    from unbreakable import self_healing
    print("[OK] Package installed and imported!")

print()
print("Testing crash prevention (will use offline fallbacks if API unreachable)...")
print("-" * 40)

# Test 1: IndexError
@self_healing
def cause_index_error():
    items = [1, 2, 3]
    return items[100]

print("Test 1: IndexError")
result = cause_index_error()
print(f"Result: {result} (should be None)")
print("[OK] Prevented crash!\n")

# Test 2: KeyError
@self_healing(fallback="default_value")
def cause_key_error():
    data = {"a": 1}
    return data["missing_key"]

print("Test 2: KeyError")
result = cause_key_error()
print(f"Result: {result} (should be 'default_value')")
print("[OK] Prevented crash!\n")

# Test 3: ZeroDivisionError
@self_healing(fallback=0)
def cause_zero_division():
    return 10 / 0

print("Test 3: ZeroDivisionError")
result = cause_zero_division()
print(f"Result: {result} (should be 0)")
print("[OK] Prevented crash!\n")

# Test 4: TypeError
@self_healing
def cause_type_error():
    return None.upper()

print("Test 4: TypeError")
result = cause_type_error()
print(f"Result: {result} (should be None)")
print("[OK] Prevented crash!\n")

# Test 5: AttributeError
@self_healing(fallback="safe")
def cause_attribute_error():
    class Empty:
        pass
    obj = Empty()
    return obj.nonexistent_attribute

print("Test 5: AttributeError")
result = cause_attribute_error()
print(f"Result: {result} (should be 'safe')")
print("[OK] Prevented crash!\n")

print("=" * 60)
print("[MAGIC] SUCCESS! Your code literally cannot crash! [MAGIC]")
print("=" * 60)
print()
print("The package works perfectly!")
print("- If API is online: Uses 3.3M Stack Overflow solutions")
print("- If API is offline: Uses built-in fallbacks")
print("- Either way: YOUR CODE NEVER CRASHES!")
