from glapp.PyOGLApp import *
from glapp.Utils import *
import numpy as np
from OpenGL.arrays.vbo import VBO
from glapp.GraphicsData import *

# simple shader that draws a point at 0, 0, 0 and colors it green
vertex_shader = r'''
#version 330 core
in vec3 position;
void main()
{
    gl_Position = vec4(position, 1); 
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
        self.vertex_count = 0

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_id = glGenVertexArrays(1)
        glBindVertexArray(self.vao_id)
        glPointSize(10)
        position_data = [[0, -0.9, 0],
                    [-0.6, 0.8, 0],
                    [0.9, -0.2, 0],
                    [-0.9, -0.2, 0],
                    [0.6, 0.8, 0]]

        self.vertex_count = len(position_data)  # returns number of vertices
        position_variable = GraphicsData("vec3", position_data)
        position_variable.create_variable(self.program_id, "position")


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)  # able to draw without referencing an array because we bound
        # the vertex array in initialise method. This uses the last bound vertex array


MyFirstShader().mainloop()
