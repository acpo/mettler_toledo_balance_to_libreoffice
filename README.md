# mettler_toledo_balance_to_libreoffice
Python and LibreOffice scripts to read a Mettler Toledo balance into a spreadsheet

## in progress
The goal is to read balance data into a spreadsheet.  The other repository uses Excel and depends on xlWings.  This version uses LibreOffice so that it is open-source and suitable for more than just Windows.  Development was on Ubuntu.  
The choice to mix LO Basic and Python is driven by easy already solved communication with the balance in Python via PySerial.  However the Python interaction with LO Calc files is difficult if you want to put data in the currently active cell and then increment the position.  The LO Basic commands were much easier.  The only challenge is to make LO call Python and return data.  
## Files
LOscript.txt needs to get entered as a Standard script in the LO Calc Macro Editor.  The line that calls the Python script calls by file name and by the name of the *def*.  
Currently only a dummy script is in place.  Any Python script for reading a Mettler Balance will work as long as you end with `return` of the variable holding the mass and include the final line `g_exportedScripts = (Dummy,)`  where Dummy is the name of *def*.  
Python script needs to be in ~/.config/libreoffice/4/user/Scripts/python (Linux) %APPDATA%\LibreOffice\4\user\Scripts\python (Windows) or $HOME/.config/libreoffice/4/user/Scripts/python (Mac)  {you might have to create the Scripts/python folder}  
You may need to install the python script provider  `sudo apt-get install libreoffice-script-provider-python`  
Permissions for serial ports are not automatically granted to users.  On Ubuntu, check `groups ${USER}` to see if you are in the *dialout* group.  If not, you can add yourself `sudo gpasswd --add ${USER} dialout`.  Logout and log back in to complete the change.  On Raspbian remember that the serial port needs to be activated `enable_uart=1` in the /boot/config.txt.  The equivalent for adding to dialout is `sudo usermod -a -G dialout pi`, also need logout/in cycle.  

### Thanks  
Thanks to two older links that provided guidance.  
http://christopher5106.github.io/office/2015/12/06/openoffice-libreoffice-automate-your-office-tasks-with-python-macros.html  
https://ask.libreoffice.org/t/how-can-i-call-a-python-script-from-a-basic-macro/25421  
