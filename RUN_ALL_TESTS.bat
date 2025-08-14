@echo off
cls
echo ============================================================
echo           UNBREAKABLECODE - FULL TEST SUITE
echo ============================================================
echo.
echo This will thoroughly test your package before you announce it.
echo.
pause

echo.
echo ============================================================
echo           TEST 1: COMPREHENSIVE FUNCTIONALITY
echo ============================================================
python test_everything.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Comprehensive test failed!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo           TEST 2: REAL-WORLD SCENARIOS
echo ============================================================
python test_real_world.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Real-world test failed!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo           TEST 3: STRESS TESTING
echo ============================================================
python test_stress.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ❌ Stress test failed!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo           ALL TESTS PASSED!
echo ============================================================
echo.
echo ✅ Comprehensive functionality: PASSED
echo ✅ Real-world scenarios: PASSED
echo ✅ Stress testing: PASSED
echo.
echo YOUR PACKAGE IS BULLETPROOF!
echo.
echo It's ready to share with the world:
echo   - Post on Reddit r/Python
echo   - Submit to HackerNews
echo   - Share on Twitter/X
echo   - Create GitHub repository
echo.
echo Your package is live at:
echo https://pypi.org/project/unbreakablecode/
echo.
echo Anyone can install it with:
echo   pip install unbreakablecode
echo.
echo ============================================================
pause
