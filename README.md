# mettler_toledo_balance_to_libreoffice
Python and LibreOffice scripts to read a Mettler Toledo balance into a spreadsheet

## in progress
The goal is to read balance data into a spreadsheet.  The other repository uses Excel and depends on xlWings.  This version uses LibreOffice so that it is open-source and suitable for more than just Windows.  Development was on Ubuntu.
## Files
LOscript.txt needs to get entered as a Standard script in the LO Calc Macro Editor.  The line that calls the Python script calls by file name and by the name of the *def*.  
Currently only a dummy script is in place.  Any Python script for reading a Mettler Balance will work as long as you end with `return` of the variable holding the mass and include the final line `g_exportedScripts = (Dummy,)`  where Dummy is the name of *def*.  

