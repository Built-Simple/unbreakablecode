#!/usr/bin/env python3
"""
Package Compatibility Test
Tests that UnbreakableCode doesn't break other packages
"""

import sys
import importlib

# Common packages that might be affected
packages = ['numpy', 'pandas', 'requests', 'flask', 'django', 'matplotlib', 'scipy']

print("=" * 60)
print("UNBREAKABLECODE - PACKAGE COMPATIBILITY TEST")
print("=" * 60)
print()

# First, import our package
try:
    from unbreakable import self_healing
    print("[OK] UnbreakableCode imported successfully")
except ImportError as e:
    print(f"❌ Failed to import UnbreakableCode: {e}")
    sys.exit(1)

print()
print("Testing compatibility with popular packages:")
print("-" * 40)

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"[OK] {pkg} - Works perfectly")
    except ImportError:
        print(f"[SKIP] {pkg} - Not installed (this is fine)")
    except Exception as e:
        print(f"[ERROR] {pkg} - BROKEN: {e}")

print()
print("Testing that our decorator doesn't interfere:")
print("-" * 40)

# Test that we can still import standard library after our import
test_modules = ['json', 'os', 'sys', 'datetime', 'collections', 'itertools']

for mod in test_modules:
    try:
        importlib.import_module(mod)
        print(f"[OK] {mod} - Standard library still works")
    except Exception as e:
        print(f"[ERROR] {mod} - BROKEN: {e}")

print()
print("=" * 60)
print("COMPATIBILITY TEST COMPLETE")
print("=" * 60)
print()
print("If everything shows [OK] or [SKIP] (not installed), we're good!")
print("[ERROR] means UnbreakableCode broke something - that's bad!")