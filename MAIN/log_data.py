# Import Libraries
import datetime
from sense_hat import SenseHat

# Settings

# Store data until written to file
def log_data():
	output_string = ",".join(str(value) for value in sense_data)
	batch_data.append(output_string)

# Function that checks each enviroment sensor
def get_sense_data():
	sense_data=[]
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_humidity())
	sense_data.append(sense.get_pressure())

	o = sense.get_orientation()
	yaw = o["yaw"]
	pitch = o["pitch"]
	roll = o["roll"]
	sense_data.extend([pitch,roll,yaw])

	mag = sense.get_compass_raw()
	mag_x = mag["x"]
	mag_y = mag["y"]
	mag_z = mag["z"]
	sense_data.extend([mag_x,mag_y,mag_z])

	acc = sense.get_accelerometer_raw()
	x = acc["x"]
	y = acc["y"]
	z = acc["z"]
	sense_data.extend([x,y,z])

	gyro = sense.get_gyroscope_raw()
	gyro_x = gyro["x"]
	gyro_y = gyro["y"]
	gyro_z = gyro["z"]
	sense_data.extend([gyro_x,gyro_y,gyro_z])

	sense_data.append(datetime.datetime.now())
	return sense_data

# Program
sense = SenseHat()

while True:
#	sense_data = get_sense_data()
	print(get_sense_data())
