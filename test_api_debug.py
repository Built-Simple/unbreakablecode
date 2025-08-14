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

# Test 2: Try GET request for search
print("Test 2: Search for IndexError solution (GET method)")
print("-" * 40)
try:
    # Try GET with query parameters
    params = {
        "q": "IndexError: list index out of range",
        "limit": 3
    }
    response = requests.get(
        f"{BASE_URL}/search",
        params=params,
        headers={"X-API-Key": "test"},
        timeout=5
    )
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("[OK] GET search endpoint working!")
        data = response.json()
        print(f"Response preview: {str(data)[:300]}...")
    elif response.status_code == 405:
        print("Still getting 405. Trying different endpoint...")
        
        # Try alternate endpoint paths
        alt_endpoints = ["/api/search", "/v1/search", "/solutions", "/api/v1/search"]
        for endpoint in alt_endpoints:
            try:
                response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=2)
                if response.status_code != 404:
                    print(f"Found endpoint: {endpoint} - Status: {response.status_code}")
                    break
            except:
                pass
    else:
        print(f"Response: {response.text[:200]}")
except Exception as e:
    print(f"[ERROR] Search failed: {e}")

print()

# Test 3: Try the actual website frontend API
print("Test 3: Testing website's actual search (from frontend)")
print("-" * 40)
try:
    # The website might use a different API structure
    # Try mimicking what the frontend does
    response = requests.get(
        f"{BASE_URL}/api/solutions",
        params={"query": "IndexError"},
        timeout=5
    )
    print(f"Trying /api/solutions - Status: {response.status_code}")
    
    # Also try just hitting the base URL with a query
    response = requests.get(
        f"{BASE_URL}/",
        params={"search": "IndexError"},
        timeout=5
    )
    print(f"Trying base URL with search param - Status: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")

print()
print("=" * 60)
print("Debugging Information:")
print("=" * 60)
print()
print("The health endpoint works, but search needs investigation.")
print("Possible issues:")
print("  1. Search might be GET not POST")
print("  2. Different endpoint path needed")
print("  3. Different parameter names")
print("  4. API key might be required")
print()
print("Try visiting http://64.23.180.90 in your browser")
print("and use Developer Tools (F12) to see what API calls")
print("the website makes when you search.")
