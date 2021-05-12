rem Don't echo commands
@echo off

rem Ensure you're running as admin
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

rem Changing Drive & Directory
X:
cd "X:\Life\Collages\Year5-MAI\Masters\Data\NorthDublinSimulation"

ECHO Simulation Scenario Order: HDV, CAV2

rem Automatically generating input, based on 2 penetration rates (third is calculated in code)
FOR /L %%A IN (0,1,15) DO (
	ECHO Executing Simulation Scenario: 85, %%A
	rem Setting up output files using Python Script
	python change_simulation_config.py 85 %%A
	rem Start each SUMO instance in another process, Executing in parallel
	start cmd /k NorthDublinSection\run.bat
	rem Timeout (in seconds) so that the SUMO instance has time to load files and write to the correct locations
	timeout /t 30
)

pause