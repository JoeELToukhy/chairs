from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
def draw_chair():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(2,0.5,2)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(2,3,0.5)
    glTranslate(0,1.2,-3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(0.5,3,0.5)
    glTranslate(3,-1.2,3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(0.5,3,0.5)
    glTranslate(3,-1.2,-3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(0.5,3,0.5)
    glTranslate(-3,-1.2,3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glScale(0.5,3,0.5)
    glTranslate(-3,-1.2,-3)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()


    glPopAttrib()
    glPopMatrix()

def draw():
    glMatrixMode(GL_MODELVIEW)

    glColor(1, 0, 0)
    glTranslate(-5, 0, 0)
    draw_chair()

    glColor(0,0,1)
    glTranslate(8,0,0)
    draw_chair()



    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize(500,500)
glutCreateWindow(b"section")
glutDisplayFunc(draw)

myinit()
glutMainLoop()

