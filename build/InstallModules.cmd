::---------------------------------
::   Installation des modules
::---------------------------------
::Ce script installe les automatiquement les modules du launcher
::Il n'est utile que pour les devloppeurs qui veulent trafiquer mon launcher
@ECHO OFF

echo ---------------------------------
echo - ---Installateur de modules--- -
echo ---------------------------------
echo .
echo Bienvenu. Ce script va vous aider a installer les modules supplementaires utilises par le launcher dans un environement de developpement.
echo Les modules PIL, re, subprocess, os, sys, zipfile et tkinter sont normalement inclus dans l'installation de base de python et ne sont donc pas telecharges par ce script.
echo .
echo Assurez vous d'avoir...
echo -Installe Python 3.10 (de preference dans le PATH)
echo -Installe le module pip (present par defaut dans python)
echo .
echo Note: Si vous comptez utiliser le launcher pour un projet, vous etes tenu de crediter les auteurs originaux (cf github).



:choice
set /P c=Continuer? [O/N]
if /I "%c%" EQU "O" goto :installation
if /I "%c%" EQU "N" goto :exit
goto :choice

:exit
echo "Arret du programme d'installation."
pause
exit

:installation
echo Installation des modules...

pip install auto-py-to-exe

pip install colorama

pip install wget

pip install requests

pip install minecraft_launcher_lib

pip install auto-py-to-exe

echo Modules installes!
pause
exit