from OpenGL.GL import *
import numpy as np

class GraphicsData():
    def __init__(self, data_type, data):
        self.data_type = data_type
        self.data = data
        self.buffer_ref = glGenBuffers(1)
        self.load()  # loads data into memory

    def load(self):
        data = np.array(self.data, np.float32)  # converts input data into an array
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)  # binding the buffer object referenced by self.buffer_ref to
        # GL_array_buffer target. This prepares buffer to be filled with data using glBufferData
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)  # data.ravel converts data into a 1D array


# create variables to put data into
    def create_variable(self, program_id, variable_name):
        variable_id = glGetAttribLocation(program_id, variable_name)  # gets pointer to variable so we can insert data
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)  # need to bind buffer object again so that the attribute pointer
        # 'glVertexAttribPointer' knows which buffer to use
        if self.data_type == "vec3":
            glVertexAttribPointer(variable_id, 3, GL_FLOAT, False, 0, None)

        glEnableVertexAttribArray(variable_id)  # enables specified variable + indicates that variable will be used as
        # an input to the vertex shader