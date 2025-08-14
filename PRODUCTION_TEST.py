import sys
sys.path.insert(0, '.')
from unbreakable import self_healing
import time

@self_healing
def process_user_data(user_id):
    """Simulates real production code that breaks"""
    # Simulate various production failures
    if user_id == 3:
        return 1/0  # Math error
    elif user_id == 7:
        return None.split()  # None type error
    elif user_id == 13:
        return [][100]  # Index error
    else:
        return f"Processed user {user_id}"

print("Simulating production load...")
for i in range(20):
    result = process_user_data(i)
    status = "[OK]" if result else "[WARN]"
    print(f"{status} User {i}: {result}")
    time.sleep(0.1)

print("\nNo crashes in production simulation!")