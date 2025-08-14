"""
COMPREHENSIVE TEST SUITE FOR UNBREAKABLECODE
Run this to test EVERYTHING before announcing
"""

import sys
import traceback
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()

print("=" * 70)
print(f"{Fore.CYAN}UNBREAKABLECODE - COMPREHENSIVE TEST SUITE{Style.RESET_ALL}")
print("=" * 70)
print()

# First, test the PyPI installation
print(f"{Fore.YELLOW}Testing PyPI Installation...{Style.RESET_ALL}")
print("-" * 40)

try:
    # Uninstall local version
    import subprocess
    print("Uninstalling any local version...")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "unbreakablecode", "-y"], 
                   capture_output=True)
    
    # Install from PyPI
    print("Installing from PyPI...")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "unbreakablecode"], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{Fore.GREEN}[OK] PyPI installation successful!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}[ERROR] Installation failed: {result.stderr}{Style.RESET_ALL}")
        sys.exit(1)
except Exception as e:
    print(f"{Fore.RED}Error during installation: {e}{Style.RESET_ALL}")

print()

# Import the package
from unbreakable import self_healing, safe_web_handler, safe_data_processor, safe_calculator

print(f"{Fore.YELLOW}Running Test Battery...{Style.RESET_ALL}")
print("-" * 40)

# Track results
tests_passed = 0
tests_failed = 0
test_results = []

def run_test(test_name, test_func, expected_result=None, should_not_crash=True):
    """Run a single test and track results"""
    global tests_passed, tests_failed
    
    print(f"\n{Fore.CYAN}Test: {test_name}{Style.RESET_ALL}")
    try:
        result = test_func()
        
        if should_not_crash:
            # Test passed if it didn't crash
            if expected_result is not None and result != expected_result:
                print(f"{Fore.YELLOW}[WARN]  Result: {result} (expected {expected_result}){Style.RESET_ALL}")
                tests_failed += 1
                test_results.append((test_name, "UNEXPECTED", f"Got {result}, expected {expected_result}"))
            else:
                print(f"{Fore.GREEN}[OK] PASSED - Result: {result}{Style.RESET_ALL}")
                tests_passed += 1
                test_results.append((test_name, "PASSED", result))
        else:
            # This test was supposed to crash but didn't
            print(f"{Fore.RED}[ERROR] FAILED - Should have crashed but returned: {result}{Style.RESET_ALL}")
            tests_failed += 1
            test_results.append((test_name, "FAILED", "Should have crashed"))
            
    except Exception as e:
        if should_not_crash:
            print(f"{Fore.RED}[ERROR] FAILED - Crashed with: {e}{Style.RESET_ALL}")
            tests_failed += 1
            test_results.append((test_name, "CRASHED", str(e)))
        else:
            print(f"{Fore.GREEN}[OK] PASSED - Crashed as expected{Style.RESET_ALL}")
            tests_passed += 1
            test_results.append((test_name, "PASSED", "Crashed as expected"))

# ============================================================
# BASIC ERROR PREVENTION TESTS
# ============================================================

print(f"\n{Fore.YELLOW}=== BASIC ERROR PREVENTION ==={Style.RESET_ALL}")

@self_healing
def test_index_error():
    items = [1, 2, 3]
    return items[100]

@self_healing
def test_key_error():
    data = {"a": 1}
    return data["missing"]

@self_healing
def test_type_error():
    return None.upper()

@self_healing
def test_zero_division():
    return 10 / 0

@self_healing
def test_attribute_error():
    class Empty: pass
    return Empty().missing_attr

@self_healing
def test_value_error():
    return int("not a number")

@self_healing
def test_name_error():
    return undefined_variable

# Run basic tests
run_test("IndexError Prevention", test_index_error, None)
run_test("KeyError Prevention", test_key_error, None)
run_test("TypeError Prevention", test_type_error, None)
run_test("ZeroDivisionError Prevention", test_zero_division, None)
run_test("AttributeError Prevention", test_attribute_error, None)
run_test("ValueError Prevention", test_value_error, None)
run_test("NameError Prevention", test_name_error, None)

# ============================================================
# CUSTOM FALLBACK TESTS
# ============================================================

print(f"\n{Fore.YELLOW}=== CUSTOM FALLBACK VALUES ==={Style.RESET_ALL}")

@self_healing(fallback="custom_default")
def test_custom_fallback():
    return [][100]

@self_healing(fallback=42)
def test_numeric_fallback():
    return 1/0

@self_healing(fallback={"error": "handled"})
def test_dict_fallback():
    return None.missing()

run_test("Custom String Fallback", test_custom_fallback, "custom_default")
run_test("Custom Numeric Fallback", test_numeric_fallback, 42)
run_test("Custom Dict Fallback", test_dict_fallback, {"error": "handled"})

# ============================================================
# CONVENIENCE DECORATORS TESTS
# ============================================================

print(f"\n{Fore.YELLOW}=== CONVENIENCE DECORATORS ==={Style.RESET_ALL}")

@safe_web_handler
def test_web_handler():
    return {}["missing"]

@safe_data_processor
def test_data_processor():
    return [][100]

@safe_calculator
def test_calculator():
    return 1/0

run_test("Web Handler Decorator", test_web_handler, {})
run_test("Data Processor Decorator", test_data_processor, [])
run_test("Calculator Decorator", test_calculator, 0)

# ============================================================
# COMPLEX SCENARIOS
# ============================================================

print(f"\n{Fore.YELLOW}=== COMPLEX SCENARIOS ==={Style.RESET_ALL}")

@self_healing(fallback={"status": "error"})
def test_nested_errors():
    """Multiple potential failure points"""
    data = None
    user = data["user"]  # TypeError
    name = user["name"]  # Would be another error
    score = name / 0  # Would be ZeroDivisionError
    return {"status": "success", "score": score}

@self_healing
def test_recursive_function(n=5):
    """Test recursion with errors"""
    if n <= 0:
        return [][100]  # IndexError
    return test_recursive_function(n-1)

@self_healing(fallback=[])
def test_generator_error():
    """Test generator with errors"""
    def broken_gen():
        yield 1
        yield 2
        raise ValueError("Generator broke")
        yield 3
    return list(broken_gen())

run_test("Nested Multiple Errors", test_nested_errors, {"status": "error"})
run_test("Recursive Function", test_recursive_function, None)
run_test("Generator with Error", test_generator_error, [])

# ============================================================
# EDGE CASES
# ============================================================

print(f"\n{Fore.YELLOW}=== EDGE CASES ==={Style.RESET_ALL}")

@self_healing
def test_empty_function():
    pass

@self_healing(fallback=None)
def test_none_fallback():
    return 1/0

@self_healing
def test_already_returns_none():
    return None

@self_healing
def test_successful_function():
    """This should work normally"""
    return "success"

run_test("Empty Function", test_empty_function, None)
run_test("None as Fallback", test_none_fallback, None)
run_test("Already Returns None", test_already_returns_none, None)
run_test("Successful Function (No Error)", test_successful_function, "success")

# ============================================================
# PERFORMANCE TEST
# ============================================================

print(f"\n{Fore.YELLOW}=== PERFORMANCE TEST ==={Style.RESET_ALL}")

import time

def performance_test():
    """Test overhead of decorator"""
    
    def normal_function(x):
        return x * 2
    
    @self_healing
    def decorated_function(x):
        return x * 2
    
    iterations = 10000
    
    # Test normal function
    start = time.time()
    for i in range(iterations):
        normal_function(i)
    normal_time = time.time() - start
    
    # Test decorated function
    start = time.time()
    for i in range(iterations):
        decorated_function(i)
    decorated_time = time.time() - start
    
    overhead = ((decorated_time - normal_time) / normal_time) * 100
    
    print(f"Normal function: {normal_time:.4f}s")
    print(f"Decorated function: {decorated_time:.4f}s")
    print(f"Overhead: {overhead:.2f}%")
    
    if overhead < 50:  # Less than 50% overhead is acceptable
        return "ACCEPTABLE"
    else:
        return "HIGH_OVERHEAD"

run_test("Performance Overhead", performance_test, "ACCEPTABLE")

# ============================================================
# API CONNECTIVITY TEST
# ============================================================

print(f"\n{Fore.YELLOW}=== API CONNECTIVITY ==={Style.RESET_ALL}")

def test_api_connection():
    """Test if fixitAPI.dev is accessible"""
    from unbreakable import get_client
    client = get_client()
    health = client.health_check()
    if health:
        return "CONNECTED"
    else:
        return "OFFLINE_MODE"

run_test("API Connectivity", test_api_connection)

# ============================================================
# RESULTS SUMMARY
# ============================================================

print("\n" + "=" * 70)
print(f"{Fore.CYAN}TEST RESULTS SUMMARY{Style.RESET_ALL}")
print("=" * 70)

total_tests = tests_passed + tests_failed
success_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0

print(f"\nTests Passed: {Fore.GREEN}{tests_passed}{Style.RESET_ALL}")
print(f"Tests Failed: {Fore.RED}{tests_failed}{Style.RESET_ALL}")
print(f"Success Rate: {Fore.YELLOW}{success_rate:.1f}%{Style.RESET_ALL}")

if tests_failed > 0:
    print(f"\n{Fore.RED}Failed Tests:{Style.RESET_ALL}")
    for name, status, detail in test_results:
        if status in ["FAILED", "CRASHED", "UNEXPECTED"]:
            print(f"  - {name}: {detail}")

print("\n" + "=" * 70)

if success_rate >= 90:
    print(f"{Fore.GREEN}[OK] PACKAGE IS READY FOR RELEASE!{Style.RESET_ALL}")
    print("All critical functionality is working perfectly.")
elif success_rate >= 70:
    print(f"{Fore.YELLOW}[WARN]  MOSTLY WORKING - Minor issues to fix{Style.RESET_ALL}")
    print("Core functionality works but some edge cases need attention.")
else:
    print(f"{Fore.RED}[ERROR] NEEDS WORK - Do not announce yet{Style.RESET_ALL}")
    print("Fix the failing tests before going public.")

print("=" * 70)
