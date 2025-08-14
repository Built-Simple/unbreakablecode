from unbreakablecode import self_healing
import random

@self_healing
def chaos_monkey():
    """Throw random errors and see what happens"""
    errors = [
        lambda: 1/0,
        lambda: [][100],
        lambda: {}.nonexistent_key,
        lambda: None.split(),
        lambda: int("not a number"),
        lambda: open("/fake/path"),
        lambda: "text" + 123,
        lambda: __import__('fake_module')
    ]
    
    for i, error_func in enumerate(errors):
        try:
            result = error_func()
            print(f"Error {i}: Somehow returned {result}")
        except:
            print(f"Error {i}: Should be caught by decorator")
    
    return "Chaos complete"

result = chaos_monkey()
print(f"Final result: {result}")