from w1thermsensor import W1ThermSensor, Unit

sensor = W1ThermSensor()

temp_c = sensor.get_temperature()
temp_f = sensor.get_temperature(Unit.DEGREES_F)

print('Found temp {:.1f}C and {:.1f}F'.format(temp_c, temp_f))
