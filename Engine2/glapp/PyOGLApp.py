from pygame.locals import *
from .Camera import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os


class PyOGLApp():
    def __init__(self, screen_posX, screen_posY, screen_width, screen_height):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_posX, screen_posY)
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('OpenGL in Python')
        self.camera = Camera()

    def draw_world_axes(self):
        glLineWidth(4)
        glBegin(GL_LINES)
        glColor(1, 0, 0)  # red color for x-axis
        glVertex3d(-1000, 0, 0)  # neg x
        glVertex3d(1000, 0, 0)  # pos x
        glColor(0, 1, 0)  # green color for y-axis
        glVertex3d(0, -1000, 0)
        glVertex3d(0, 1000, 0)
        glColor(0, 0, 1)  # blue color for z-axis
        glVertex3d(0, 0, -1000)
        glVertex3d(0, 0, 1000)
        glEnd()

        # sphere indicating pos x
        sphere = gluNewQuadric()
        glColor(1, 0, 0)
        glPushMatrix()
        glTranslated(1, 0, 0)  # adding glPush and glPop so that glTranslated does not effect the next sphere
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        # sphere indicating pos y
        glColor(0, 1, 0)
        glPushMatrix()
        glTranslated(0, 1, 0)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        # sphere indicating pos y
        glColor(0, 0, 1)
        glPushMatrix()
        glTranslated(0, 0, 1)
        gluSphere(sphere, 0.05, 10, 10)
        glPopMatrix()

        # Color and line width for cube
        glColor(1, 1, 1)
        glLineWidth(1)

    def initialise(self):
        pass

    def display(self):
        pass

    def camera_init(self):
        pass

    def mainloop(self):
        done = False
        self.initialise()
        pygame.event.set_grab(True)  # grabs hold of mouse. Not usable for other windows when app is running
        pygame.mouse.set_visible(
            False)  # mouse is no longer visible. Can't use it to shut window down --> program key press

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.event.set_grab(False)
                        pygame.mouse.set_visible(True)
            self.camera_init()
            self.display()
            pygame.display.flip()
        pygame.quit()

