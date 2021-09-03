@echo off
gen >in
a <in >out
stupid <in >ok
fc out ok
if errorlevel 1 exit /b
test
