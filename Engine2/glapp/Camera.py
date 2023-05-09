import pygame
from OpenGL.GLU import *
from math import *


class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)  # this is the direction that the camera is looking in. The base of
        # this vector is at eye
        self.look = self.eye + self.forward
        self.yaw = 90  # angle for yaw, rotates about y-axis
        self.pitch = 0  # angle for pitch, rotates about x-axis

        # using mouse to move these angles -> need to record last pos of mouse and figure out updated mouse pos
        self.last_mouse = pygame.math.Vector2(0, 0)  # initial value for mouse position, stores last mouse pos
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.8

    def rotate_camera(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch
        if self.pitch > 89.0:
            self.pitch = 89.0

        if self.pitch < -89.0:
            self.pitch = 89.0
        self.forward.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward.y = sin(radians(self.yaw))
        self.forward.z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        self.forward = self.forward.normalize()
        #  since our forward vector has changed, we must now update our right and up vectors to be perpendicular to our
        #  new forward vector
        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()  # crossing new forward vector with up
        # vector gives us a new right vector
        self.up = self.right.cross(self.forward).normalize()  # crossing the new right vector with the new forward
        # vector gives us a new up vector


    def update_camera(self, w, h):
        if pygame.mouse.get_visible():  # if mouse is visible then we do not execute the rest fo the code
            return
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(w/2, h/2)  # put mouse back in center of screen after a movement
        self.last_mouse = pygame.mouse.get_pos()  # updates last_mouse
        # we use the mouse_change x pos for the yaw (rotate about y-axis) b/c the x pos of mouse acts as the moment arm
        # to allow rotation to happen. Same idea for using mouse_chamge.y for pitch
        self.rotate_camera(-mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * self.key_sensitivity
        elif keys[pygame.K_UP]:
            self.eye += self.forward * self.key_sensitivity
        elif keys[pygame.K_RIGHT]:
            self.eye -= self.right * self.key_sensitivity
        elif keys[pygame.K_LEFT]:
            self.eye += self.right * self.key_sensitivity

        self.look = self.eye + self.forward  # need to update self.look since eye has moved
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
