import pygame as pg
from matrix_functions import *


class Camera:

    # Constructor for a camera object, receives 'redner' and 'position' arguments:
    # ? I'm not 100% sure what render is yet, but it looks like it is just refers to the
    # software renderer in main...
    def __init__(self, render, position):

        self.render = render

        self.width = render.WIDTH
        self.height = render.HEIGHT

        self.position = np.array([*position, 1.0])      # Supply the initial camera spawn positions for the scene
        self.forward = np.array([0, 0, 1, 1])           # Orientation vector camera forward, normalized
        self.up = np.array([0, 1, 0, 1])                # Orientation vector camera upwards, normalized
        self.right = np.array([1, 0, 0, 1])             # Orientation vector camera right, normalized

        self.h_fov = 90 * math.pi / 180    # Converts 90 degrees to radians using pi/180
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)

        # MUST IMPLEMENT !!!!!!!!!!!
        self.near_plane = 0.1           # Setting the distance of the near plane for view frustum
        self.far_plane = 100            # Setting the distance of the far plane for view frustum
        # MUST IMPLEMENT !!!!!!!!!!!

        self.moving_speed = 0.3
        self.rotation_speed_x = 0.015
        self.rotation_speed_y = 0.010

        self.anglePitch = 0
        self.angleYaw = 0

    # How do I access these values within the class? I need to practice doing so...
    # In any def, variable = self.access_attribute

    def control(self):
        key = pg.key.get_pressed()

        # Adding my own mouse movement:
        if not key[pg.K_q]:
            # Mouse cursor is invisible during runtime!
            pg.mouse.set_visible(0)

            # Sets mouse to the middle of the screen:
            pg.mouse.set_pos(pg.display.get_window_size()[0]/2, pg.display.get_window_size()[1]/2)
            # Tuple dx, dy gets mouse relative movements to multiply camera rotation later:
            dx, dy = pg.mouse.get_rel()
        else:
            pg.mouse.set_visible(1)
            dx, dy = pg.mouse.get_rel()[0]*0, pg.mouse.get_rel()[1]*0

        # Camera movements:
        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += self.forward * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.forward * self.moving_speed
        if key[pg.K_SPACE]:
            self.position += self.up * self.moving_speed
        if key[pg.K_LSHIFT]:
            self.position -= self.up * self.moving_speed

        # Camera rotations:
        self.camera_yaw(self.rotation_speed_x * -dx/3)
        # dx is negated to convert relative screen movement values to the camera coordinate system, which
        # has a right-hand coordinate system (opposite of left hand described in main). The same applies for dy...

        self.camera_pitch(self.rotation_speed_y * -dy/3)

    # Rotate the camera yaw:
    def camera_yaw(self, angle):
        self.angleYaw += angle

    # Rotate the camera pitch:
    def camera_pitch(self, angle):
        self.anglePitch += angle

    def axisIdentity(self):
        self.forward = np.array([0, 0, -1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])

    def camera_update_axis(self):
        rotate = rotate_x(self.anglePitch) @ rotate_y(self.angleYaw)
        self.axisIdentity()
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    # Translate function component for perspective matrix:
    def translate_matrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    # Rotate function component for perspective matrix:
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    # Multiplying the first two camera components of the perspective matrix:
    def camera_matrix(self):
        self.camera_update_axis()
        return self.translate_matrix() @ self.rotate_matrix()


"""
CS4800 NOTES:
- The near plane has the equation c = -m/f. This will be a negative value...
- I'm not quite sure what the definitions for m or f are, but I should ask Dr. Semwal...
- I believe that the point for the corresponding red square: (-c, -c, c)
"""
