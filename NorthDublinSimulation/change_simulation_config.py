import xml.etree.ElementTree as ET
import sys
import os

'''
This code has takes in 2 arguments & has 4 functions:
INPUTS:
	Human Driven Vehicle %, Connected Autonomous Vehicle Level 2 %
FUNCTIONS:
	1. Create a new directory for the simulation outputs.
	2. Change the directory of the SSM devices output files based on the 2 input numbers in the argument.
	3. Change stats & TripInfo device output files based on the 2 input numbers in the argument.
	4. Change the HDV, CAV2 & CAV4 probability to reflect the 2 input numbers in the argument.
'''

# Get the final % penetration rate based on the other input rates
# (Convert to int, if possible, to limit decimal points)
cav4_percent = 100 - float(sys.argv[1]) - float(sys.argv[2])
if(cav4_percent.is_integer()):
	cav4_percent = int(cav4_percent)

def main():
	# Ensure input is what is expected
	if(validate_input()):
		HDVPercent = str((float(sys.argv[1]) - float(sys.argv[2]) + 15)/100)
		CAVPercent = str(float(sys.argv[2])/200)
		# File paths & lists of file names
		working_directory = "NorthDublinSection/"
		vehicle_list = ["bicycle", "bus", "motorcycle", "passenger", "pedestrian", "tram", "truck"]
		output_dir = "Results/HDV-" + HDVPercent + "_" + "CAV2-" + CAVPercent + "_" + "CAV4-" + CAVPercent + "/" 

# 1.
		# Making Results Directory
		path = working_directory + output_dir
		try: 
		    os.mkdir(path) 
		    print()
		    print("Created Directory:" + path)
		except OSError as error: 
			print("Directory already exists, will overwrite  upon simulation.")
 
# 2.
		# SUMO Config file outputs changed to new directory
		print()
		print("Changing Output Locations to:")
		xmlTree = ET.parse(working_directory + "osm.sumocfg")
		xmlRoot = xmlTree.getroot()
		xmlRoot = config_directory_swap(xmlRoot, output_dir)
		xmlTree.write(working_directory + "osm.sumocfg")

# 3.
		# Each Transport class outputs changed to new directory
		print()
		print("Changing Output Locations of:")
		for transport in vehicle_list:
			xmlTree = ET.parse(working_directory + "osm." + transport + ".trips.xml")
			xmlRoot = xmlTree.getroot()
			xmlRoot = ssm_directory_swap(xmlRoot, transport, output_dir)
			xmlTree.write(working_directory + "osm." + transport + ".trips.xml")

		# Completes all transport modes with public transport file
		xmlTree = ET.parse(working_directory + "trips.trips.xml")
		xmlRoot = xmlTree.getroot()
		xmlRoot = ssm_directory_swap(xmlRoot, "trips", output_dir)
		xmlTree.write(working_directory + "trips.trips.xml")

# 4.
		# Change the probability of HDVs & CAVs
		print()
		print("Changing Probabilities of:")
		xmlTree = ET.parse(working_directory + "osm.passenger.trips.xml")
		xmlRoot = xmlTree.getroot()
		xmlRoot = change_cav_probabilities(xmlRoot)
		xmlTree.write(working_directory + "osm.passenger.trips.xml")

	else:
		print("INVALID INPUT")
		print("PLEASE ENTER IN % MAKEUP OF SIMULATION")
		print("HDV % CAV2 %, eg. 90 5")


# Checks that the argument input is equal to 3 and made up of numbers
def validate_input():
	# Ensure there are three arguments and 2 are numbers
	if(len(sys.argv) == 3):
		return (check_arg(1) and check_arg(2))
	# If any test fails, then return False
	return False 


# Checks that the indexed argument input is a number 
def check_arg(index):
	# Check the argument is numeric in nature
	return sys.argv[index].isnumeric()


# Changes the directory of the (unique tags) stats and tripinfo device output file.
def config_directory_swap(root, new_dir):

	# Using Iterator to quickly search sub trees
	for stats_out in root.iter("statistic-output"):
		# Alters the output file to the new directory for the simulation statistics.
		stats_out.set("value", new_dir + "stats.xml")

	# Using Iterator to quickly search sub trees
	for trips_out in root.iter("tripinfo-output"):
		# Alters the output file to the new directory for the tripinfo results.
		trips_out.set("value", "tripinfo" + sys.argv[2] + ".xml")

	print("New TripInfo & Stats outputs: " + new_dir + "tripinfo.xml & " + new_dir + "stats.xml")
	# Returns the edited root.
	return root


# Changes the directory of the SSM output file for the given vehicle type.
def ssm_directory_swap(root, transport_type, new_dir):

	# Cycle through all vehicles defined in file.
	for vehicle_class in root.findall("vType"):

		# Looks for the ssm file parameter.
		print(vehicle_class.get("id"))
		for parameter in vehicle_class.iter("param"):
			key = parameter.get("key")
			if (key == "device.ssm.file"):

				# Applies different naming structure to output files depending on vehicle id.
				vehicle_id = vehicle_class.get("id")
				if(vehicle_id == "HDV" or vehicle_id == "CAV2" or 
					vehicle_id == "CAV2" or vehicle_id == "pt_tram" or vehicle_id == "pt_bus"):
					file_output = new_dir + "ssm_" + vehicle_id + ".xml"
				else:
					file_output = new_dir + "ssm_" + transport_type + ".xml"

				# Alters the output file to the new directory for this vehicle.
				parameter.set("value", file_output)

	# Returns the edited root.
	return root


# Changes the makeup of autonomous vehicle probability based on arguments
def change_cav_probabilities(root):

	# Cycle through all vehicles defined in file.
	for vehicle_class in root.findall("vType"):

		# Looks for the car ID.
		car_id = vehicle_class.get("id")
		print(car_id)

		# print((float(sys.argv[1]) - float(sys.argv[2]) + 15)/100)

		# Assign probabilities to vehicle classes based on argument
		if (car_id == "HDC"):
			vehicle_class.set("probability", str((float(sys.argv[1]) - float(sys.argv[2]) + 15)/100))
		elif (car_id == "CAV2"):
			vehicle_class.set("probability", str(float(sys.argv[2])/200))
		elif (car_id == "CAV4"):
			vehicle_class.set("probability", str(float(sys.argv[2])/200))
		else:
			print("Error in assigning probabilities")

	# Returns the edited root
	return root



if __name__== "__main__":
	main()