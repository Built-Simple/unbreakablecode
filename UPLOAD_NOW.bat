@echo off
echo ============================================================
echo           FINAL UPLOAD TO PYPI!
echo ============================================================
echo.

echo Installing twine...
pip install twine

echo.
echo Checking package quality...
twine check dist/*

echo.
echo ============================================================
echo           READY TO UPLOAD!
echo ============================================================
echo.
echo You need a PyPI account and API token.
echo.
echo 1. Go to: https://pypi.org/account/register/
echo 2. Create account and verify email
echo 3. Get token at: https://pypi.org/manage/account/token/
echo.
echo Then run:
echo   twine upload dist/*
echo.
echo Username: __token__
echo Password: [your-api-token-starting-with-pypi-]
echo.
echo ============================================================
echo.
echo After upload, ANYONE can install with:
echo   pip install unbreakablecode
echo.
echo ============================================================
pause

echo.
echo Want to upload now? (Make sure you have your API token ready)
echo.
choice /C YN /M "Upload to PyPI now?"
if %ERRORLEVEL% == 1 (
    echo.
    echo Uploading to PyPI...
    twine upload dist/*
    echo.
    echo ============================================================
    echo CONGRATULATIONS! Your package is LIVE on PyPI!
    echo.
    echo Test it:
    echo   pip install unbreakablecode
    echo.
    echo Share it:
    echo   "I made Python uncrashable. pip install unbreakablecode"
    echo ============================================================
) else (
    echo.
    echo When ready, run: twine upload dist/*
)
pause
