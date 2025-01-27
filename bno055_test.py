import time
import board
import busio
import adafruit_bno055

i2c = board.I2C()

sensor = adafruit_bno055.BNO055_I2C(i2c,0x29) # adafruit library defaults to 0x28, but our sensor defaults to 0x29

while True:
        euler = sensor.euler
        print("---------------------------------------------------------------------")
        print("Euler")
        print(f"Heading: {euler[0]} deg, Roll: {euler[1]} deg, Pitch: {euler[2]} deg")
        print("Acceleration") # I think these need to be calibrated
        print(f"Heading: {sensor.acceleration[0]}, Roll: {sensor.acceleration[1]}, Pitch: {sensor.acceleration[2]}") 
        print(f"Temperature: {sensor.temperature}")

        time.sleep(0.5)

