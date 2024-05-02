
from OpenGL.GL import *

import pygame
import math
from pygame.locals import *
from math import *
from random import *


px, py = 600, 600 


def SetPixel(x,y):
    #if pc.x > pxi && pc.x<pxf && pc.y>pyi && pc.y < pyf
    glBegin(GL_POINTS)
    glColor3fv([255/255,255/255,255/255])
    #r,g,b = random(), random(), random()
    #glColor3fv([r,g,b])
    glVertex2f(x/px,y/py)
    glEnd()  
    

def Draw8Points( x, y, a, b):
    SetPixel(x + a, y + b)
    SetPixel(x - a, y + b)
    SetPixel(x - a, y - b)
    SetPixel(x + a, y - b)
    SetPixel(x + b, y + a)
    SetPixel(x - b, y + a)
    SetPixel(x - b, y - a)
    SetPixel(x + b, y - a)

def CircleBresenham( x, y, R):
    x1,y1,d= 0,R,1 - R
    Draw8Points(x, y, x1, y1)
    while (x1 < y1):
        if (d < 0):
            d += 2 * x1 + 2
        else:
            d += 2 * (x1 - y1) + 5
            y1 -= 1
        x1 += 1
        Draw8Points(x, y, x1, y1)

def line_opt_prim( x0, y0, x1, y1):
    steep = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    
    dx = x1 - x0
    dy = y1 - y0
    derror = abs(dy / float(dx))
    error = 0
    y = y0
    #for (x = x0 x <= x1; x++)
    for x in range(x0, x1 + 1): #posible error
        if (steep):
            SetPixel(y, x)
    
        else:
            SetPixel(x, y)
        error += derror
        if (error > .5):
            y += 1 if y1 > y0 else -1
            error -= 1.0


def linea(p1, p2):
    line_opt_prim(p1.x, p1.y, p2.x, p2.y)

class Punto:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y) 

    def __add__(self, obj):
        return Punto(self.x + obj.x, self.y + obj.y)

    def __iadd__(self, obj):
        self.x += obj.x
        self.y += obj.y
        return Punto(self.x, self.y)

    def __isub__(self, obj):
        self.x -= obj.x
        self.y -= obj.y
        return Punto(self.x, self.y)

    def __sub__(self, obj):
        return Punto(self.x - obj.x, self.y - obj.y)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __ne__(self, p):
        return not self.__eq__(p)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

class Triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class Reg:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

class Hexagono():
    def __init__(self, _x, _y, c):
        self.x = int(_x)
        self.y = int(_y)
        self.c = c
        self.a, self.b = c/2, c/2*sqrt(3)
        self.pc = Punto(self.x, self.y) #                              pt1                     , pt2                                          , pt3                            , pt4                  , pt5                                , pt6                                 
        self.pt1, self.pt2, self.pt3, self.pt4, self.pt5, self.pt6 = Punto(self.x, self.y + c), Punto(self.x + self.b, self.y + self.a), Punto(self.x+self.b, self.y-self.a), Punto(self.x,self.y-c), Punto(self.x-self.b, self.y-self.a), Punto(self.x-self.b, self.y +self.a),                                               
        self.paux = self.pt1 
        #                                                                   region1                                region2                                  region3                                region4                                  region5                                  region6                     
        self.reg1, self.reg2, self.reg3, self.reg4, self.reg5, self.reg6 = Triangulo(self.pt1, self.pt2, self.pc), Triangulo(self.pt2, self.pt3, self.pc), Triangulo(self.pt3, self.pt4, self.pc), Triangulo(self.pt4, self.pt5, self.pc), Triangulo(self.pt5, self.pt6, self.pc), Triangulo(self.pt6, self.pt1, self.pc) 
        
    def regiones(self):
        equilatero(self.reg1)
        equilatero(self.reg2)
        equilatero(self.reg3)
        equilatero(self.reg4)
        equilatero(self.reg5)
        equilatero(self.reg6)

        #if self.paux.x == self.pt1.x and self.paux.y == self.pt1.y:
        #    self.pt1 = self.rotacion2d(self.pt1,)
        #self.pt2 = self.rotacion2d(self.pt2)
        #self.pt3 = self.rotacion2d(self.pt3)
        #self.pt4 = self.rotacion2d(self.pt4)
        #self.pt5 = self.rotacion2d(self.pt5)
        #self.pt6 = self.rotacion2d(self.pt6)

        self.reg1= Triangulo(self.pt1, self.pt2, self.pc)#, Triangulo(self.pt2, self.pt3, self.pc), Triangulo(self.pt3, self.pt4, self.pc), Triangulo(self.pt4, self.pt5, self.pc), Triangulo(self.pt5, self.pt6, self.pc), Triangulo(self.pt6, self.pt1, self.pc) 


        equilatero(self.reg1)
        equilatero(self.reg2)
        equilatero(self.reg3)
        equilatero(self.reg4)
        equilatero(self.reg5)
        equilatero(self.reg6)


    def recur_tri(self, reg):
        reg.pt1 = self.rotacion2d(reg.pt1)




    def dibu_pts(self):
        self.pt1 
        linea()
        
    

    def dibujar(self):
        self.regiones()

    def rotacion2d(self, pnt, angle):
        # Definir el ángulo de rotación en grados
        theta = angle
        # Convertir el ángulo de grados a radianes
        theta = math.radians(theta)
        # Calcular las coordenadas del punto rotado
        x_rot = pnt.x * math.cos(theta) - pnt.y * math.sin(theta)
        y_rot = pnt.x * math.sin(theta) + pnt.y * math.cos(theta)
        p_rotado = Punto(x_rot, y_rot)
        return p_rotado
        
#pxi , pyi, pxf, pyf = 0, 0, 0, 0


def equilatero(reg):
    linea(reg.p1,reg.p2)
    linea(reg.p2,reg.p3)
    linea(reg.p3,reg.p1)   

def triangulo(pt1,pt2,pt3):
    linea(pt1,pt2)
    linea(pt2,pt3)
    linea(pt3,pt1)

def circle(ct,r):
    CircleBresenham(ct.x,ct.y,r)
    #line_opt_prim(200,200,250,250)

def pruebas():
    px,py,c = 200,200,200
    a = c / sqrt(3)
    m = c / (sqrt(3) * 2)
    p1, p2, p3 = Punto(px, py - a), Punto(px + (c / 2), py + m), Punto(px - (c / 2), py + m)
    #print(p1.x, p1.y, p2.x, p2.y , p3.x, p3.y)
    #triangulo(p1,p2,p3)
    #linea(p1, p2)
    #linea(p2, p3)
    #linea(p3, p1)

    #pt1, pt2, pt3 = Punto(200,84.5),Punto(300,257.7),Punto(100.0,257.7)
    #triangulo(pt1, pt2, pt3)





def Puntos():
    glBegin(GL_POINTS)
    for _ in range(px):
        x=randrange(-px,py)/px
        y=randrange(-px,py)/px
        r,g,b = random(),random(),random()
        glColor3fv([r,g,b])
        glVertex2f(x,y)
    glEnd()

def Parabola():
    glBegin(GL_POINTS)
    glColor3fv([0,1,0])
    x=-1
    x1=-1
    x2=-1
    for _ in range (px):
        y = x**2
        y1 = x1**2 + 0.1
        y2 = x2**2 + 0.2
        c1=[1,0,0]
        c2=[0,1,0]
        c3=[0,0,1]
        
        glVertex2f(x,y)
        glVertex2f(x,-y)
        glColor3fv(c1)
        glVertex2f(x1,y1)
        glVertex2f(x1,-y1)
        glColor3fv(c2)
        glVertex2f(x2,-y2)
        glColor3fv(c3)

        x += 1/300
        x1 += 1/300
        x2 += 1/300
    glEnd() 

 

def main():
    pantalla = [px,py]
    Cerrar = False
    hx = Hexagono(0,0,500)
    pygame.init()
    pygame.display.set_mode(pantalla,DOUBLEBUF|OPENGL)
    pygame.display.set_caption("primitivas")
    glClearColor(0, 0, 0, 1) # Establece el color de fondo a blanco
    while not Cerrar:
        for event in pygame.event.get():
            if event.type == QUIT:
                Cerrar = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Cerrar = True
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #Parabola()
        #Puntos()
        #linea()
        #circle()
        pruebas()
        hx.dibujar()

        pygame.display.flip()
        pygame.time.wait(60)

    pygame.quit()

main()