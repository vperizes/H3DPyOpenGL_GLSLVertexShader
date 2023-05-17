import numpy as np
from math import *


# first defining the identity matrix
# could use np.identity but for this exercise we're visualizing its use
def identity_matrix():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)


def translation_matrix(x, y, z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]], np.float32)


def scale_matrix(s):
    return np.array([[s, 0, 0, 0],
                     [0, s, 0, 0],
                     [0, 0, s, 0],
                     [0, 0, 0, 1]], np.float32)


def scale_matrix3(sx, sy, sz):
    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]], np.float32)


# rotating around the x
def rotate_x_matrix(angle):
    cosine = cos(radians(angle))  # converting to radians allows us to pass in degrees
    sine = sin(radians(angle))
    return np.array([[1, 0, 0, 0],
                     [0, cosine, -sine, 0],
                     [0, sine, cosine, 0],
                     [0, 0, 0, 1]], np.float32)


# rotating around the y
def rotate_y_matrix(angle):
    cosine = cos(radians(angle))
    sine = sin(radians(angle))
    return np.array([[cosine, 0, sine, 0],
                     [0, 1, 0, 0],
                     [-sine, 0, cosine, 0],
                     [0, 0, 0, 1]], np.float32)


# rotating around the z
def rotate_z_matrix(angle):
    cosine = cos(radians(angle))
    sine = sin(radians(angle))
    return np.array([[cosine, -sine, 0, 0],
                     [sine, cosine, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]], np.float32)


# the matrix input of the translate method takes the current matrix of whatever we are trying to translate and the
# values that we want to translate that object by
def translate(matrix, x, y, z):
    trans = translation_matrix(x, y, z)
    return matrix @ trans  # multiplying current matrix with translation matrix constructed in previous line


def scale(matrix, cons):
    sc = scale_matrix(cons)
    return matrix @ sc


def scale3(matrix, x, y, z):
    sc = scale_matrix3(x, y, z)
    return matrix @ sc


def rotate(matrix, angle, axis):
    rot = identity_matrix()
    if axis == "x":
        rot = rotate_x_matrix(angle)
    elif axis == "y":
        rot = rotate_y_matrix(angle)
    elif axis == "z":
        rot = rotate_z_matrix(angle)

    return matrix @ rot

