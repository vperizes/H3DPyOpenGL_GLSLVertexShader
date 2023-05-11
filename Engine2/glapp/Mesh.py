import pygame
from OpenGL import *
from .GraphicsData import *
import numpy as np
from pygame import *
from .Uniform import *


class Mesh:
    def __init__(self, program_id, vertices, vertex_colors, draw_type, translation=pygame.Vector3(0, 0, 0)):
        self.vertices = vertices
        self.draw_type = draw_type
        self.vao_id = glGenVertexArrays(1)
        glBindVertexArray(self.vao_id)
        position = GraphicsData("vec3", self.vertices)
        position.create_variable(program_id, "position")
        colors = GraphicsData("vec3", vertex_colors)
        colors.create_variable(program_id, "vertex_color")
        self.translation = Uniform("vec3", translation)
        self.translation.find_variable(program_id, "translation")

    def draw(self):
        self.translation.load()  # need to load translation data before binding
        glBindVertexArray(self.vao_id)
        glDrawArrays(self.draw_type, 0, len(self.vertices))
