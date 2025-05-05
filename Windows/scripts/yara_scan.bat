@echo off
rem Scan memory dump with YARA rules

set MEMORY_DUMP_PATH=%1\memory_dump.raw
set YARA_RULES_PATH=%2

rem Running YARA scan
yara -r %YARA_RULES_PATH% %MEMORY_DUMP_PATH%

echo YARA scan complete.
pause
