import math
import numpy as np

"""
The Perspective Matrix:
This matrix is used to take theoretical vertices in 3D space and project them locally into the near plane.
We use this method in computer graphics to transform 3D shapes into 2D space...

Think of this:

        *  + +  *
      +       + +  
    *  + +  *   +
    +       +   *
    +       + +
    *  + +  *  
    
Imagine this cube in 3D space. Obviously your computer screen can't reach into 3D space, since
graphics are being rendered on a flat screen. Projection matrices are meant to simulate the illusion
of a 3D object on a 2D screen by taking all vertices defined by a shape and plastering them
onto the view screen...
"""


class Projection:
    def __init__(self, render):
        # Take necessary values for the formation of the projection matrix from an instance of the camera class:
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane

        RIGHT = math.tan(render.camera.h_fov / 2)   # Use the FOV value to calculate right bound
        LEFT = -RIGHT

        TOP = math.tan(render.camera.v_fov / 2)     # Use the FOV value to calculate the top bound
        BOTTOM = -TOP

        # Predetermined elements of the projection matrix:
        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR + NEAR) / (FAR - NEAR)
        m32 = -2 * NEAR * FAR / (FAR - NEAR)

        # Forming the projection matrix for use as a perspective matrix component:
        self.projection_matrix = np.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        # Matrix used to transform object's coordinates to screen resolution:
        HW, HH = render.H_WIDTH, render.H_HEIGHT
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0],
            [0, -HH, 0, 0],
            [0, 0, 1, 0],
            [HW, HH, 0, 1]
        ])
