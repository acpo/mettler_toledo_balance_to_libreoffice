# Parameters for the Mettler Toledo XS105 scale:
# 9600
# 8/No
# 1 stopbit
# Xon/Xoff
# <CR><LF>
# Ansi/win
# Off

import serial
import time
import re
#import xlwings as xw  #not needed for LibreOffice

##def read_weight(socket, timelapse=1):
##    """
##    Returns the weight in gram and the stability.
##
##    :param socket: serial socket
##    :param timelapse: timelapse between each measurement
##    :returns: tuple (weight, stability)
##    """
##    ser.write(b'\nSI\n')
##    time.sleep(1)
##    #TODO check inWaiting length
##    value = ser.read(ser.inWaiting())
##    value = value.decode('utf-8')
##    value = value.split('\n')[1][:-1]
##    if value[3] == 'S':
##        stability = True
##    else:
##        stability = False
##    weight = value[4:-1].strip(' ')
##    return (weight, stability)
##

def get_mass():

#    ser = serial.Serial(port='COM1',
    ser = serial.Serial(port='/dev/ttyS0',
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS
    )

    if not ser.isOpen():
        ser.open()
    
    ser.write(b'\nSI\n')
    time.sleep(1)
    #TODO check inWaiting length
    value = ser.read(ser.inWaiting())
    value = value.decode('utf-8')
    value = value.split('\n')[1][:-1]

    if value[3] == 'S':
        stability = True
    else:
        stability = False
    weight = value[4:-1].strip(' ')
    print(weight)

    #weight, stability = read_weight(ser)
    #wb = xw.Book.caller() #xlwings not needed with LibreOffice
    #wb.app.selection.value = weight #xlwings not needed with LibreOffice
    #print('M = ' + str(weight) + ' g')

    if ser.isOpen():
        ser.close()
        
    return(weight)
g_exportedScripts = (get_mass,)

