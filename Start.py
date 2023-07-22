import os
import shutil

def pause():
	input("Naciśnij ENTER")

print('Tworzenie listy.')

index = 'input/index.json'
objects = 'input/objects'

with open(index, 'r') as file:
	content = file.read()



#    --- ROBIENIE LISTY PLIKÓW ---    #

# Usuwanie zbęnych rzeczy #1
content = content.replace('": {"hash": "', '@')
content = content.replace('", "size": ', '@')
content = content.replace('"', '')

content = content.replace("{", '')
content = content.replace("objects", '')
content = content.replace(": ", '')

# Robi pierwszą listę
content = content.split('}, ')


for a in range(len(content)):
	# dzeli na mniejsze listy
	content[a] = content[a].split('@')
	del content[a][2]

	# odaje folder w którym znajduje się plik
	content[a][1] = str(f'input/objects/{content[a][1][0:2]}/{content[a][1]}')

	# dodaje nazwę pliku na początek
	content[a].insert(0, (content[a][0].split('/'))[-1])
	content[a][0] = content[a][1].replace(content[a][0], '')

	# w sumie nie pamiętam bo mocno zmieniałem, sorry XD
	content[a][1] = str('output/' + content[a][1])
	content[a][0] = str('output/' + content[a][0])
#print(content)



#    --- KOPIOWANIE PLIKÓW I ZMIANA NAZW ---    #

print('Kopiowanie')

os.makedirs('output/')
for a in range(len(content)):
	try:
		shutil.copyfile(content[a][2], content[a][1])

	except:
		os.makedirs(content[a][0])
		shutil.copyfile(content[a][2], content[a][1])

input('Gotowe.')
