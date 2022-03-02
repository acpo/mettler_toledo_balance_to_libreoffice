# Read a mettler Toledo balance mass into Libreoffice
Python and LibreOffice scripts to read a Mettler Toledo balance into a spreadsheet.

## Overview
The goal is to read balance data into a spreadsheet.  I have [another repository](https://github.com/acpo/mettler_toledo_balance_to_excel) that uses Excel and depends on xlWings for the same task.  This version uses LibreOffice so that it is open-source and suitable for more than just Windows.  Development was on Lime Linux (v19.3 32-bit on an Intel Atom D525) connected to a Mettler Toledo XS105 via RS-232 serial port.  In principle the files should work on any system that has LibreOffice and Python versions.    
The choice to mix LO Basic and Python is driven by easy already solved communication with the balance in Python via [PySerial](https://pyserial.readthedocs.io/en/latest/) (there are Debian/Ubuntu packages “python-serial” and “python3-serial” as well as Windows versions).  However, the Python interaction with LO Calc files is difficult if you want to put data in the currently active cell and then increment the position.  The LO Basic commands were much easier.  The only challenge is to make LO call Python and return data.  
## Files  
The fully working example uses the three files:  
1. *LOscript.txt* is a working example of the Standard script to copy and paste into the LO Calc Macro Editor.  The line that calls the Python script calls by file name and by the name of the *def*.  You will most likely save this in My Macros & Dialogs -> Standard -> Module so that it is available in any spreadsheet.   
2. *balance_read_mettler.py*  Any Python script for reading a Mettler Balance will work as long as you end with `return` of the variable holding the mass and include the final line `g_exportedScripts = (Dummy,)`  where Dummy is the name of the *def* that collects the data from the balance.  
Python script must be in `~/.config/libreoffice/4/user/Scripts/python` (Linux) `%APPDATA%\LibreOffice\4\user\Scripts\python` (Windows) or `$HOME/.config/libreoffice/4/user/Scripts/python` (Mac)  {you might have to create the Scripts/python folder}  
3.  *ReadMettlerToSheet.ods* This spreadsheet is a minimal working example containing a button that calls the macro.  Remember the macro is typically not stored in the spreadsheet.    

You may need to install the python script provider  `sudo apt-get install libreoffice-script-provider-python` to make the Python/LO connection work.  
Permissions for serial ports are not automatically granted to users on Linux-like operationg systems.  On Ubuntu, check `groups ${USER}` to see if you are in the *dialout* group.  If not, you can add yourself `sudo gpasswd --add ${USER} dialout`.  Logout and log back in to complete the change.  On Raspbian remember that the serial port needs to be activated `enable_uart=1` in the /boot/config.txt.  The equivalent for adding to dialout is `sudo usermod -a -G dialout pi`, also need logout/in cycle.  

### Thanks  
Thanks to two older links that provided guidance.  
http://christopher5106.github.io/office/2015/12/06/openoffice-libreoffice-automate-your-office-tasks-with-python-macros.html  
https://ask.libreoffice.org/t/how-can-i-call-a-python-script-from-a-basic-macro/25421  
