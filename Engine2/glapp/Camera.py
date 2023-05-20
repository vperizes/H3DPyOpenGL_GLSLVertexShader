import pygame
from OpenGL.GLU import *
from math import *
import numpy as np
from .Transformations import *
from .Uniform import *



class Camera:
    def __init__(self, program_id, width, height):
        self.transformation = identity_matrix()

        # using mouse to move these angles -> need to record last pos of mouse and figure out updated mouse pos
        self.last_mouse = pygame.math.Vector2(0, 0)  # initial value for mouse position, stores last mouse pos
        self.mouse_sensitivityX = 0.1
        self.mouse_sensitivityY = 0.1
        self.key_sensitivity = 0.08
        self.projection_matrix = self.perspective_mat(60, width/height, 0.01, 1000)
        self.projection = Uniform("mat4", self.projection_matrix)
        self.projection.find_variable(program_id, "projection_mat")
        self.screen_width = width
        self.screen_height = height
        self.program_id = program_id

    def perspective_mat(self, angle_of_view, aspect_ratio, near_plane, far_plane):
        a = radians(angle_of_view)
        d = 1.0 / tan(a/2.0)
        r = aspect_ratio
        b = (far_plane + near_plane)/(near_plane - far_plane)
        c = (far_plane * near_plane)/(near_plane - far_plane)
        # transpose of perspective matrix used because of order of matrix multiplication
        return np.array([[d/r, 0, 0, 0],
                         [0, d, 0, 0],
                         [0, 0, b, c],
                         [0, 0, -1, 0]], np.float32)

    def rotate_camera(self, yaw, pitch):
        self.transformation = rotate(self.transformation, yaw, "y")
        self.transformation = rotate(self.transformation, pitch, "x")


    def update_camera(self):
        if pygame.mouse.get_visible():  # if mouse is visible then we do not execute the rest fo the code
            return
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos(self.screen_width/2, self.screen_height/2)  # put mouse back in center of screen after a
        # movement
        self.last_mouse = pygame.mouse.get_pos()  # updates last_mouse
        # we use the mouse_change x pos for the yaw (rotate about y-axis) b/c the x pos of mouse acts as the moment arm
        # to allow rotation to happen. Same idea for using mouse_change.y for pitch
        self.rotate_camera(mouse_change.x * self.mouse_sensitivityX, mouse_change.y * self.mouse_sensitivityY)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.transformation = translate(self.transformation, 0, 0, self.key_sensitivity)
        elif keys[pygame.K_UP]:
            self.transformation = translate(self.transformation, 0, 0, -self.key_sensitivity)
        elif keys[pygame.K_RIGHT]:
            self.transformation = translate(self.transformation, self.key_sensitivity, 0, 0)
        elif keys[pygame.K_LEFT]:
            self.transformation = translate(self.transformation, -self.key_sensitivity, 0, 0)

        self.projection.load()  # load perspective matrix
        lookat_mat = self.transformation
        lookat = Uniform("mat4", lookat_mat)
        lookat.find_variable(self.program_id, "view_mat")
        lookat.load()  # loads correct transformation for camera orientation (where the camera is looking at)
