
# AwalPROGRAM
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

display = (600,900)			#ukuran layar di Viewpor 600X450
keys = {
    "img01": False, 	#tombol "l"
    "img02": False,
    "img03": False,		#tombol "s"
	"depan_lemari": False, 	#tombol ke atas
	"belakang_lemari": False,		#tombol ke bawah
	"kanan": False,		#tombol ke kanan
	"kiri": False,		#tombol ke kiri
	"belakang": False,		#tombol ke belakang
	"depan": False,		#tombol ke depan
}

def inisialisasi():
    glViewport(0,0,display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(30, (display[0]/display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

#KOORDINAT titik-titik yang dipakai dengan dilihat dari luar arah 
#berlawanan arah dengan jarum jam
#glVertex3f( 1,  1,  1) #0
#glVertex3f( 1,  1, -1) #1
#glVertex3f( 1, -1, -1) #2
#glVertex3f( 1, -1,  1) #3
#glVertex3f(-1,  1,  1) #4
#glVertex3f(-1, -1, -1) #5
#glVertex3f(-1, -1,  1) #6
#glVertex3f(-1,  1, -1) #7


#LANTAI
def lantai():
	#BAWAH
	glColor3f(0, 0.6, 0)
	glBegin(GL_QUADS)
	glVertex3f(-3, 0,  -3) #bawah kiri
	glVertex3f( 3, 0,  -3) #bawah kanan
	glVertex3f( 3,  0,  3) #atas kanan
	glVertex3f(-3,  0,  3) #atas kiri
	glEnd()

def pegangan():
	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-2.4, 0.9, -2) #6
	glVertex3f( -2.5, 0.9,  -2) #3
	glVertex3f( -2.5,  1.1,  -2) #0
	glVertex3f(-2.4,  1.1,  -2) #4
	glEnd()

	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-2.1, 0.9, -2) #6
	glVertex3f( -2, 0.9,  -2) #3
	glVertex3f( -2,  1.1,  -2) #0
	glVertex3f(-2.1,  1.1,  -2) #4
	glEnd()	

	glFlush()	

def lemari():
	glColor3f(0.6, 0.1, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-3, 0, -2) #6
	glVertex3f( -1.5, 0,  -2) #3
	glVertex3f( -1.5,  2,  -2) #0
	glVertex3f(-3,  2,  -2) #4
	glEnd()

	glColor3f(0.7, 0.3, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-3, 2, -3) #6
	glVertex3f( -1.5, 2,  -3) #3
	glVertex3f( -1.5,  2,  -2) #0
	glVertex3f(-3,  2,  -2) #4
	glEnd()	

	glColor3f(0.7, 0.3, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-3, 0, -3) #6
	glVertex3f( -1.5, 0,  -3) #3
	glVertex3f( -1.5,  2,  -3) #0
	glVertex3f(-3,  2,  -3) #4
	glEnd()

	glColor3f(0.7, 0.3, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-3, 0, -3) #6
	glVertex3f( -3, 0,  -2) #3
	glVertex3f( -3,  2,  -2) #0
	glVertex3f(-3,  2,  -3) #4
	glEnd()

	glColor3f(0.7, 0.3, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-1.5, 0, -3) #6
	glVertex3f( -1.5, 0,  -2) #3
	glVertex3f( -1.5,  2,  -2) #0
	glVertex3f(-1.5,  2,  -3) #4
	glEnd()	

	glFlush()

def lemariKawat():
	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-3, 0, -2) #6
	glVertex3f( -1.5, 0,  -2) #3
	glVertex3f( -1.5,  2,  -2) #0
	glVertex3f(-3,  2,  -2) #4
	glEnd()

	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-3, 0, -2) #6
	glVertex3f( -2.25, 0,  -2) #3
	glVertex3f( -2.25,  2,  -2) #0
	glVertex3f(-3,  2,  -2) #4
	glEnd()

	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-3, 0, -3) #6
	glVertex3f( -3, 0,  -2) #3
	glVertex3f( -3,  2,  -2) #0
	glVertex3f(-3,  2,  -3) #4
	glEnd()

	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-1.5, 0, -3) #6
	glVertex3f( -1.5, 0,  -2) #3
	glVertex3f( -1.5,  2,  -2) #0
	glVertex3f(-1.5,  2,  -3) #4
	glEnd()	

	glFlush()	
	

#TEKSTUR MEJA
def img1():
    textureSurface = pygame.image.load('c:/Users/MelvinSimahan/Desktop/grafkom/bawah.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def img2():
    textureSurface = pygame.image.load('c:/Users/MelvinSimahan/Desktop/grafkom/atas.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def img3():
    textureSurface = pygame.image.load('c:/Users/MelvinSimahan/Desktop/grafkom/kiri.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid	


#MEJA
def gambarKubusKawat():
	glColor3f(0,0,0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f( 2.1, 0.8,  1) #3
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f(-1,  1,  1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0,0,0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(-1, 0.8,  -0.7) #6
	glVertex3f( 2.1, 0.8,  -0.7) #3
	glVertex3f( 2.1,  1,  -0.7) #0
	glVertex3f(-1,  1,  -0.7) #4
	glEnd()
	
	# KIRI
	glColor3f(0,0,0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f(-1,  1,  1) #4
	glVertex3f(-1,  1, -0.7) #7
	glVertex3f(-1, 0.8, -0.7) #5
	glEnd();
	
	# KANAN
	glColor3f(0,0,0)
	glBegin(GL_LINE_LOOP)
	glVertex3f( 2.1, 0.8, -0.7) #2
	glVertex3f( 2.1,  1, -0.7) #1
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f( 2.1, 0.8,  1) #3
	glEnd()

	glColor3f(0,0,0)   
	glBegin(GL_LINE_LOOP)
	glVertex3f(-1,  1,  1) #4
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f( 2.1,  1, -0.7) #1
	glVertex3f(-1,  1, -0.7) #7
	glEnd()
    
	glFlush ()


def kaki1():
	glColor3f(0, 0, 0) #warna garis adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-0.5, 0,  1) #bawah kiri
	glVertex3f( -0.2, 0,  1) #bawah kanan
	glVertex3f( -0.2,  0.8,  1) #atas kanan
	glVertex3f(-0.5,  0.8,  1) #atas kiri
	glEnd()
	
	# KANAN
	glBegin(GL_LINE_LOOP)
	glVertex3f( -0.2, 0.8, 0.7) #2
	glVertex3f( -0.2,  0, 0.7) #1
	glVertex3f( -0.2,  0,  1) #0
	glVertex3f( -0.2, 0.8,  1) #3
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f( -0.5, 0.8, 0.7) #2
	glVertex3f( -0.5,  0, 0.7) #1
	glVertex3f( -0.5,  0,  1) #0
	glVertex3f( -0.5, 0.8,  1) #3
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f(-0.5, 0,  0.7) #bawah kiri
	glVertex3f( -0.2, 0,  0.7) #bawah kanan
	glVertex3f( -0.2,  0.8,  0.7) #atas kanan
	glVertex3f(-0.5,  0.8,  0.7) #atas kiri
	glEnd()
	
	glFlush ()

def kubuskaki1():
	glColor3f(1, 1, 1) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-0.5, 0,  1) #bawah kiri
	glVertex3f( -0.2, 0,  1) #bawah kanan
	glVertex3f( -0.2,  0.8,  1) #atas kanan
	glVertex3f(-0.5,  0.8,  1) #atas kiri
	glEnd()
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( -0.2, 0.8, 0.7) #2
	glVertex3f( -0.2,  0, 0.7) #1
	glVertex3f( -0.2,  0,  1) #0
	glVertex3f( -0.2, 0.8,  1) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( -0.5, 0.8, 0.7) #2
	glVertex3f( -0.5,  0, 0.7) #1
	glVertex3f( -0.5,  0,  1) #0
	glVertex3f( -0.5, 0.8,  1) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-0.5, 0,  0.7) #bawah kiri
	glVertex3f( -0.2, 0,  0.7) #bawah kanan
	glVertex3f( -0.2,  0.8,  0.7) #atas kanan
	glVertex3f(-0.5,  0.8,  0.7) #atas kiri
	glEnd()
	
	glFlush ()

def kubuskaki2():
	glColor3f(1, 1, 1) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(1.6, 0,  1) #bawah kiri
	glVertex3f( 1.3, 0,  1) #bawah kanan
	glVertex3f( 1.3,  0.8,  1) #atas kanan
	glVertex3f( 1.6,  0.8,  1) #atas kiri
	glEnd()
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 1.6, 0.8, 0.7) #2
	glVertex3f( 1.6,  0, 0.7) #1
	glVertex3f( 1.6,  0,  1) #0
	glVertex3f( 1.6, 0.8,  1) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 1.3, 0.8, 0.7) #2
	glVertex3f( 1.3,  0, 0.7) #1
	glVertex3f( 1.3,  0,  1) #0
	glVertex3f( 1.3, 0.8,  1) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(1.6, 0,  0.7) #bawah kiri
	glVertex3f( 1.3, 0,  0.7) #bawah kanan
	glVertex3f( 1.3,  0.8, 0.7) #atas kanan
	glVertex3f( 1.6,  0.8,  0.7) #atas kiri
	glEnd()
	
	glFlush ()

def kubuskaki3():
	glColor3f(1, 1, 1) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(1.6, 0,  -0.4) #bawah kiri
	glVertex3f( 1.3, 0,  -0.4) #bawah kanan
	glVertex3f( 1.3,  0.8,  -0.4) #atas kanan
	glVertex3f( 1.6,  0.8,  -0.4) #atas kiri
	glEnd()
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 1.6, 0.8, -0.4) #2
	glVertex3f( 1.6,  0, -0.4) #1
	glVertex3f( 1.6,  0,  -0.7) #0
	glVertex3f( 1.6, 0.8,  -0.7) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(1.6, 0,  -0.7) #bawah kiri
	glVertex3f( 1.3, 0,  -0.7) #bawah kanan
	glVertex3f( 1.3,  0.8,  -0.7) #atas kanan
	glVertex3f( 1.6,  0.8,  -0.7) #atas kiri
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 1.3, 0.8, -0.4) #2
	glVertex3f( 1.3,  0, -0.4) #1
	glVertex3f( 1.3,  0,  -0.7) #0
	glVertex3f( 1.3, 0.8,  -0.7) #3
	glEnd()
	

	
	glFlush ()

def kubuskaki4():
	glColor3f(1, 1, 1) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-0.5, 0,  -0.4) #bawah kiri
	glVertex3f( -0.2, 0,  -0.4) #bawah kanan
	glVertex3f( -0.2,  0.8, -0.4) #atas kanan
	glVertex3f(-0.5,  0.8,  -0.4) #atas kiri
	glEnd()
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( -0.2, 0.8, -0.4) #2
	glVertex3f( -0.2,  0, -0.4) #1
	glVertex3f( -0.2,  0,  -0.7) #0
	glVertex3f( -0.2, 0.8,  -0.7) #3
	glEnd()

	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( -0.5, 0.8, -0.4) #2
	glVertex3f( -0.5,  0, -0.4) #1
	glVertex3f( -0.5,  0,  -0.7) #0
	glVertex3f( -0.5, 0.8,  -0.7) #3
	glEnd()

	glBegin(GL_QUADS)
	glVertex3f(-0.5, 0,  -0.7) #bawah kiri
	glVertex3f( -0.2, 0,  -0.7) #bawah kanan
	glVertex3f( -0.2,  0.8, -0.7) #atas kanan
	glVertex3f(-0.5,  0.8,  -0.7) #atas kiri
	glEnd()
	
	glFlush ()           

def kaki2():
	glColor3f(0, 0, 0) #warna garis adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.6, 0,  1) #bawah kiri
	glVertex3f( 1.3, 0,  1) #bawah kanan
	glVertex3f( 1.3,  0.8,  1) #atas kanan
	glVertex3f( 1.6,  0.8,  1) #atas kiri
	glEnd()
	
	# KANAN
	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.6, 0.8, 0.7) #2
	glVertex3f( 1.6,  0, 0.7) #1
	glVertex3f( 1.6,  0,  1) #0
	glVertex3f( 1.6, 0.8,  1) #3
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.3, 0.8, 0.7) #2
	glVertex3f( 1.3,  0, 0.7) #1
	glVertex3f( 1.3,  0,  1) #0
	glVertex3f( 1.3, 0.8,  1) #3
	glEnd()
	
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.6, 0,  0.7) #bawah kiri
	glVertex3f( 1.3, 0,  0.7) #bawah kanan
	glVertex3f( 1.3,  0.8,  0.7) #atas kanan
	glVertex3f( 1.6,  0.8,  0.7) #atas kiri
	glEnd()		

	glFlush ()

def kaki4():
	glColor3f(0, 0, 0) #warna garis adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(-0.5, 0,  -0.4) #bawah kiri
	glVertex3f( -0.2, 0,  -0.4) #bawah kanan
	glVertex3f( -0.2,  0.8, -0.4) #atas kanan
	glVertex3f(-0.5,  0.8,  -0.4) #atas kiri
	glEnd()
	
	# KANAN
	glBegin(GL_LINE_LOOP)
	glVertex3f( -0.2, 0.8, -0.4) #2
	glVertex3f( -0.2,  0, -0.4) #1
	glVertex3f( -0.2,  0,  -0.7) #0
	glVertex3f( -0.2, 0.8,  -0.7) #3
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f( -0.5, 0.8, -0.4) #2
	glVertex3f( -0.5,  0, -0.4) #1
	glVertex3f( -0.5,  0,  -0.7) #0
	glVertex3f( -0.5, 0.8,  -0.7) #3
	glEnd()	

	glBegin(GL_LINE_LOOP)
	glVertex3f(-0.5, 0,  -0.7) #bawah kiri
	glVertex3f( -0.2, 0,  -0.7) #bawah kanan
	glVertex3f( -0.2,  0.8, -0.7) #atas kanan
	glVertex3f(-0.5,  0.8,  -0.7) #atas kiri
	glEnd()	
	
	glFlush ()

def kaki3():
	glColor3f(0, 0, 0) #warna garis adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.6, 0,  -0.4) #bawah kiri
	glVertex3f( 1.3, 0,  -0.4) #bawah kanan
	glVertex3f( 1.3,  0.8,  -0.4) #atas kanan
	glVertex3f( 1.6,  0.8,  -0.4) #atas kiri
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f(1.6, 0,  -0.7) #bawah kiri
	glVertex3f( 1.3, 0,  -0.7) #bawah kanan
	glVertex3f( 1.3,  0.8,  -0.7) #atas kanan
	glVertex3f( 1.6,  0.8,  -0.7) #atas kiri
	glEnd()

	# KANAN
	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.6, 0.8, -0.4) #2
	glVertex3f( 1.6,  0, -0.4) #1
	glVertex3f( 1.6,  0,  -0.7) #0
	glVertex3f( 1.6, 0.8,  -0.7) #3
	glEnd()

	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.3, 0.8, -0.4) #2
	glVertex3f( 1.3,  0, -0.4) #1
	glVertex3f( 1.3,  0,  -0.7) #0
	glVertex3f( 1.3, 0.8,  -0.7) #3
	glEnd()

	glFlush ()            

#membuat KUBUS dengan warna garis adalah hitam
def gambarKubus():
	glPushMatrix()
	glColor3f(1, 1, 1)
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f( 2.1, 0.8,  1) #3
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f(-1,  1,  1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  -0.7) #6
	glVertex3f( 2.1, 0.8,  -0.7) #3
	glVertex3f( 2.1,  1,  -0.7) #0
	glVertex3f(-1,  1,  -0.7) #4
	glEnd()
	
	# KIRI
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f(-1,  1,  1) #4
	glVertex3f(-1,  1, -0.7) #7
	glVertex3f(-1, 0.8, -0.7) #5
	glEnd();
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 2.1, 0.8, -0.7) #2
	glVertex3f( 2.1,  1, -0.7) #1
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f( 2.1, 0.8,  1) #3
	glEnd()
	
	img1()
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 0.0); glVertex3f(-1,  1,  1) #4
	glTexCoord2f(1.0, 0.0); glVertex3f( 2.1,  1,  1) #0
	glTexCoord2f(1.0, 1.0); glVertex3f( 2.1,  1, -0.7) #1
	glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1, -0.7) #7
	glEnd()
	glPopMatrix()
    
	glFlush ()

def gambarKubus2():
	glColor3f(1, 1, 1)
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f( 2.1, 0.8,  1) #3
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f(-1,  1,  1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  -0.7) #6
	glVertex3f( 2.1, 0.8,  -0.7) #3
	glVertex3f( 2.1,  1,  -0.7) #0
	glVertex3f(-1,  1,  -0.7) #4
	glEnd()
	
	# KIRI
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f(-1,  1,  1) #4
	glVertex3f(-1,  1, -0.7) #7
	glVertex3f(-1, 0.8, -0.7) #5
	glEnd();
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 2.1, 0.8, -0.7) #2
	glVertex3f( 2.1,  1, -0.7) #1
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f( 2.1, 0.8,  1) #3
	glEnd()
	
	img2()
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 0.0); glVertex3f(-1,  1,  1) #4
	glTexCoord2f(1.0, 0.0); glVertex3f( 2.1,  1,  1) #0
	glTexCoord2f(1.0, 1.0); glVertex3f( 2.1,  1, -0.7) #1
	glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1, -0.7) #7
	glEnd()
    
	glFlush ()

def gambarKubus3():
	glColor3f(1, 1, 1)
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f( 2.1, 0.8,  1) #3
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f(-1,  1,  1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  -0.7) #6
	glVertex3f( 2.1, 0.8,  -0.7) #3
	glVertex3f( 2.1,  1,  -0.7) #0
	glVertex3f(-1,  1,  -0.7) #4
	glEnd()
	
	# KIRI
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f(-1, 0.8,  1) #6
	glVertex3f(-1,  1,  1) #4
	glVertex3f(-1,  1, -0.7) #7
	glVertex3f(-1, 0.8, -0.7) #5
	glEnd();
	
	# KANAN
	glColor3f(1, 1, 1)
	glBegin(GL_QUADS)
	glVertex3f( 2.1, 0.8, -0.7) #2
	glVertex3f( 2.1,  1, -0.7) #1
	glVertex3f( 2.1,  1,  1) #0
	glVertex3f( 2.1, 0.8,  1) #3
	glEnd()
	
	img3()
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 0.0); glVertex3f(-1,  1,  1) #4
	glTexCoord2f(1.0, 0.0); glVertex3f( 2.1,  1,  1) #0
	glTexCoord2f(1.0, 1.0); glVertex3f( 2.1,  1, -0.7) #1
	glTexCoord2f(0.0, 1.0); glVertex3f(-1,  1, -0.7) #7
	glEnd()
    
	glFlush ()

#4 KUBUS DI MEJA
def benda1():
	glColor3f(1, 0, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(0, 1,  -0.1) #6
	glVertex3f( 0.5, 1,  -0.1) #3
	glVertex3f( 0.5,  1.5,  -0.1) #0
	glVertex3f(0,  1.5,  -0.1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(1, 0, 0)
	glBegin(GL_QUADS)
	glVertex3f(0, 1,  -0.5) #6
	glVertex3f( 0.5, 1,  -0.5) #3
	glVertex3f( 0.5,  1.5,  -0.5) #0
	glVertex3f(0,  1.5,  -0.5) #4
	glEnd()
	
	# KIRI
	glColor3f(1, 0, 0)
	glBegin(GL_QUADS)
	glVertex3f(0, 1.5,  -0.1) #6
	glVertex3f(0,  1,  -0.1) #4
	glVertex3f(0,  1, -0.5) #7
	glVertex3f(0, 1.5, -0.5) #5
	glEnd();
	
	# KANAN
	glColor3f(1, 0, 0)
	glBegin(GL_QUADS)
	glVertex3f( 0.5, 1.5, -0.5) #2
	glVertex3f( 0.5,  1, -0.5) #1
	glVertex3f( 0.5,  1,  -0.1) #0
	glVertex3f( 0.5, 1.5,  -0.1) #3
	glEnd()
	
	#ATAS
	glColor3f(1, 0, 0)
	glBegin(GL_QUADS)
	glVertex3f(0,  1.5,  -0.1) #4
	glVertex3f( 0.5,  1.5,  -0.1) #0
	glVertex3f( 0.5,  1.5, -0.5) #1
	glVertex3f(0,  1.5, -0.5) #7
	glEnd()
    
	glFlush ()

def benda2():
	glColor3f(1, 0, 0.7) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(0.6, 1,  0) #6
	glVertex3f( 0.8, 1,  0) #3
	glVertex3f( 0.8,  1.2,  0) #0
	glVertex3f(0.6,  1.2,  0) #4
	glEnd()
	
	# BELAKANG
	glColor3f(1, 0, 0.7)
	glBegin(GL_QUADS)
	glVertex3f(0.6, 1,  -0.2) #6
	glVertex3f( 0.8, 1,  -0.2) #3
	glVertex3f( 0.8,  1.2,  -0.2) #0
	glVertex3f(0.6,  1.2,  -0.2) #4
	glEnd()
	
	# KIRI
	glColor3f(1, 0, 0.7)
	glBegin(GL_QUADS)
	glVertex3f(0.6, 1.2,  0) #6
	glVertex3f(0.6,  1,  0) #4
	glVertex3f(0.6,  1, -0.2) #7
	glVertex3f(0.6, 1.2, -0.2) #5
	glEnd();
	
	# KANAN
	glColor3f(1, 0, 0.7)
	glBegin(GL_QUADS)
	glVertex3f( 0.8, 1.2, -0.2) #2
	glVertex3f( 0.8,  1, -0.2) #1
	glVertex3f( 0.8,  1,  0) #0
	glVertex3f( 0.8, 1.2,  0) #3
	glEnd()
	
	#ATAS
	glColor3f(1, 0, 0.7)
	glBegin(GL_QUADS)
	glVertex3f(0.6,  1.2,  0) #4
	glVertex3f( 0.8,  1.2,  0) #0
	glVertex3f( 0.8,  1.2, -0.2) #1
	glVertex3f(0.6,  1.2, -0.2) #7
	glEnd()
    
	glFlush ()

def benda2Kawat():
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(0.6, 1,  0) #6
	glVertex3f( 0.8, 1,  0) #3
	glVertex3f( 0.8,  1.2,  0) #0
	glVertex3f(0.6,  1.2,  0) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(0.6, 1,  -0.2) #6
	glVertex3f( 0.8, 1,  -0.2) #3
	glVertex3f( 0.8,  1.2,  -0.2) #0
	glVertex3f(0.6,  1.2,  -0.2) #4
	glEnd()
	
	# KIRI
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(0.6, 1.2,  0) #6
	glVertex3f(0.6,  1,  0) #4
	glVertex3f(0.6,  1, -0.2) #7
	glVertex3f(0.6, 1.2, -0.2) #5
	glEnd();
	
	# KANAN
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f( 0.8, 1.2, -0.2) #2
	glVertex3f( 0.8,  1, -0.2) #1
	glVertex3f( 0.8,  1,  0) #0
	glVertex3f( 0.8, 1.2,  0) #3
	glEnd()
	
	#ATAS
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(0.6,  1.2,  0) #4
	glVertex3f( 0.8,  1.2,  0) #0
	glVertex3f( 0.8,  1.2, -0.2) #1
	glVertex3f(0.6,  1.2, -0.2) #7
	glEnd()
    
	glFlush ()

def benda3():
	glColor3f(0, 0.7, 1) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(1.2, 1,  0) #6
	glVertex3f( 1.5, 1,  0) #3
	glVertex3f( 1.5,  1.3,  0) #0
	glVertex3f(1.2,  1.3,  0) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0, 0.7, 1)
	glBegin(GL_QUADS)
	glVertex3f(1.2, 1,  -0.2) #6
	glVertex3f( 1.5, 1,  -0.2) #3
	glVertex3f( 1.5,  1.3,  -0.2) #0
	glVertex3f(1.2,  1.3,  -0.2) #4
	glEnd()
	
	# KIRI
	glColor3f(0, 0.7, 1)
	glBegin(GL_QUADS)
	glVertex3f(1.2, 1.3,  0) #6
	glVertex3f(1.2,  1,  0) #4
	glVertex3f(1.2,  1, -0.2) #7
	glVertex3f(1.2, 1.3, -0.2) #5
	glEnd();
	
	# KANAN
	glColor3f(0, 0.5, 1)
	glBegin(GL_QUADS)
	glVertex3f( 1.5, 1.3, -0.2) #2
	glVertex3f( 1.5,  1, -0.2) #1
	glVertex3f( 1.5,  1,  0) #0
	glVertex3f( 1.5, 1.3,  0) #3
	glEnd()
	
	#ATAS
	glColor3f(0, 0.7, 1)
	glBegin(GL_QUADS)
	glVertex3f(1.2,  1.3,  0) #4
	glVertex3f( 1.5,  1.3,  0) #0
	glVertex3f( 1.5,  1.3, -0.2) #1
	glVertex3f(1.2,  1.3, -0.2) #7
	glEnd()
    
	glFlush ()

def benda3Kawat():
	glColor3f(0, 0, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.2, 1,  0) #6
	glVertex3f( 1.5, 1,  0) #3
	glVertex3f( 1.5,  1.3,  0) #0
	glVertex3f(1.2,  1.3,  0) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.2, 1,  -0.2) #6
	glVertex3f( 1.5, 1,  -0.2) #3
	glVertex3f( 1.5,  1.3,  -0.2) #0
	glVertex3f(1.2,  1.3,  -0.2) #4
	glEnd()
	
	# KIRI
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.2, 1.3,  0) #6
	glVertex3f(1.2,  1,  0) #4
	glVertex3f(1.2,  1, -0.2) #7
	glVertex3f(1.2, 1.3, -0.2) #5
	glEnd();
	
	# KANAN
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.5, 1.3, -0.2) #2
	glVertex3f( 1.5,  1, -0.2) #1
	glVertex3f( 1.5,  1,  0) #0
	glVertex3f( 1.5, 1.3,  0) #3
	glEnd()
	
	#ATAS
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(1.2,  1.3,  0) #4
	glVertex3f( 1.5,  1.3,  0) #0
	glVertex3f( 1.5,  1.3, -0.2) #1
	glVertex3f(1.2,  1.3, -0.2) #7
	glEnd()
    
	glFlush ()	

def benda4():
	glColor3f(0.7, 0.3, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_QUADS)
	glVertex3f(1, 1,  0.8) #6
	glVertex3f( 1.5, 1,  0.8) #3
	glVertex3f( 1.5,  1.1,  0.8) #0
	glVertex3f(1,  1.1,  0.8) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0.7, 0.3, 0)
	glBegin(GL_QUADS)
	glVertex3f(1, 1,  0.5) #6
	glVertex3f( 1.5, 1,  0.5) #3
	glVertex3f( 1.5,  1.1,  0.5) #0
	glVertex3f(1,  1.1,  0.5) #4
	glEnd()
	
	# KIRI
	glColor3f(0.7, 0.3, 0)
	glBegin(GL_QUADS)
	glVertex3f(1, 1.1,  0.8) #6
	glVertex3f(1,  1,  0.8) #4
	glVertex3f(1,  1, 0.5) #7
	glVertex3f(1, 1.1, 0.5) #5
	glEnd();
	
	# KANAN
	glColor3f(0.7, 0.3, 0)
	glBegin(GL_QUADS)
	glVertex3f( 1.5, 1.1, 0.5) #2
	glVertex3f( 1.5,  1, 0.5) #1
	glVertex3f( 1.5,  1,  0.8) #0
	glVertex3f( 1.5, 1.1,  0.8) #3
	glEnd()
	
	#ATAS
	glColor3f(0.7, 0.3, 0)
	glBegin(GL_QUADS)
	glVertex3f(1,  1.1,  0.8) #4
	glVertex3f( 1.5,  1.1, 0.8) #0
	glVertex3f( 1.5,  1.1, 0.5) #1
	glVertex3f(1,  1.1, 0.5) #7
	glEnd()
    
	glFlush ()

def benda4Kawat():
    #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(1, 1,  0.8) #6
	glVertex3f( 1.5, 1,  0.8) #3
	glVertex3f( 1.5,  1.1,  0.8) #0
	glVertex3f(1,  1.1,  0.8) #4
	glEnd()
	
	# BELAKANG
	glBegin(GL_LINE_LOOP)
	glVertex3f(1, 1,  0.5) #6
	glVertex3f( 1.5, 1,  0.5) #3
	glVertex3f( 1.5,  1.1,  0.5) #0
	glVertex3f(1,  1.1,  0.5) #4
	glEnd()
	
	# KIRI
	glBegin(GL_LINE_LOOP)
	glVertex3f(1, 1.1,  0.8) #6
	glVertex3f(1,  1,  0.8) #4
	glVertex3f(1,  1, 0.5) #7
	glVertex3f(1, 1.1, 0.5) #5
	glEnd();
	
	# KANAN
	glBegin(GL_LINE_LOOP)
	glVertex3f( 1.5, 1.1, 0.5) #2
	glVertex3f( 1.5,  1, 0.5) #1
	glVertex3f( 1.5,  1,  0.8) #0
	glVertex3f( 1.5, 1.1,  0.8) #3
	glEnd()
	
	#ATAS
	glBegin(GL_LINE_LOOP)
	glVertex3f(1,  1.1,  0.8) #4
	glVertex3f( 1.5,  1.1, 0.8) #0
	glVertex3f( 1.5,  1.1, 0.5) #1
	glVertex3f(1,  1.1, 0.5) #7
	glEnd()
    
	glFlush ()

def benda1Kawat():
	glColor3f(0, 0, 0) #warna kawasan adalah hitam
	# DEPAN, Berlawanan arah dengan jarum jam
	glBegin(GL_LINE_LOOP)
	glVertex3f(0, 1,  -0.1) #6
	glVertex3f( 0.5, 1,  -0.1) #3
	glVertex3f( 0.5,  1.5,  -0.1) #0
	glVertex3f(0,  1.5,  -0.1) #4
	glEnd()
	
	# BELAKANG
	glColor3f(0, 0, 0) 
	glBegin(GL_LINE_LOOP)
	glVertex3f(0, 1,  -0.5) #6
	glVertex3f( 0.5, 1,  -0.5) #3
	glVertex3f( 0.5,  1.5,  -0.5) #0
	glVertex3f(0,  1.5,  -0.5) #4
	glEnd()
	
	# KIRI
	glColor3f(0, 0, 0) 
	glBegin(GL_LINE_LOOP)
	glVertex3f(0, 1.5,  -0.1) #6
	glVertex3f(0,  1,  -0.1) #4
	glVertex3f(0,  1, -0.5) #7
	glVertex3f(0, 1.5, -0.5) #5
	glEnd();
	
	# KANAN
	glColor3f(0, 0, 0) 
	glBegin(GL_LINE_LOOP)
	glVertex3f( 0.5, 1.5, -0.5) #2
	glVertex3f( 0.5,  1, -0.5) #1
	glVertex3f( 0.5,  1,  -0.1) #0
	glVertex3f( 0.5, 1.5,  -0.1) #3
	glEnd()
	
	#ATAS
	glColor3f(0, 0, 0)
	glBegin(GL_LINE_LOOP)
	glVertex3f(0,  1.5,  -0.1) #4
	glVertex3f( 0.5,  1.5,  -0.1) #0
	glVertex3f( 0.5,  1.5, -0.5) #1
	glVertex3f(0,  1.5, -0.5) #7
	glEnd()
    
	glFlush ()

def mejaku():
    kubuskaki1()
    kubuskaki2()
    kubuskaki3()
    kubuskaki4()
    kaki1()
    kaki2()
    kaki3()
    kaki4()
    benda4Kawat()
    benda2Kawat()
    benda3Kawat()
    benda2()
    benda3()
    benda4()
    gambarKubusKawat()

	
def main():
    pygame.init()
    display = (800,600) 
    keys["img01"] = True
    nilai_X=0
    nilai_Y=0
    nilai_Z=0
    sudutPutar=1
    pygame.display.set_mode(display, pygame.OPENGL|pygame.DOUBLEBUF)
    gluPerspective(45, display[0]/display[1],0.1,50.0)
    glTranslatef(0, -1, -8)
    glRotatef( -35, -35, 90, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable( GL_TEXTURE_2D )
    glEnable( GL_DEPTH_TEST )   		
    lantai()
    pegangan()
    mejaku()
 
	

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        mejaku()
        lantai()
	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                sudutPutar += 0.1
                glRotatef(sudutPutar, 0, 1, 0)		

            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    if keys["img01"] == True:
                        keys["img01"] = False
                        keys["img02"] = True
                    elif keys["img02"] == True:
                        keys["img02"] = False
                        keys["img03"] = True
                    elif keys["img03"] == True:
                        keys["img03"] = False
                        keys["img01"] = True

            if event.type == pygame.KEYDOWN:
                    if event.key == K_UP:
                        keys["depan"] = True
                    elif event.key == K_DOWN:
                        keys["belakang"] = True
                    if event.key == K_RIGHT:					
                        keys["kanan"] = True				
                    elif event.key == K_LEFT:
                        keys["kiri"] = True
                    if event.key == K_d:
                        keys["depan_lemari"] = True
                    elif event.key == K_b:
                        keys["belakang_lemari"] = True
					
            if event.type == pygame.KEYUP:
                    if event.key == K_UP:
                        keys["depan"] = False
                    elif event.key == K_DOWN:
                        keys["belakang"] = False
                    if event.key == K_RIGHT:
                        keys["kanan"] = False
                    elif event.key == K_LEFT:
                        keys["kiri"] = False
                    if event.key == K_d:
                        keys["depan_lemari"] = False
                    elif event.key == K_b:
                        keys["belakang_lemari"] = False

        glPushMatrix()
        glTranslatef(nilai_X, 0, nilai_Z)
        benda1()
        benda1Kawat()		
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0, nilai_Y)
        pegangan()
        lemari()
        lemariKawat()
        glPopMatrix()		

        if keys["kanan"] == True:
            glPushMatrix()
            if nilai_X < 1.5:
                nilai_X += 0.01 # tambah nilai X
                glTranslatef(nilai_X, 0, 0)
            glPopMatrix()

        if keys["kiri"] == True:		
            glPushMatrix()
            if nilai_X > -1:			
                nilai_X -= 0.01 # kurangi nilai X 
                glTranslatef(nilai_X, 0, 0)
            glPopMatrix()		

        if keys["depan"] == True:
            glPushMatrix()
            if nilai_Z < 1.1:			
                nilai_Z += 0.01 # tambah nilai z
                glTranslatef(0, 0, nilai_Z)
            glPopMatrix()

        if keys["belakang"] == True:		
            glPushMatrix()
            if nilai_Z > -0.2:				
                nilai_Z -= 0.01 # kurang nilai z
                glTranslatef(0, 0, nilai_Z)
            glPopMatrix()

        if keys["depan_lemari"] == True:		
            glPushMatrix()
            if nilai_Y < 5:				
                nilai_Y += 0.01 # kurang nilai Y
                glTranslatef(0, 0, nilai_Y)
            glPopMatrix()

        if keys["belakang_lemari"] == True:		
            glPushMatrix()
            if nilai_Y > 0:				
                nilai_Y -= 0.01 # kurang nilai Y
                glTranslatef(0, 0, nilai_Y)
            glPopMatrix()	

        if keys["img01"]:
            gambarKubus()
        if keys["img02"]:
            gambarKubus2()
        if keys["img03"]:
            gambarKubus3()

        pygame.display.flip()

main()
# Akhir PROGRAM
