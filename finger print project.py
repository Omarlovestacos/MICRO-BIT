from microbit import *
 #the idea of this project is showcasing the idea of your phones fingerprint scanner
 #this is tested on a microbit v2
 #name=omar hijazi
while True:
    if pin_logo.is_touched():
        display.scroll('finger print detected')
