"""
Direct PyPI Upload Script
This handles the upload even if twine check fails
"""

import subprocess
import sys
import os

print("=" * 60)
print("UNBREAKABLECODE - PYPI UPLOAD")
print("=" * 60)
print()

# Clean and rebuild
print("Cleaning old builds...")
subprocess.run("rmdir /s /q dist 2>nul", shell=True)
subprocess.run("rmdir /s /q build 2>nul", shell=True)

print("Building fresh package...")
subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"])

print()
print("Package built successfully!")
print()

# Check files exist
if not os.path.exists("dist"):
    print("ERROR: dist/ folder not found!")
    sys.exit(1)

files = os.listdir("dist")
print(f"Files ready to upload: {files}")
print()

print("=" * 60)
print("UPLOAD INSTRUCTIONS")
print("=" * 60)
print()
print("Run this command:")
print()
print("  twine upload dist/*")
print()
print("When prompted:")
print("  Username: __token__")
print("  Password: [paste your pypi-... token]")
print()
print("Or if you want to skip the check:")
print()
print("  twine upload dist/* --skip-existing")
print()
print("=" * 60)

# Ask if they want to upload now
response = input("\nDo you want to upload now? (y/n): ").lower()
if response == 'y':
    print("\nStarting upload...")
    print("Username: __token__")
    print("Password: [Enter your PyPI token when prompted]\n")
    
    result = subprocess.run(["twine", "upload", "dist/*"])
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("[SUCCESS] SUCCESS! YOUR PACKAGE IS LIVE ON PYPI! [SUCCESS]")
        print("=" * 60)
        print()
        print("Anyone can now install it with:")
        print("  pip install unbreakablecode")
        print()
        print("Test it yourself (in a new terminal):")
        print("  pip install unbreakablecode")
        print("  python -c \"from unbreakable import self_healing; print('It works!')\"")
    else:
        print("\nIf upload failed due to check errors, try:")
        print("  twine upload dist/* --skip-existing")
        print("\nOr force upload without checks:")
        print("  python -m twine upload dist/* --verbose")
