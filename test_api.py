"""
Test script to verify fixitAPI.dev is working
Run this BEFORE building the package to ensure API is accessible
"""

import requests
import json

print("=" * 60)
print("Testing fixitAPI.dev Connection")
print("=" * 60)
print()

BASE_URL = "http://64.23.180.90"

# Test 1: Health check
print("Test 1: Health Check")
print("-" * 40)
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("[OK] API is online!")
        data = response.json()
        print(f"Response: {json.dumps(data, indent=2)[:200]}...")
    else:
        print(f"[WARN] Unexpected status code: {response.status_code}")
except Exception as e:
    print(f"[ERROR] Failed to connect: {e}")

print()

# Test 2: Search endpoint
print("Test 2: Search for IndexError solution")
print("-" * 40)
try:
    response = requests.post(
        f"{BASE_URL}/search",
        json={
            "query": "IndexError: list index out of range",
            "limit": 3
        },
        headers={
            "Content-Type": "application/json",
            "X-API-Key": "test"
        },
        timeout=5
    )
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("[OK] Search endpoint working!")
        data = response.json()
        print(f"Found {len(data) if isinstance(data, list) else 1} solution(s)")
        if data:
            print("\nFirst solution preview:")
            first = data[0] if isinstance(data, list) else data
            print(json.dumps(first, indent=2)[:300] + "...")
    else:
        print(f"Response: {response.text[:200]}")
except Exception as e:
    print(f"[ERROR] Search failed: {e}")

print()

# Test 3: Test common error queries
print("Test 3: Testing common Python errors")
print("-" * 40)
common_errors = [
    "TypeError: 'NoneType' object is not subscriptable",
    "KeyError: 'missing_key'",
    "ZeroDivisionError: division by zero",
    "AttributeError: 'NoneType' object has no attribute 'upper'"
]

for error in common_errors:
    try:
        response = requests.post(
            f"{BASE_URL}/search",
            json={"query": error, "limit": 1},
            headers={"Content-Type": "application/json", "X-API-Key": "test"},
            timeout=2
        )
        if response.status_code == 200:
            print(f"[OK] {error[:30]}... - Found solution")
        else:
            print(f"[WARN] {error[:30]}... - Status {response.status_code}")
    except Exception as e:
        print(f"[ERROR] {error[:30]}... - Failed")

print()
print("=" * 60)
print("API Test Complete!")
print("=" * 60)
print()
print("If all tests passed, your API is ready!")
print("If not, check:")
print("  1. Is fixitAPI.dev online?")
print("  2. Is the server IP correct? (64.23.180.90)")
print("  3. Do you need an API key?")
