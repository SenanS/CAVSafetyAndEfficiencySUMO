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
# cav4_percent = 100 - float(sys.argv[1]) - float(sys.argv[2])
# if(cav4_percent.is_integer()):
# 	cav4_percent = int(cav4_percent)

def main():
	# Ensure input is what is expected
	# File paths & lists of file names
	# working_directory = "/"
	vehicle_list = ["bicycle", "bus", "motorcycle", "passenger", "pedestrian", "tram", "truck", "CAV2", "CAV4"]
	# output_dir = "Results/HDV-" + HDVPercent + "_" + "CAV2-" + CAVPercent + "_" + "CAV4-" + CAVPercent + "/" 

	with open('SSM' +sys.argv[1]+ '.xml', 'w') as f:
		xmlShrub.write(f, encoding='unicode')
		log_loc = xmlShrub.Element('SSMLog')

		
		# print("Changing Output Locations of:")
		for transport in vehicle_list:
			xmlTree = ET.parse(working_directory + "ssm_" + transport + ".xml")
			xmlRoot = xmlTree.getroot()
			# xmlRoot = ssm_directory_swap(xmlRoot, transport, output_dir)
			# xmlTree.write(working_directory + "osm." + transport + ".trips.xml")
			for SSM in xmlRoot.findall("SSMLog"):
				for conflicts in SSM.findall("SSMLog"):
					conflict_found = False;
					for TTC in conflicts.iter("minTTC"):
						value = TTC.get("value")
						if(value == "111")
							conflict_found = True
					for PET in conflicts.iter("PET"):
						value = PET.get("value")
						if(value == "111")
							conflict_found = True
					if(conflict_found == True):
						log_loc.insert(-1, conflicts)



		# Completes all transport modes with public transport file
		# xmlTree = ET.parse(working_directory + "trips.trips.xml")
		# xmlRoot = xmlTree.getroot()
		# xmlRoot = ssm_directory_swap(xmlRoot, "trips", output_dir)
		# xmlTree.write(working_directory + "trips.trips.xml")




if __name__== "__main__":
	main()