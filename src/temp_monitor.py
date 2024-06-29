# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import busio
from adafruit_ht16k33 import segments
from w1thermsensor import W1ThermSensor, Unit, Sensor

from .email_helper import send_email_notification

if __name__ == '__main__':
    min_temperature_threshold = 68
    max_temperature_threshold = 80

    readings = []
    num_readings_req = 5

    # Create the I2C interface.
    i2c = busio.I2C(board.SCL, board.SDA)

    # Initialize temp sensor
    sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="00000fdf38f3")

    # Gets the temperature in F
    for _ in range(num_readings_req):
        temp_f = sensor.get_temperature(Unit.DEGREES_F)
        readings.append(temp_f)

    avg_temp = sum(readings) / len(readings)

    # Create the LED segment class.
    # This creates a 7 segment 4 character display:
    display = segments.Seg7x4(i2c)
    display.brightness = 0.25

    display.print('{:.1f}F'.format(avg_temp))

    if avg_temp < min_temperature_threshold or avg_temp > max_temperature_threshold:
        pass
        #send_email_notification()
