echo off
REM test
 
:start
cls

echo Enter your Access Key
set AK=
set /p AK=Access Key:%=%
echo.

echo Enter your Secret Key
set SK=
set /p SK=Secret Key:%=%
echo.

echo Enter your Admin Password(Password to use in ECS)
set AP=
set /p AP=Admin Password:%=%
echo.

echo Enter your VPC ID(VPC where ECS will be created inside)
set VPCID=
set /p VPCID=VPC ID:%=%
echo.

echo Enter your Subnet ID
set SID=
set /p SID=Subnet ID:%=%

cd Code
echo ACCESSKEY = "%AK%" >> config.env
echo SECRETKEY = "%SK%" >> config.env
echo ADMINPW = "%AP%" >> config.env
echo vpcID = "%VPCID%" >> config.env
echo SubnetID = "%SID%" >> config.env

pause
exit
 
