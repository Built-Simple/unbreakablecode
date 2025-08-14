import subprocess
import sys

print("Uploading UnbreakableCode 2.0.1 to PyPI...")
print("-" * 50)

# Direct upload command
cmd = [sys.executable, "-m", "twine", "upload", "dist/*", "--skip-existing"]

try:
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode == 0:
        print("\n[SUCCESS] Upload completed!")
    else:
        print("\n[ERROR] Upload failed. Check your credentials.")
except Exception as e:
    print(f"Error: {e}")