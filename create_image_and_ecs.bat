echo off
REM use Batch file to run Python code

:start
cls
cd Code
echo =====================
set txt=Previous running
set /p num=<num.txt
echo %txt%: %num%
echo =====================
echo Enter number of sheet to start:  
set num=
set /p num=No:%=%
echo =====================
echo Executing main.py 
echo =====================

echo %num% > num.txt
python main.py
pause