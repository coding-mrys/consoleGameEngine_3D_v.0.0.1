import time
from cge import*
import tools
from math import sin,cos

a = 0;b=0;c=0
x=30;y=30

pi = 3.1415926535

k=0

build_display(550,150)
color("f")

def update():
    show()
    clear()

while running:
    #exit
    if keyboard.is_pressed("q"):
        running = False
    if keyboard.is_pressed("d"):
        x+=2
    if keyboard.is_pressed("a"):
        x-=2
    if keyboard.is_pressed("w"):
        y-=2
    if keyboard.is_pressed("s") :
        y+=2

    if keyboard.is_pressed("1"):
        a+=2
    if keyboard.is_pressed("2"):
        b+=2
    if keyboard.is_pressed("3"):
        c+=2

    x = int(300+cos(a*pi/180)*40)
    y = int(60+sin(a*pi/180)*40*0.6)
    
    cube.build(x,y,0,30)
    cube.rotate(a,b,c)

    a+=2.5
    b+=2.5
    c+=2.5

    tools.circle(100,50,40)
    for i in range(45):
        tools.line(100,50,int(100+cos((a+i)*pi/180)*40),int(50+sin((a+i)*pi/180)*40*0.6))
    
    k+=1
    if k > 300:
        k=0

    tools.rect(40+k,60+int(sin((0.8*a)*pi/180)*50),40,30)

    if keyboard.is_pressed("o"):
        cube.pp = False
    elif keyboard.is_pressed("p"):
        cube.pp = True

    #update
    update()

clear()