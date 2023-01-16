import os
import keyboard
import time
import random
import display
import cube
import tools

#global variables
row = []
running = True

#build display
def build_display(width,height):
    display = open("display.py","w")
    display.write("screen = [\n")
 
    for i in range(width):
        row.append(" ")
    
    for j in range(height):
        display.write(str(row))
        display.write(",\n")
    display.write("]")

#show display
def show():
    for k in range(len(display.screen)):
        line=""
        for l in range(len(display.screen[k])):
            line+=display.screen[k][l]
        print(line)


#update screen
def clear():
    for i in range(len(display.screen)):
        for j in range(len(display.screen[i])):
            display.screen[i][j] = " "

    os.system("cls")

#change color
def color(value):
    os.system("color " + value)

 