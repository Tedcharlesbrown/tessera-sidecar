import json
import os.path
import time

from globals import *	

test_port = 0

def get_settings():
	return settings

def setup():
	print("FINDING SETTINGS FILE")
	if (os.path.exists("settings.json")):
		print("SETTINGS FILE FOUND")
		# Opening JSON file
		with open('settings.json', 'r') as openfile:
			# Reading from json file
			json_object = json.load(openfile)
			# parseSettings(json_object)
			for ID in range(len(json_object)):
				if "PROCESSOR" in json_object[ID]:
					processor_array[json_object[ID].get("PROCESSOR")] = json_object[ID]
				else:
					global settings
					global test_port
					settings = json_object[ID]
					test_port = json_object[ID].get("COMPANION IP")
	else:
		print("NO SETTINGS FILE, CREATING ONE")
		# add setting to json
		processor_array.insert(0,settings)
		# Serializing json
		json_object = json.dumps(processor_array, indent=4)
		# Writing to sample.json
		with open("settings.json", "w") as outfile:
			outfile.write(json_object)


# if (os.path.exists("settings.json")):
# 	print("SETTINGS FILE FOUND")
# 	# Opening JSON file
# 	with open('settings.json', 'r') as openfile:
# 		# Reading from json file
# 		json_object = json.load(openfile)
# 		# parseSettings(json_object)
# 		for ID in range(len(json_object)):
# 			if "PROCESSOR" in json_object[ID]:
# 				processor_array[json_object[ID].get("PROCESSOR")] = json_object[ID]
# 			else:
# 				updateSettings(json_object)

# else:
# 	print("NO SETTINGS FILE, CREATING ONEe")
# 	# add setting to json
# 	processor_array.insert(0,settings)
# 	# Serializing json
# 	json_object = json.dumps(processor_array, indent=4)
# 	# Writing to sample.json
# 	with open("settings.json", "w") as outfile:
# 		outfile.write(json_object)





