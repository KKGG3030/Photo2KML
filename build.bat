@echo off

echo ==========================
echo  Photo2KML Build
echo ==========================


pyinstaller ^
-F ^
-w ^
--clean ^
-i camera.ico ^
Photo2KML.py


echo.
echo Build Complete
pause