import tkinter
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
## hardware defination
bled = LED(5)
rled = LED(6)
yled = LED(26)

##GUI definations
win= tkinter.Tk()
win.title("Led Toggler")
myFont= tkinter.font.Font(family = 'Helvatica', size = 12, weight = "bold")

##Event functions
def bchangetxt():
    rledButton["text"] = "Switch on red LED"
    yledButton["text"] = "Switch on yellow LED"

def rchangetxt():
    bledButton["text"] = "Switch on blue LED"
    yledButton["text"] = "Switch on yellow LED"
    
def ychangetxt():
    bledButton["text"] = "Switch on blue LED"
    rledButton["text"] = "Switch on red LED"


def bledToggler():
    if bled.is_lit:
        bled.off()
        bledButton["text"] = "Switch on blue LED"
    else:
        bled.on()
        bchangetxt()
        clean(rled, yled)
        bledButton["text"] = "Switch off blue LED"
        
        
def rledToggler():
    if rled.is_lit:
        rled.off()
        rledButton["text"] = "Switch on red LED"
    else:
        rled.on()
        clean(bled, yled)
        rledButton["text"] = "Switch off red LED"
        rchangetxt()
        
def yledToggler():
    if yled.is_lit:
        yled.off()
        yledButton["text"] = "Switch on yellow LED"
    else:
        yled.on()
        clean(rled, bled)
        yledButton["text"] = "Switch off yellow LED"
        ychangetxt()

def close():
    rled.off()
    bled.off()
    yled.off()
    #RPi.GPIO.cleanup()
    win.destroy()
    

def clean(led1, led2):
    led1.off()
    led2.off()

## Defination of Widgets
##        
bledButton = tkinter.Button(win, text = 'Switch on blue LED', font = myFont, command = bledToggler, bg = 'blue', height= 1, width = 24)
bledButton.grid(row=0, column = 1)

rledButton = tkinter.Button(win, text = 'Switch on red LED', font = myFont, command = rledToggler, bg = 'red', height= 1, width = 24)
rledButton.grid(row=1, column = 1)

yledButton = tkinter.Button(win, text = 'Switch on yellow LED', font = myFont, command = yledToggler, bg = 'yellow', height= 1, width = 24)
yledButton.grid(row=2, column = 1)

exitButton = tkinter.Button(win, text = 'Exit', font = myFont, command = close, bg = 'white', height= 1, width = 24)
exitButton.grid(row=3, column = 1)

win.protocol("WM_DELETE_WINDOW",close)



