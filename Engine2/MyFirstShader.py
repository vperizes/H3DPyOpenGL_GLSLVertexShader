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
        self.vao_id = None  # vao = vertex array object
        self.vertex_count = 0

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        # vao stores all states needed to supply vertex data to graphics pipeline - i.e. format of vertex data,
        # location of vertex data in memory, and associated attribs (color, texture coords, etc)
        self.vao_id = glGenVertexArrays(1)  # creating a single new VAO id/ref
        glBindVertexArray(self.vao_id)  # vao is now bound and state of vertex attribute array is set - this defines
        # layout and data state of vertex data in VBO (vertex buffer obj)
        glLineWidth(2)
        position_data = [[0, -0.9, 0],
                    [-0.6, 0.8, 0],
                    [0.9, -0.2, 0],
                    [-0.9, -0.2, 0],
                    [0.6, 0.8, 0]]

        self.vertex_count = len(position_data)  # returns number of vertices
        position_variable = GraphicsData("vec3", position_data)
        position_variable.create_variable(self.program_id, "position")

        color_data = [[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1],
                      [1, 0, 1],
                      [1, 1, 0]]
        color_variable = GraphicsData("vec3", color_data)
        color_variable.create_variable(self.program_id, "vertex_color")


    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertex_count)  # able to draw without referencing an array because we bound
        # the vertex array in initialise method. This uses the last bound vertex array


MyFirstShader().mainloop()
