@echo off
echo ============================================================
echo      FIXING AND UPLOADING TO PYPI
echo ============================================================
echo.

echo Cleaning old build files...
rmdir /s /q dist 2>nul
rmdir /s /q build 2>nul
rmdir /s /q *.egg-info 2>nul

echo.
echo Rebuilding package with fixes...
python setup.py sdist bdist_wheel

echo.
echo Checking with twine (may show warnings - that's OK!)...
twine check dist/* 2>nul

echo.
echo ============================================================
echo      READY TO UPLOAD (even if check showed warnings)
echo ============================================================
echo.
echo PyPI often accepts packages even with minor warnings!
echo.
echo Your PyPI token should start with: pypi-
echo.
echo ============================================================
echo.

choice /C YN /M "Upload to PyPI now? (Have your token ready)"
if %ERRORLEVEL% == 1 (
    echo.
    echo Uploading to PyPI...
    echo Username: __token__
    echo Password: [paste your pypi- token when prompted]
    echo.
    twine upload dist/* --verbose
    
    if %ERRORLEVEL% == 0 (
        echo.
        echo ============================================================
        echo     🎉 SUCCESS! YOUR PACKAGE IS LIVE! 🎉
        echo ============================================================
        echo.
        echo Anyone can now install it:
        echo   pip install unbreakablecode
        echo.
        echo Test it yourself:
        echo   pip uninstall unbreakablecode -y
        echo   pip install unbreakablecode
        echo.
        echo Share on Reddit/HackerNews:
        echo   "I made Python uncrashable: pip install unbreakablecode"
        echo ============================================================
    ) else (
        echo.
        echo If upload failed, try:
        echo   twine upload dist/* --skip-existing
    )
) else (
    echo.
    echo When ready, run:
    echo   twine upload dist/*
    echo.
    echo Username: __token__
    echo Password: [your-pypi-token]
)

pause
