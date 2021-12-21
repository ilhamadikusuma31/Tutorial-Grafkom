import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
print("Imports successful!")

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import*
w,h= 500,500

# glTranslated
# glScaled
# glRotate

x = 0

def square():
    global x
    x -= 0.1
    # glTranslated(x,0,0)
    # glScaled(x,3,0)
    # glRotatef(x,1,1,0)
    glColor3f(0,1,0) #RGB
    glBegin(GL_QUADS)
    glVertex2f(100+x, 100)
    glVertex2f(200+x, 100)
    glVertex2f(200+x, 200)
    glVertex2f(100+x, 200)
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
    square()
   
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

