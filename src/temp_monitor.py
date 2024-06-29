# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import busio
from adafruit_ht16k33 import segments
from w1thermsensor import W1ThermSensor, Unit, Sensor

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize temp sensor
sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="00000fdf38f3")

# Gets the temperature in F
temp_f = sensor.get_temperature(Unit.DEGREES_F)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
display.brightness = 0.25
#display.colon(turn_on=False)
#display[4] = 'F'

display.print('{:.1f}F'.format(temp_f))
#display.marquee('123456789 ')

# Clear the display.
#display.fill(0)

# Can just print a number
#display.print(42)
#time.sleep(1)

# Set the first character to '1':
#display[0] = '1'
# Set the second character to '2':
#display[1] = '2'
# Set the third character to 'A':
#display[2] = 'A'
# Set the forth character to 'B':
#display[3] = 'B'
#time.sleep(1)

#numbers = [0.0, 1.0, 0.55, 10.23, 100.5]

# print floating point numbers
#for i in numbers:
#    display.print(str(i))
#    time.sleep(0.5)

# print hex values, enable colon
#for i in range(0xFF):
#    display.fill(0)
#    display.print(':')
#    display.print(hex(i))
#    time.sleep(0.25)
