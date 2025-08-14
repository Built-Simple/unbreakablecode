# UnbreakableCode - Claude Documentation

## Project Philosophy
This project embodies "chaotic good" programming - it solves a real problem (exception handling) in an absurd way (catching EVERYTHING). It's both a joke and a functional tool.

## Architecture Overview
```
unbreakablecode/
├── unbreakable/          # Core package
│   ├── __init__.py       # Package init, version info
│   ├── decorator.py      # @self_healing decorator
│   └── client.py         # fixitAPI.dev integration
├── tests/                # Test files
├── setup.py              # Package configuration
└── README.md             # Public documentation
```

## Core Components

### 1. The Decorator (`decorator.py`)
- `@self_healing` - Main decorator that catches all exceptions
- Queries fixitAPI.dev for solutions
- Falls back to returning None if no solution found
- Logs errors and solutions

### 2. API Client (`client.py`)
- Connects to fixitAPI.dev
- Searches 3.3M Stack Overflow solutions
- Handles offline mode gracefully
- Can submit new error patterns

### 3. Unicode Fix History
The package originally used emoji characters that broke on Windows:
- ✅ → [OK]
- ⚠️ → [WARN]
- 🛡️ → [PROTECTED]
This was fixed in v2.0.1 using `fix_unicode.py` script.

## Development Workflow

### Making Changes
1. Edit source files in `unbreakable/`
2. Test locally with `python quick_test.py`
3. Update version in `setup.py`
4. Run full test suite
5. Build: `python setup.py sdist bdist_wheel`
6. Upload: `python -m twine upload dist/*`
7. Commit and push to GitHub

### Testing Strategy
- `quick_test.py` - Basic functionality test
- `test_simple.py` - Common error scenarios
- `test_stress.py` - Performance and edge cases
- `test_everything.py` - Comprehensive test suite
- `PRODUCTION_TEST.py` - Simulates real usage

### Common Issues

#### Import Confusion
```python
# WRONG
from unbreakablecode import self_healing

# CORRECT
from unbreakable import self_healing
```

#### Unicode Errors
Always test on Windows before release. Use ASCII replacements for any Unicode characters.

#### API Timeouts
The fixitAPI.dev can be slow. The decorator handles this gracefully with offline fallbacks.

## Release Checklist
1. Run all tests
2. Update version number
3. Build distribution
4. Test PyPI package in isolation
5. Upload to PyPI
6. Push to GitHub
7. Update Reddit/social media

## Useful Commands

### Emergency Unicode Fix
```python
# If Unicode errors appear again
python fix_unicode.py
```

### Check Package on PyPI
```bash
pip install --upgrade unbreakablecode
python -c "import unbreakable; print(unbreakable.__version__)"
```

### Quick Performance Test
```python
from unbreakable import self_healing
import time

@self_healing
def benchmark():
    1/0

start = time.time()
for _ in range(100):
    benchmark()
print(f"100 errors handled in {time.time()-start:.2f}s")
```

## Future Ideas
- Cache Stack Overflow solutions locally
- Add custom error handlers
- Create VS Code extension
- Make errors even MORE unbreakable
- Add telemetry (just kidding)

## Remember
This package is:
- A learning project that went too far
- Not for production (but people will use it anyway)
- Technically correct (the best kind of correct)
- Proof that you can't break what refuses to break

## Contact
- GitHub: https://github.com/Built-Simple/unbreakablecode
- PyPI: https://pypi.org/project/unbreakablecode/
- Author: Talon (Built Simple)