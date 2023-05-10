from OpenGL.GL import *


# creating a compiler for our shader that takes in a shader type (vertex or fragment shader) and shader source aka
# strings of shader code
def compile_shader(shader_type, shader_source):
    shader_id = glCreateShader(shader_type)  # allows us to reference shader later on
    glShaderSource(shader_id, shader_source)
    glCompileShader(shader_id)
    # error logic in case of mistakes
    compile_success = glGetShaderiv(shader_id, GL_COMPILE_STATUS)
    if not compile_success:
        error_message = glGetShaderInfoLog(shader_id)
        glDeleteShader(shader_id)  # taking shader out of memory if it does not compile
        raise Exception(error_message)
    return shader_id


# need to also compile the actual program
def create_program(vertex_shader_code, fragment_shader_code):
    vertex_shader_id = compile_shader(GL_VERTEX_SHADER, vertex_shader_code)
    fragment_shader_id = compile_shader(GL_FRAGMENT_SHADER, fragment_shader_code)
    program_id = glCreateProgram()
    glAttachShader(program_id, vertex_shader_id)
    glAttachShader(program_id, fragment_shader_id)
    glLinkProgram(program_id)
    # error message incase program link is unsuccessful
    link_success = glGetProgramiv(program_id, GL_LINK_STATUS)
    if not link_success:
        info = glGetProgramInfoLog(program_id)
        raise RuntimeError(info)
    glDeleteShader(vertex_shader_id)  # deletes shader from program if not linked correctly
    glDeleteShader(fragment_shader_id)
    return program_id


