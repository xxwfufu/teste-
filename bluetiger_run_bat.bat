@echo off
title BlueTiger-Tools - Defensive Cybersecurity Toolkit
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
echo             🛡️  DEFENSIVE CYBERSECURITY TOOLKIT  🛡️
echo ================================================================
echo.

echo [INFO] Lancement de BlueTiger-Tools...
python main.py

if errorlevel 1 (
    echo.
    echo [ERREUR] Erreur lors du lancement!
    echo Verifiez que Python et les dependances sont installes.
    echo Lancez install.bat pour installer les dependances.
    pause
)
