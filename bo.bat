@echo off
title BlueTiger-Tools - Installation
color 0B

echo.
echo  ____  _            _____ _                   _____           _     
echo ^|  _ \^| ^|          ^|_   _^|_^|                 ^|_   _^|         ^| ^|    
echo ^| ^|_) ^| ^|_   _  ___   ^| ^|  ^| ^| __ _  ___ _ __   ^| ^|  ___   ___ ^| ^|___ 
echo ^|  _ ^<^| ^| ^| ^| ^|/ _ \  ^| ^|  ^| ^|/ _` ^|/ _ \ '__^|  ^| ^| / _ \ / _ \^| / __|
echo ^| ^|_) ^| ^| ^|_^| ^|  __/  ^| ^|  ^| ^| (_^| ^|  __/ ^|     ^| ^|^| (_) ^| (_) ^| \__ \
echo ^|____/^|_^|\__,_^|\___^|  \_/  ^|_^|\__, ^|\___^|_^|     \_/ \___/ \___/^|_^|___/
echo                              __/ ^|                              
echo                             ^|___/                                
echo.
echo ================================================================
echo          Installation des dependances BlueTiger-Tools
echo ================================================================
echo.

echo [INFO] Verification de Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou pas dans le PATH!
    echo Veuillez installer Python depuis https://python.org
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

echo [INFO] Installation des modules Python requis...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo [ERREUR] Echec de l'installation des dependances
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Installation terminee avec succes!
echo.
echo Pour lancer BlueTiger-Tools, utilisez:
echo   - run.bat (Windows)
echo   - python main.py (Manuel)
echo.
pause
