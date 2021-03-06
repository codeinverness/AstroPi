# Added heading to dataset

#Import Libraries
import datetime
from sense_hat import SenseHat

# Settings
timestamp = datetime.datetime.now()
FILENAME = ""
write_frequency = 50

# Store data until written to file
def log_data():
	output_string = ",".join(str(value) for value in sense_data)
	batch_data.append(output_string)

def file_setup(filename):
	header = ["temp_h","temp_p","Humidity","Pressure","Pitch","Roll","Yaw","Mag_X","Mag_Y","Mag_Z","Accel_X","Accel_Y","Accel_Z","Gyro_X","Gyro_Y","Gyro_Z","Timestamp"]
	with open(filename,"w") as f:
		f.write(",".join(str(value) for value in header)+ "/n")

# Function that checks each enviroment sensor
def get_sense_data():
	sense_data=[]
	sense_data.append(sense.get_temperature_from_humidity())
	sense_data.append(sense.get_temperature_from_pressure())
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

	sense_data.append(timestamp)
	return sense_data

# Program
sense = SenseHat()

batch_data = []

if FILENAME == "":
	filename = "SenseLog-" + str(timestamp)+".csv"
else:
	filename = FILENAME+"-"+str(timestamp)+".csv"

file_setup(filename)

while True:
	sense_data = get_sense_data()
	print(sense_data)
