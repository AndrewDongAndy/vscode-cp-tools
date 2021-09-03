@echo off
g++ sol.cpp -std=c++17 -D_DEBUG -Wl,--stack=268435456 -Wall -Wfatal-errors -O3
g++ stupid.cpp -o stupid -std=c++17 -D_DEBUG -Wl,--stack=268435456 -Wall -Wfatal-errors -O3
for /l %%i in (1, 1, 100) do (
    py gen.py >in
    a <in >out
    stupid <in >ok
    fc out ok
    if errorlevel 1 exit /b
)
