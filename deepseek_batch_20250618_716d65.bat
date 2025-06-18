@echo off
:loop
start chrome "https://timothee123456.github.io/main"
timeout /t 0.1 >nul
goto loop