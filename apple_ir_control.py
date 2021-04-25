from piir.io import receive
from piir.decode import decode
import subprocess,piir,sys

# GPIO of IR receiver
pinr = 24

# GPIO of IR sender
pins = 22

# IR codes defined
remoteMD = piir.Remote('/home/pi/minidisc.json', pins)
remoteTAPE = piir.Remote('/home/pi/tape.json', pins)
remoteCD = piir.Remote('/home/pi/cd.json', pins)

# number of times to send IR code
mdsend = 2
tapesend = 2
cdsend = 2

# enable or disable optional IR control
enMD = 1
enCD = 0
enTape = 0

# unique IR value of buttons on apple remote
# captured using test mode of this script
ok = r"xee\x87\\\xab"
menu = r"xee\x87\x03\xab"
down = r"xee\x87\x0c\xab"
up = r"xee\x87\n\xab"
left = r"xee\x87\t\xab"
right = r"xee\x87\x06\xab"
play = r"xee\x87_\xab"

# if 'test' is entered as argument then only show remote button press codes
# ex: python3 apple_ir_control.py test
if (len(sys.argv) - 1):
     if sys.argv[1] == 'test':
         while True:
             print(decode(receive(pinr)))

while True:
    data = str(decode(receive(pinr)))
    if ok in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["amixer", "-c", "2", "cset", "numid=3", "104"])
        else:
            if enMD: remoteMD.send('PAUSE', mdsend)
            if enTape: remoteTAPE.send('PAUSE', tapesend)
            if enCD: remoteCD.send('PAUSE', cdsend)
    elif menu in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["sudo", "/home/pi/hub-ctrl", "-h", "1", "-P", "2", "-p", "0"])
            subprocess.call(["mpc", "stop", "-q"])
        else:
            if enMD: remoteMD.send('STOP', mdsend)
            if enTape: remoteTAPE.send('STOP', tapesend)
            if enCD: remoteCD.send('STOP', cdsend)
    elif down in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["/home/pi/volume-down.sh"])
        else:
            if enMD: remoteMD.send('SCROLL', mdsend)
    elif up in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["/home/pi/volume-up.sh"])
        else:
            if enMD: remoteMD.send('DISPLAY', mdsend)
    elif left in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["mpc", "prev", "-q"])
        else:
            if enMD: remoteMD.send('PREV', mdsend)
            if enTape: remoteTAPE.send('PREV', tapesend)
            if enCD: remoteCD.send('PREV', cdsend)
    elif right in data:
        if subprocess.call(["/home/pi/volume-mpc.sh"]):
            subprocess.call(["mpc", "next", "-q"])
        else:
            if enMD: remoteMD.send('NEXT', mdsend)
            if enTape: remoteTAPE.send('NEXT', tapesend)
            if enCD: remoteCD.send('NEXT', cdsend)
    elif play in data:
        subprocess.call(["/home/pi/volume-play.sh"])
