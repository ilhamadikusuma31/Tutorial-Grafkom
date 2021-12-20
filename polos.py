import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Imports successful!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import*
w,h= 500,500


def Circle_polygon(x_pos, y_pos, radius, sides):    
    glBegin(GL_POLYGON)    
    for i in range(100):#perhitungan sin dan cos dari sudut lingkaran 
        cosine= radius * cos(i*2*pi/sides) + x_pos  
        sine  = radius * sin(i*2*pi/sides) + y_pos   
        glVertex2f(cosine,sine)
    glEnd()

def lingkaran():
    Circle_polygon(50,100, 8, 100)

def segiBanyak():
    glBegin(GL_POLYGON)
    glVertex2f(10,10)
    glVertex2f(10,90)
    glVertex2f(3,-10)
    glVertex2f(133,20)
    glVertex2f(123,23)

    glEnd()

def titik():
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()

def garis():
    glColor3f(0.216,0.722,0.267) #RGB
    glBegin(GL_LINES)
    glVertex2f(10,10)
    glVertex2f(10,90)
    glEnd()


def square():
    glColor3f(0,1,0) #RGB
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # square()
    # titik()
    # garis()
    # segiBanyak()
    lingkaran()
    glutSwapBuffers()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Latihan opengl")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()

main()





# def Circle_polygon(x_pos, y_pos, radius, sides):    
#     glBegin(GL_POLYGON)    
#     for i in range(100):#perhitungan sin dan cos dari sudut lingkaran 
#         cosine= radius * cos(i*2*pi/sides) + x_pos  
#         sine  = radius * sin(i*2*pi/sides) + y_pos   
#         glVertex2f(cosine,sine)
#     glEnd()