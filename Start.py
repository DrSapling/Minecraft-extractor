import os
import shutil

def pause():
	input("Press ENTER")

print('Creating a list.')

index = 'input/index.json'
objects = 'input/objects'

with open(index, 'r') as file:
	content = file.read()



#    --- CREATING A LIST OF FILES ---    #

# Removing meaningless stuff
content = content.replace('": {"hash": "', '@')
content = content.replace('", "size": ', '@')
content = content.replace('"', '')

content = content.replace("{", '')
content = content.replace("objects", '')
content = content.replace(": ", '')

# Creating the first list
content = content.split('}, ')


for a in range(len(content)):
	# Dividing into smaller lists
	content[a] = content[a].split('@')
	del content[a][2]

	# Creates a path of directory with file
	content[a][1] = str(f'input/objects/{content[a][1][0:2]}/{content[a][1]}')

	# Adds the name of a file at the beginnging
	content[a].insert(0, (content[a][0].split('/'))[-1])
	content[a][0] = content[a][1].replace(content[a][0], '')

	# I do not quite remember what this does, sorry XD
	content[a][1] = str('output/' + content[a][1])
	content[a][0] = str('output/' + content[a][0])
#print(content)



#    --- COPYING FILES AND CHANGING NAMES ---    #

print('Copying')

os.makedirs('output/')
for a in range(len(content)):
	try:
		shutil.copyfile(content[a][2], content[a][1])

	except:
		os.makedirs(content[a][0])
		shutil.copyfile(content[a][2], content[a][1])

input('DONE.')
