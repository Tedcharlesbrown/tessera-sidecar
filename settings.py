import json
import os.path
import time

from globals import *


if (os.path.exists("settings.json")):
	# Opening JSON file
	with open('settings.json', 'r') as openfile:
		# Reading from json file
		json_object = json.load(openfile)
		# parseSettings(json_object)
		for ID in range(len(json_object)):
			if "PROCESSOR" in json_object[ID]:
				processor_array[json_object[ID].get("PROCESSOR")] = json_object[ID]
			else:
				settings = json_object[ID]

else:
	# add setting to json
	processor_array.insert(0,settings)
	# Serializing json
	json_object = json.dumps(processor_array, indent=4)
	# Writing to sample.json
	with open("settings.json", "w") as outfile:
		outfile.write(json_object)





