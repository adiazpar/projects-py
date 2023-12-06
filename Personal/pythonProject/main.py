from object_3d import *
from camera import *
from projection import *
import pygame as pg

"""
https://www.youtube.com/@CoderSpaceChannel

Coder Space is a very talented programmer who implements various graphics techniques 
& other projects in Python. I have been following them for years, and I highly 
recommend checking out their channel.

THE GRAPHICS PIPELINE:
For my DEMO1, I have decided to follow a tutorial for creating a basic graphics engine in Python by Coder Space.
Following his demonstration from the video, I deduced my own conclusion on how some methods work, and have
provided my own comments explaining how this program operates.

I spent a considerable amount of time writing this code from scratch, and listening to Coder Space's lectures.
I chose to create my project this way so I can better understand the concepts of computer graphics.

I found consistency with these concepts with Dr. Semwal's lectures and the CS4800 book.

-----------------------------------------------------------------------------------------------------------------
Python is a very limited programming language for rendering graphics...

What did I learn from this project?
    - Camera perspective matrix, M = [TRANSLATION @ ROTATION @ PROJECTION]
    - Forward, Up, Right vectors for camera view direction
    - Camera FOV & 
    - Linear transformations in code, translate, rotate, scale to manipulate vertices
    - How object vertices are transferred from normalized local space to screen resolution
    - Reading from OBJ file to create vertices and faces
    - Rendering vertices and faces to screen
    - Basic coordinate system for world and local
    - The difference between world and local coordinates
    
What I want to learn in the future:
    - View frustum culling in 3D, how to use the near and far plane...
    - Disable rendering vertices / faces that are covered by other vertices / faces above them...
    - The above is known as 'Occlusion culling', maybe use ray-cast, z-buffer algorithm, etc...

View Frustrum Culling resrouces:
https://www.reddit.com/r/GraphicsProgramming/comments/16eq4lw/i_am_trying_to_make_a_3d_renderer_for_the_first/
https://en.wikipedia.org/wiki/Viewing_frustum
http://www.lighthouse3d.com/tutorials/view-frustum-culling/

Occlusion Culling resources:
https://docs.panda3d.org/1.10/python/programming/render-attributes/occlusion-culling/index
https://github.com/rkibria/pyrasterize

"""


class SoftwareRender:

    # This is the constructor!
    # Define standard objects from pygame such as window resolution, drawing surface,
    # and desired frames per second:
    def __init__(self):
        # This initializes all imported pygame modules
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1280, 720  # This is a tuple, the aspect ratio 1280, 720
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)     # I dont understand this
        self.clock = pg.time.Clock()                    # The clock object helps track time
        self.create_objects()

    # In this method, we create an object instance which is called from the constructor
    # in main (__init__)
    def create_objects(self):
        # Creating an instance of the camera class and set an initial position:
        self.camera = Camera(self, [-5, -5, 50])

        # Creating an instance of the projection class for rendering use:
        self.projection = Projection(self)

        # Drawing world axes:
        self.axes = Axes(self)
        self.axes.scale(5)
        self.axes.translate([0.0001, 0.0001, 0.0001])

        # Drawing local axes:
        self.local_axes = Axes(self)
        self.local_axes.translate([2, 2, 2])
        self.local_axes.movement_flag = False

        self.object = self.get_object_from_file('resources/t_34_obj.obj')
        # self.object = self.get_object_from_file('resources/Lowpoly_tree_sample.obj')
        # self.object = self.get_object_from_file('resources/tablefloor.obj')
        #self.object = self.get_object_from_file('resources/hand.OBJ')

        # DEMO:
        self.object.scale(1)
        self.object.rotate_y(-math.pi / 4)
        self.object.translate([2, 2, 2])
        self.object.movement_flag = True

    # Function to read OBJ file format to create vertex and face array data for rendering:
    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    # Performs the entire rendering, paints the entire surface with desired color:
    def draw(self):
        self.screen.fill(pg.Color('black'))

        # Call the object's draw method for screen projection and movement (defined in object_3d class):
        self.object.draw()
        self.axes.draw()

        if self.local_axes.movement_flag == True:
            self.local_axes.draw()     # DEMO purposes

    # The main program loop that calls the method for drawing objects:
    def run(self):
        while True:
            self.draw()
            self.camera.control()

            # Checks for exit of application:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption("FPS: " + str(int(self.clock.get_fps())))
            pg.display.flip()               # Updates full display surface to screen
            self.clock.tick(self.FPS)       # In milliseconds to update the clock


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()

"""
3D SYSTEM BASICS:
The world coordinate system can be interpreted as the "scene" coordinate system.
It uses a Left-handed Coordinate System, with:
    - positive x-axis pointing right, 
    - positive y-axis pointing upwards,
    - positive z-axis pointing into the screen
    
    Y
    |                 *d
    |  *a        Z
    |         +
    |      +              *c
    |   +       *b
    |_________________ X
    
Objects in space are defined by points in the 3D space, which are called "vertices".
These points are roughly illustrated in the drawing above, as you can see point a, b, c, d...

Each vertex has corresponding coordinates, with each one of the form (x1, y1, z1), and so on.
By connecting these vertices, we get a representation of an object in 3D space, with all respective connections
forming a "face" of an object.

EACH OBJECT has its own coordinate system known as the "LOCAL" coordinate system
The local system is in charge of things such as movement, and rotation.
    
    - If we want to move an object for example, we need to somehow transform its local
      coordinates to world coordinates.
    
    - Essentially, any actions done to an object must transform local coordinates to world coordinates.
"""

"""
3D OBJECT ACTIONS:
The main actions that can be done on a 3D object are as follows:
    - Moving
    - Rotating
    - Scaling
    - Shift
    
Almost any change to a vertex in space is carried out by multiplying the given vertices of  
an object by a matrix defined by the specific action.
    - Translation Matrix
    - Rotation Matrix
    - Scaling Matrix
"""
