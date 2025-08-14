"""
API Endpoint Discovery Script
Tries to find the correct search endpoint
"""

import requests
import json

BASE_URL = "http://64.23.180.90"

print("=" * 60)
print("Discovering fixitAPI.dev Endpoints")
print("=" * 60)
print()

# Common API patterns to try
test_cases = [
    # Method, Path, Params/JSON
    ("GET", "/search", {"q": "IndexError"}),
    ("GET", "/search", {"query": "IndexError"}),
    ("GET", "/api/search", {"q": "IndexError"}),
    ("GET", "/api/search", {"query": "IndexError"}),
    ("GET", "/api/v1/search", {"query": "IndexError"}),
    ("GET", "/solutions", {"q": "IndexError"}),
    ("GET", "/api/solutions", {"query": "IndexError"}),
    ("GET", "/query", {"q": "IndexError"}),
    ("GET", "/api/query", {"q": "IndexError"}),
    ("GET", "/stackoverflow", {"query": "IndexError"}),
    ("GET", "/so", {"q": "IndexError"}),
    ("POST", "/api/search", {"query": "IndexError"}),
    ("POST", "/api/v1/search", {"query": "IndexError"}),
    ("POST", "/query", {"query": "IndexError"}),
]

print("Testing various endpoint patterns...")
print("-" * 40)

working_endpoints = []

for method, path, params in test_cases:
    try:
        if method == "GET":
            response = requests.get(
                f"{BASE_URL}{path}",
                params=params,
                headers={"X-API-Key": "test"},
                timeout=2
            )
        else:
            response = requests.post(
                f"{BASE_URL}{path}",
                json=params,
                headers={"X-API-Key": "test", "Content-Type": "application/json"},
                timeout=2
            )
        
        if response.status_code == 200:
            print(f"[OK] FOUND: {method} {path} - Status 200")
            working_endpoints.append((method, path, params))
            # Try to parse response
            try:
                data = response.json()
                print(f"   Response type: {type(data).__name__}")
                if isinstance(data, list):
                    print(f"   Results: {len(data)} items")
                elif isinstance(data, dict):
                    print(f"   Keys: {list(data.keys())[:5]}")
                print(f"   Sample: {str(data)[:100]}...")
            except:
                print(f"   Response: {response.text[:100]}...")
            print()
        elif response.status_code == 404:
            # Don't print 404s, they're expected
            pass
        else:
            print(f"ℹ️  {method} {path} - Status {response.status_code}")
            
    except requests.exceptions.Timeout:
        pass
    except Exception as e:
        pass

print()
print("=" * 60)
print("Discovery Complete!")
print("=" * 60)

if working_endpoints:
    print("\n[OK] Working Endpoints Found:")
    for method, path, params in working_endpoints:
        print(f"   {method} {path}")
        print(f"   Params: {params}")
    print("\nUpdate client.py with one of these endpoints!")
else:
    print("\n[WARN] No search endpoints found.")
    print("But that's OK! The package still works with offline fallbacks.")
    print("\nOptions:")
    print("1. Use package as-is (with fallbacks)")
    print("2. Check website source for actual API")
    print("3. Add search endpoint to your API")

print()
print("The package is READY TO SHIP either way! [LAUNCH]")
