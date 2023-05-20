import pygame

from glapp.PyOGLApp import *
from glapp.Utils import *
import numpy as np
from OpenGL.arrays.vbo import VBO
from glapp.GraphicsData import *
from glapp.Square import *
from glapp.Triangle import *
from glapp.Axes import *

# simple shader that draws a point at 0, 0, 0 and colors it green
vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertex_color;
uniform mat4 projection_mat;
uniform mat4 view_mat;
uniform mat4 model_mat;
out vec3 color;

void main()
{
    //need to take the inverse of view mat - pov is now through camera so need inverse to correctly rep objects
    gl_Position = projection_mat * inverse(view_mat) * model_mat * vec4(position, 1); 
    color = vertex_color;
}
'''

fragment_shader = r'''
#version 330 core
in vec3 color;
out vec4 frag_color;

void main()
{
    frag_color = vec4(color, 1);
}
'''


class GLSL_Shader1(PyOGLApp):
    def __init__(self):
        super().__init__(2200, 200, 1000, 800)
        self.square = None
        self.triangle = None
        self.axes = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id, pygame.Vector3(-1, 1, 0))
        self.triangle = Triangle(self.program_id, pygame.Vector3(0.5, -0.5, 0))
        self.axes = Axes(self.program_id, pygame.Vector3(0, 0, 0))
        self.camera = Camera(self.program_id, self.screen_width, self.screen_height)
        glEnable(GL_DEPTH_TEST)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.camera.update_camera()
        self.square.draw()
        self.triangle.draw()
        self.axes.draw()


GLSL_Shader1().mainloop()
