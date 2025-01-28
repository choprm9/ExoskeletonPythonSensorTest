import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import time
import board
import busio
import adafruit_bno055

# A cube to represent the sensor
vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

i2c = board.I2C()

sensor = adafruit_bno055.BNO055_I2C(i2c,0x29)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialize OpenGL
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Replace this with real sensor data later
    yaw, pitch, roll = sensor.euler

    while True:
        calib_status = sensor.calibration_status
        print(f"System: {calib_status[0]}, Gyro: {calib_status[1]}, Accel: {calib_status[2]}, Mag: {calib_status[3]}")
        euler = sensor.euler
        if euler[0] != None and euler[1] != None and euler[2] != None: 
            yaw, pitch, roll = sensor.euler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply rotations (replace with real sensor data)
        glPushMatrix()
        glRotatef(float(yaw), 0, 1, 0)   # Yaw (around Y-axis)
        glRotatef(float(pitch), 1, 0, 0) # Pitch (around X-axis)
        glRotatef(float(roll), 0, 0, 1)  # Roll (around Z-axis)

        draw_cube()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(100)

if __name__ == "__main__":
    main()
