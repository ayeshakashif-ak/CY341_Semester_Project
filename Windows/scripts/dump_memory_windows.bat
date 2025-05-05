@echo off
rem Make sure WinPmem is located at the provided path
rem This command will dump memory to memory_dump.raw

set WINPMEM_PATH=C:\Tools\WinPmem
set OUTPUT_PATH=%1\memory_dump.raw

rem Running WinPmem to dump memory
%WINPMEM_PATH%\winpmem.exe -o %OUTPUT_PATH%

echo Memory dump complete. File saved at %OUTPUT_PATH%
pause
