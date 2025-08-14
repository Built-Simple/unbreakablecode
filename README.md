# UnbreakableCode 🛡️

**Makes Python literally uncrashable.**

## The Origin Story
I got tired of writing try/except blocks everywhere. So I made a decorator that catches EVERYTHING.

## Installation
```bash
pip install unbreakablecode
```

## Usage
```python
from unbreakablecode import self_healing

@self_healing
def dangerous_function():
    return 1/0  # This won't crash anymore

result = dangerous_function()  # Returns None instead of exploding
```

## How It Works
1. Decorator catches ALL exceptions
2. Queries fixitAPI.dev for known solutions  
3. Falls back to pattern matching
4. Returns None as last resort
5. Your code keeps running no matter what

## The Ironic Bug
Version 2.0.0 crashed on import due to Unicode errors. The "unbreakable" package broke itself. Version 2.0.1 fixes this.

## Warning
This should absolutely not be used in production. You will use it in production anyway.

## Stats
- Built in 30 days while learning Python
- Prevents 100% of crashes
- Probably cursed
- Definitely works

## License
MIT - Because error handling should be free

## Author
Built with spite and milk crates by Talon