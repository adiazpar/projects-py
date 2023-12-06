import pygame as pg
from matrix_functions import *
from numba import njit


@njit(fastmath=True)
def any_func(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object3D:
    # Constructor of an object of type "object":
    def __init__(self, render, vertexes='', faces=''):
        self.render = render

        # Vertices are often defined as Homogeneous coordinates, which means:
        # v = (x, y, z, w), where w = 1. I'm not sure what value w represents in this case,
        # so I must research...
        self.vertexes = np.array(vertexes)

        # Faces are created by receiving a list of vertices in a certain order that will define the face.
        # For example, in a 3D system, we define 4 vertices to form the face of a cube:
        #
        #          1 * ----- * 2        - A face will be defined as 1 -> 2 -> 4 -> 3
        #            |       |          - Thus, the vertex index in the array is designated to the vertex
        #            |       |            number in the figure! v[1] -> v[2] -> v[4] -> v[3]
        #          3 * ----- * 4
        #
        # The key takeaway is the relationship between vertices and faces, refer to the tutorial for help...

        self.faces = faces

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color('orange'), face) for face in self.faces]
        self.movement_flag, self.draw_vertexes = False, False
        self.label = ''

    # For a more flexible programming structure, draw the object through a general drawing method:
    def draw(self):
        self.screen_projection()
        self.movement()

    # DEMO Rotate the object around a chosen axis for demonstration:
    def movement(self):
        if self.movement_flag:
            #self.rotate_x(-(pg.time.get_ticks() % 0.005))
            self.rotate_y(-(pg.time.get_ticks() % 0.005))
            # self.rotate_z(-(pg.time.get_ticks() % 0.005))

    # One of the most important methods for rendering objects:
    def screen_projection(self):
        # Transfer vertices of object into camera space:
        vertexes = self.vertexes @ self.render.camera.camera_matrix()

        # Using the projection matrix, transfer the vertices into clip space:
        vertexes = vertexes @ self.render.projection.projection_matrix

        # Normalize each vertex of the object in clip space by dividing each component by w, this way, w = 1:
        vertexes /= vertexes[:, -1].reshape(-1, 1)

        # It is necessary to cut off vertices >1 and < -1 because such coordinates
        # will not fit into the visible area of the screen:
        # Therefore, it is not necessary to draw faces with such values:
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0

        # After all the above transformations, the vertices will now be in the normalized clipping space.
        # However, we need to somehow display these coordinates on our screen coordinates (Where (0, 0) is at top left)
        # The below function will transfer the coordinates of the object's vertices according to screen resolution:
        vertexes = vertexes @ self.render.projection.to_screen_matrix

        # Take a slize of the (x, y, z, w) coordinates to just use the (x, y) components for the screen:
        vertexes = vertexes[:, :2]

        # Iterate over all the faces of the object and get the necessary vertices to display the desired face:
        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertexes[face]

            # Make the decision to draw a face based on the cut-off vertices that have taken a 0 value above:
            if not any_func(polygon, self.render.H_WIDTH, self.render.H_HEIGHT):
                # After applying the last matrix, the position of such vertices will be equal
                # to the middle of the screen:

                # If there aren't any 0 value vertices included in the current face, then draw the face:
                pg.draw.polygon(self.render.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])

        # Draws the vertices if the draw_vertexes boolean is set to true in the constructor:
        if self.draw_vertexes:

            # Draw the vertices of the object according to the same principle defined above:
            for vertex in vertexes:
                if not any_func(vertex, self.render.H_WIDTH, self.render.H_HEIGHT):
                    pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 2)

    # Method to translate the object's array of vertices by multiplying the array by the
    # translation matrix defined in matrix_functions file, given a position pos.
    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    # Method to scale the object's size by multiplying its array of vertices by the
    # scaling matrix defined in matrix_functions file, given a scalar to scale to.
    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)

    # Method to rotate the object's vertices around the x-axis by multiplying the
    # respective rotation matrix in the matrix_functions file, given an angle to rotate to.
    def rotate_x(self, angle):
        self.vertexes = self.vertexes @ rotate_x(angle)

    # Method to rotate the object's vertices around the y-axis by multiplying the
    # respective rotation matrix in the matrix_functions file, given an angle to rotate to.
    def rotate_y(self, angle):
        self.vertexes = self.vertexes @ rotate_y(angle)

    # Method to rotate the object's vertices around the z-axis by multiplying the
    # respective rotation matrix in the matrix_functions file, given an angle to rotate to.
    def rotate_z(self, angle):
        self.vertexes = self.vertexes @ rotate_z(angle)

# The above methods work well because we make use of the numpy library, which gives us the ability to
# multiply an entire array of values by a matrix easily...


# This method is used to create an Axes object (World or Local):
class Axes(Object3D):
    def __init__(self, render):
        super().__init__(render)
        self.vertexes = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertexes = False
        self.label = 'XYZ'