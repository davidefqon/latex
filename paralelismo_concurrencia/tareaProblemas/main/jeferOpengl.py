
from OpenGL.GL import *

import math
import pygame
from pygame.locals import *
from math import *
from random import *

px, py = 800, 800 
Elev, Giro = 0 ,0 

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
    vdx = dx
    if vdx == 0: 
        dx = 0.000001
    derror = abs(dy / float(dx))
    error = 0
    y = y0
    #for (x = x0 x <= x1; x++)
    for x in range(x0, x1 + 1): #posible error
        if steep:
            SetPixel(y, x)
    
        else:
            SetPixel(x, y)
        error += derror
        if (error > .5):
            y += 1 if y1 > y0 else -1
            error -= 1.0

def draw_line(x0, y0, x1, y1):
    # Calcula las diferencias entre las coordenadas finales e iniciales
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Determina la dirección del trazo y ajusta los puntos si es necesario
    steep = dy > dx
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    # Intercambia los puntos finales si es necesario
    swapped = False
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
        swapped = True

    # Recalcula las diferencias después del ajuste
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Calcula el incremento y el desplazamiento inicial
    if dy == 0:
        slope = 0  # Evita la división por cero
    else:
        slope = dy / dx
    error = 0.0
    y = y0
    ystep = 1 if y0 < y1 else -1

    # Dibuja los píxeles a lo largo de la línea
    for x in range(x0, x1 + 1):
        if steep:
            SetPixel(y, x)  # Dibuja un punto intercambiando las coordenadas
        else:
            SetPixel(x, y)
        error += slope
        if error >= 0.5:
            y += ystep
            error -= 1.0

    # Si los puntos se intercambiaron inicialmente, restablece el orden de los puntos
    if swapped:
        return (x1, y1), (x0, y0)
    else:
        return (x0, y0), (x1, y1)

def linea(p1, p2):
    #line_opt_prim((p1.x), (p1.y), (p2.x), (p2.y))
    draw_line(int(p1.x), int(p1.y), int(p2.x), int(p2.y))

class Punto:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)  
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

class Punto3d():
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def a2d(self):
        p = Punto(0,0)
        
        p.x = self.x*math.cos(Giro) - self.z*math.sin(Giro)
        p.y = -self.x*math.sin(Giro)*math.sin(Elev) + self.y*math.cos(Elev) - self.z*math.cos(Giro)*math.sin(Elev)
        return p


class Cubo():
    def __init__(self,px, py, a):
        self.xi = 0
        self.yi = 0
        self.zi = 0

        self.p1 = Punto3d(-a,a,-a)
        self.p2 = Punto3d(-a,a,a)
        self.p3 = Punto3d(a,a,a)
        self.p4 = Punto3d(a,a,-a)
        self.p5 = Punto3d(-a,-a,-a)
        self.p6 = Punto3d(-a,-a,a)
        self.p7 = Punto3d(a,-a,a)
        self.p8 = Punto3d(a,-a,-a)

        

    def mostrar(self):
        #print(self.p1p)
        self.p1p = self.p1.a2d()
        self.p2p = self.p2.a2d()
        self.p3p = self.p3.a2d()
        self.p4p = self.p4.a2d()
        self.p5p = self.p5.a2d()
        self.p6p = self.p6.a2d()
        self.p7p = self.p7.a2d()
        self.p8p = self.p8.a2d()

        linea(self.p1p, self.p2p)
        linea(self.p2p, self.p3p)
        linea(self.p3p, self.p4p)
        linea(self.p4p, self.p1p)
        
        linea(self.p5p, self.p6p)
        linea(self.p6p, self.p7p)
        linea(self.p7p, self.p8p)
        linea(self.p8p, self.p5p)
        
        linea(self.p1p, self.p5p)
        linea(self.p2p, self.p6p)
        linea(self.p3p, self.p7p)
        linea(self.p4p, self.p8p)


class Seno():
    def __init__(self):
        self.s = 0

    def fun(self,x):
        ret = 90 * math.sin(x)  
        return ret
    
    def dibujarfun(self):
        for i in range (-500,500,1):
            SetPixel(i, self.fun(i * 3.14/180))

class CopoNieve:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def triangulo(self, x, y):
        8

def main():
    global Giro, Elev
    pantalla = [px,py]
    Cerrar = False
    activador= False
    cubo = Cubo(100,100,100) 
    seno = Seno()
    pygame.init()
    pygame.display.set_mode(pantalla,DOUBLEBUF|OPENGL)
    pygame.display.set_caption("primitivas")
    glClearColor(0, 0, 0, 1) # Establece el color de fondo a blanco
    while not Cerrar:
        for event in pygame.event.get():
            if event.type == QUIT:
                Cerrar = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Cerrar = True

            elif event.type == MOUSEBUTTONDOWN:
                activador = True
            elif event.type == MOUSEMOTION:
                # Captura las coordenadas del mouse
                if activador:
                    mouse_x, mouse_y = event.pos
                    #print("Coordenadas del mouse:", mouse_x, mouse_y)
                    Elev = mouse_y * 0.01745
                    Giro = mouse_x * 0.01745
            elif event.type == MOUSEBUTTONUP:
                # Captura el evento de levantar el mouse
                activador = False
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #hx.dibujar()
        #cubo.mostrar()
        seno.dibujarfun()
        #line_opt_prim(100,0,-100,0)
        pygame.display.flip()
        pygame.time.wait(60)

    pygame.quit()

main()