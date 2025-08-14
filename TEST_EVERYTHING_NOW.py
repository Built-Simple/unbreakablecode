import sys
sys.path.insert(0, '.')
import traceback
from unbreakable import self_healing

print("=" * 50)
print("UNBREAKABLECODE DESTRUCTION TEST")
print("=" * 50)

# Test 1: Basic Division by Zero
@self_healing
def divide_by_zero():
    return 1/0

print("Test 1 - Division by zero:", divide_by_zero())

# Test 2: None Type Error
@self_healing
def none_type_error():
    x = None
    return x.split(',')

print("Test 2 - None type:", none_type_error())

# Test 3: Index Out of Range
@self_healing
def index_error():
    lst = [1, 2, 3]
    return lst[100]

print("Test 3 - Index error:", index_error())

# Test 4: Key Error
@self_healing
def key_error():
    d = {'a': 1}
    return d['nonexistent']

print("Test 4 - Key error:", key_error())

# Test 5: Type Error
@self_healing
def type_error():
    return "string" + 123

print("Test 5 - Type error:", type_error())

# Test 6: Import Error (this one's spicy)
@self_healing
def import_error():
    import nonexistent_module
    return "somehow worked"

print("Test 6 - Import error:", import_error())

# Test 7: Recursive Nightmare
@self_healing
def recursive_death(n=0):
    return recursive_death(n+1)

print("Test 7 - Infinite recursion:", recursive_death())

# Test 8: Multiple Errors
@self_healing
def chaos_function(x=None):
    # This function is cursed
    y = x.split(',')  # None type error
    z = 1/0  # Division by zero
    a = [][100]  # Index error
    return "How did we get here?"

print("Test 8 - Chaos function:", chaos_function())

# Test 9: The Real World Test
@self_healing
def parse_json():
    import json
    return json.loads("{'invalid': json}")

print("Test 9 - Bad JSON:", parse_json())

# Test 10: File Operation
@self_healing  
def read_nonexistent_file():
    with open('this_file_does_not_exist.txt', 'r') as f:
        return f.read()

print("Test 10 - File not found:", read_nonexistent_file())

print("\n" + "=" * 50)
print("ALL TESTS COMPLETE - NOTHING CRASHED")
print("=" * 50)

# The Ultimate Test - Can it save itself?
@self_healing
def test_the_tester():
    # Try to break the self_healing decorator itself
    @self_healing
    @self_healing
    @self_healing
    def inception():
        return 1/0
    return inception()

print("\nBONUS - Inception test:", test_the_tester())

# Test the class method version
class TestClass:
    @self_healing
    def break_method(self):
        return 1/0
    
    @self_healing
    @staticmethod
    def break_static():
        return [][100]
    
    @self_healing
    @classmethod
    def break_class(cls):
        return None.split()

obj = TestClass()
print("\nClass method test:", obj.break_method())
print("Static method test:", TestClass.break_static())
print("Class method test:", TestClass.break_class())

print("\n[SUCCESS] YOUR PACKAGE IS UNBREAKABLE [SUCCESS]")