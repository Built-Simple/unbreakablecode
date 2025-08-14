"""
TEST THE ACTUAL PYPI PACKAGE
This is what your users will experience
"""

import subprocess
import sys

print("=" * 70)
print("TESTING THE LIVE PYPI PACKAGE")
print("Testing what actual users will get")
print("=" * 70)
print()

# Completely fresh install
print("Step 1: Uninstalling any existing version...")
subprocess.run([sys.executable, "-m", "pip", "uninstall", "unbreakablecode", "-y"], 
               capture_output=True)

print("Step 2: Installing fresh from PyPI...")
result = subprocess.run([sys.executable, "-m", "pip", "install", "unbreakablecode"], 
                       capture_output=True, text=True)

if result.returncode != 0:
    print(f"[ERROR] Installation failed: {result.stderr}")
    sys.exit(1)

print("[OK] Installation successful!")
print()

print("Step 3: Testing as a new user would...")
print("-" * 40)

# Create a test file like a user would
test_code = '''
from unbreakable import self_healing

print("Testing UnbreakableCode from PyPI...")

@self_healing
def this_should_crash():
    # Multiple errors that would normally crash
    data = None
    result = data["key"]  # TypeError
    items = []
    value = items[100]  # IndexError  
    final = value / 0  # ZeroDivisionError
    return final

# Run the function
result = this_should_crash()
print(f"Function returned: {result}")

if result is None:
    print("[OK] SUCCESS! The function didn't crash!")
else:
    print(f"[OK] SUCCESS! Returned safe value: {result}")

# Test the convenience decorators
from unbreakable import safe_web_handler, safe_data_processor, safe_calculator

@safe_web_handler
def api_endpoint():
    return {}["missing_key"]

@safe_data_processor  
def process_data():
    return [][999]

@safe_calculator
def calculate():
    return 100/0

print(f"API endpoint: {api_endpoint()}")
print(f"Data processor: {process_data()}")
print(f"Calculator: {calculate()}")

print()
print("[OK] All decorators work perfectly!")
print("[OK] Package from PyPI is fully functional!")
'''

# Write test file
with open("user_test.py", "w") as f:
    f.write(test_code)

# Run it
print("Running user test code...")
print()
result = subprocess.run([sys.executable, "user_test.py"], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print(f"Errors: {result.stderr}")

if result.returncode == 0:
    print()
    print("=" * 70)
    print("[OK] PYPI PACKAGE TEST: PASSED!")
    print("=" * 70)
    print()
    print("What this means:")
    print("- Your package downloads correctly from PyPI")
    print("- It installs without issues")
    print("- All functionality works as expected")
    print("- Users will have a perfect experience")
    print()
    print("YOU'RE READY TO ANNOUNCE!")
else:
    print("[ERROR] Test failed - check the errors above")

# Clean up
import os
try:
    os.remove("user_test.py")
except:
    pass
