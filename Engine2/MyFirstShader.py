from glapp.PyOGLApp import *
from glapp.Utils import *
import numpy as np
from OpenGL.arrays.vbo import VBO

# simple shader that draws a point at 0, 0, 0 and colors it green
vertex_shader = r'''
#version 330 core

void main()
{
    gl_Position = vec4(0.5, 0.5, 0, 1); 
}
'''

fragment_shader = r'''
#version 330 core

out vec4 frag_color;

void main()
{
    frag_color = vec4(1, 1, 0, 1);
}
'''


class MyFirstShader(PyOGLApp):
    def __init__(self):
        super().__init__(2200, 200, 1000, 800)
        self.vao_id = None  # vao = vertex array object

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_id = glGenVertexArrays(1)
        glBindVertexArray(self.vao_id)
        glPointSize(10)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_POINTS, 0, 1)  # able to draw without referencing an array because we bound the vertex array in
        # initialise method. This uses the last bound vertex array


MyFirstShader().mainloop()
