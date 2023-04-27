#importing the module
import json

#opening JSON file
#from the same location as the python script
with open('new.json') as json_file:
	data = json.load(json_file)

#This prints the type of the data - this shows that it is a dict
print("Type:", type(data))

#This next section goes through in a randon order of the file and 
#pulls keys and values from the different sections.

for i in data['phoneNumbers']:
	print("----------------------------")
	print("Contact Number Type (Home or Mobile):", i['type'])
	print("number:", i['number'])


for x in data['address']:
	print("No:", x['streetAddress'])
	print("City:", x['city'])
	print("State:", x['state'])
	print("ZIP Code:", x['postalCode'])

for y in data['employee']:
	print("---------------------------")
	print("Forename:", y['firstName'])
	print("Surname:", y['lastName'])
	print("Gender:", y['gender'])


