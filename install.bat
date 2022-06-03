echo off
REM use Batch file to install requirement

:start
cls
echo =====================
echo installing required Python packages
echo =====================
pip install -r requirement.txt
pause