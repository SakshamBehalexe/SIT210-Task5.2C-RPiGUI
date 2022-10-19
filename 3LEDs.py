import tkinter
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
## hardware defination
bled = LED(5)
rled = LED(6)
yled = LED(26)

#radio = IntVar()
##GUI definations
win= tkinter.Tk()
win.title("Led Toggler")
myFont= tkinter.font.Font(family = 'Helvatica', size = 12, weight = "bold")

##Event functions
def bchangetxt():
    rledRadiobutton["text"] = "Switch on red LED"
    yledRadiobutton["text"] = "Switch on yellow LED"

def rchangetxt():
    bledRadiobutton["text"] = "Switch on blue LED"
    yledRadiobutton["text"] = "Switch on yellow LED"
    
def ychangetxt():
    bledRadiobutton["text"] = "Switch on blue LED"
    rledRadiobutton["text"] = "Switch on red LED"


def bledToggler():
    if bled.is_lit:
        bled.off()
        bledRadiobutton["text"] = "Switch on blue LED"        
    else:
        bled.on()
        bchangetxt()
        clean(rled, yled)
        bledRadiobutton["text"] = "Switch off blue LED"
        
        
def rledToggler():
    if rled.is_lit:
        rled.off()
        rledRadiobutton["text"] = "Switch on red LED"
    else:
        rled.on()
        clean(bled, yled)
        rledRadiobutton["text"] = "Switch off red LED"
        rchangetxt()
        
def yledToggler():
    if yled.is_lit:
        yled.off()
        yledRadiobutton["text"] = "Switch on yellow LED"
    else:
        yled.on()
        clean(rled, bled)
        yledRadiobutton["text"] = "Switch off yellow LED"
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
bledRadiobutton = tkinter.Radiobutton(win, text = 'Switch on blue LED', font = myFont, command = bledToggler, bg = 'blue', height= 1, width = 24, value =1)
bledRadiobutton.grid(row=0, column = 1)

rledRadiobutton = tkinter.Radiobutton(win, text = 'Switch on red LED', font = myFont, command = rledToggler, bg = 'red', height= 1, width = 24, value = 2)
rledRadiobutton.grid(row=1, column = 1)

yledRadiobutton = tkinter.Radiobutton(win, text = 'Switch on yellow LED', font = myFont, command = yledToggler, bg = 'yellow', height= 1, width = 24, value = 3)
yledRadiobutton.grid(row=2, column = 1)

exitRadiobutton = tkinter.Radiobutton(win, text = 'Exit',font = myFont, command = close, bg = 'white', height= 1, width = 24, value = 4)
exitRadiobutton.grid(row=3, column = 1)

win.protocol("WM_DELETE_WINDOW",close)
