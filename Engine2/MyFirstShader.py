from glapp.PyOGLApp import *
from glapp.Utils import *
import numpy as np
from OpenGL.arrays.vbo import VBO
from glapp.GraphicsData import *
from glapp.Square import *

# simple shader that draws a point at 0, 0, 0 and colors it green
vertex_shader = r'''
#version 330 core
in vec3 position;
in vec3 vertex_color;
out vec3 color;

void main()
{
    gl_Position = vec4(position, 1); 
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


class MyFirstShader(PyOGLApp):
    def __init__(self):
        super().__init__(2200, 200, 1000, 800)
        self.square = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.square = Square(self.program_id)


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        self.square.draw()


MyFirstShader().mainloop()
