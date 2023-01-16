from math import cos
from math import sin
import tools

class angles:
    a=0
    b=0
    c=0

pp = True

rotatedX = [0,0,0]
rotatedY = [0,0,0]
rotatedZ = [0,0,0]

points = [
    [-1,-1,1],
    [1,-1,1],
    [1,1,1],
    [-1,1,1],
    [-1,-1,-1],
    [1,-1,-1],
    [1,1,-1],
    [-1,1,-1]
]

transformed = [0,0,0]

pi = 3.1415926535

#build and rotate cube
def build(x,y,z,size):

    pX = [0,0,0,0,0,0,0,0]
    pY = [0,0,0,0,0,0,0,0]

    #x rotation matrix
    rotateX = [
        [1,0,0],
        [0,cos(angles.a*pi/180),-sin(angles.a*pi/180)],
        [0,sin(angles.a*pi/180),cos(angles.a*pi/180)]
    ]
    #y rotation matrix
    rotateY = [
        [cos(angles.b*pi/180),0,sin(angles.b*pi/180)],
        [0,1,0],
        [-sin(angles.b*pi/180),0,cos(angles.b*pi/180)]
    ]
    #z rotation matrix
    rotateZ = [
        [cos(angles.c*pi/180),-sin(angles.c*pi/180),0],
        [sin(angles.c*pi/180),cos(angles.c*pi/180),0],
        [0,0,1]
    ]

    for i in range(8):
        
        for j in range(3):
            rotatedX[j] = points[i][0]*rotateX[j][0]+points[i][1]*rotateX[j][1]+points[i][2]*rotateX[j][2]

        for j in range(3):
            rotatedY[j] = rotatedX[0]*rotateY[j][0]+rotatedX[1]*rotateY[j][1]+rotatedX[2]*rotateY[j][2]
        
        for j in range(3):
            rotatedZ[j] = rotatedY[0]*rotateZ[j][0]+rotatedY[1]*rotateZ[j][1]+rotatedY[2]*rotateZ[j][2]

        p = 1/(2.5-rotatedZ[2])*1.5

        if pp:
            #perspective projection matrix
            projection = [
                [p,0,0],
                [0,p,0], 
                [0,0,0]
            ]
        else:
            #orthographic projection matrix
            projection = [
                [1,0,0],
                [0,1,0],
                [0,0,0]
            ]

        transformed[0] = rotatedZ[0] * projection[0][0] + rotatedZ[0] * projection[0][1] + rotatedZ[0] * projection[0][2]
        transformed[1] = rotatedZ[1] * projection[0][1] + rotatedZ[1] * projection[1][1] + rotatedZ[1] * projection[1][2]

        xpos = transformed[0]*(size)+x
        ypos = transformed[1]*((size*0.6))+y

        tools.pixel(int(xpos),int(ypos))

        pX[i] = int(xpos)
        pY[i] = int(ypos)

    tools.line(pX[3],pY[3],pX[0],pY[0])
    tools.line(pX[3],pY[3],pX[2],pY[2])
    tools.line(pX[3],pY[3],pX[7],pY[7])

    tools.line(pX[1],pY[1],pX[0],pY[0])
    tools.line(pX[1],pY[1],pX[2],pY[2])
    tools.line(pX[1],pY[1],pX[5],pY[5])

    tools.line(pX[4],pY[4],pX[0],pY[0])
    tools.line(pX[4],pY[4],pX[5],pY[5])
    tools.line(pX[4],pY[4],pX[7],pY[7])

    tools.line(pX[6],pY[6],pX[2],pY[2])
    tools.line(pX[6],pY[6],pX[5],pY[5])
    tools.line(pX[6],pY[6],pX[7],pY[7])

    #connect all
    """
    for i in range(7):
        for j in range(0,7,1):
            tools.line(pX[i],pY[i],pX[j],pY[j])
    """
def rotate(x,y,z):
    angles.a=x;angles.b=y;angles.c=z
