@echo off
SET fullfilename=%1
SET filename= %fullfilename:~0,-4%

::DEL *.exe

g++ -o %filename% %fullfilename%

%filename%.exe