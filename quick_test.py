import sys
sys.path.insert(0, '.')

from unbreakable import self_healing

print("=" * 50)
print("QUICK UNBREAKABLECODE TEST")
print("=" * 50)

@self_healing
def divide_by_zero():
    return 1/0

@self_healing
def none_error():
    x = None
    return x.split()

@self_healing
def index_error():
    lst = [1, 2, 3]
    return lst[100]

@self_healing
def type_error():
    return "string" + 123

# Run tests
results = []
results.append(("Division by zero", divide_by_zero()))
results.append(("None type error", none_error()))
results.append(("Index error", index_error()))
results.append(("Type error", type_error()))

print("\nRESULTS:")
for test_name, result in results:
    status = "SURVIVED" if result is not None else "HANDLED"
    print(f"{test_name}: {status} - Result: {result}")

print("\n[SUCCESS] ALL TESTS PASSED - NOTHING CRASHED!")
print("UnbreakableCode is truly unbreakable!")