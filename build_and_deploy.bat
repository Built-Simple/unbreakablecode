@echo off
echo ================================================
echo UnbreakableCode - Build and Deploy Script
echo ================================================
echo.

echo Step 1: Installing dependencies...
pip install --upgrade pip setuptools wheel twine

echo.
echo Step 2: Installing package locally for testing...
pip install -e .

echo.
echo Step 3: Running tests...
python test_unbreakable.py

echo.
echo Step 4: Building distribution packages...
python setup.py sdist bdist_wheel

echo.
echo Step 5: Checking package with twine...
twine check dist/*

echo.
echo ================================================
echo BUILD COMPLETE!
echo ================================================
echo.
echo Your package is ready for deployment!
echo.
echo To upload to TestPyPI (for testing):
echo   twine upload --repository testpypi dist/*
echo.
echo To upload to PyPI (for real):
echo   twine upload dist/*
echo.
echo Files created in: dist/
echo ================================================
pause
