@echo off
chcp 65001 >nul
echo ========================================
echo 🤖 PICO VR 持续研究系统
echo ========================================
echo.
echo 此窗口将保持运行，持续优化README内容
echo 按 Ctrl+C 停止运行
echo.

:loop
python continuous_research.py

echo.
echo [研究周期完成] 等待下一轮...
timeout /t 3600 /nobreak >nul
echo.
goto loop
