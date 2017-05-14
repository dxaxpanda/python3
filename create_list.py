from sys import argv
import string

script, input_file, output_file = argv
array = []

# ouverture du fichier et affectation à une variable. le mode 'a+' écrit a la fin
treatment_file = open(output_file, 'a+')

# façon safe d'ouvrir un fichier, le referme automatiquement
with open(input_file, 'r') as ins:
	#array = []

	# loop de chaque ligne du fichier et ajout à la liste array
	for line in ins:
		print(f"Adding item {line} to the list ")
		# suppression de tout whitespace de la ligne
		line = line.strip()
		# ajout de la ligne à la liste
		array.append(line)
	#[w.strip() for w in array]
	#list(map(str.split, array))

	# récupération de la liste array
	print(f"This is our array: {array}")

	# loop de chaque objet de la liste
	for item in array:
		print(f"Writing {item} to the {treatment_file}")
		#treatment_file.write("{}\n".format(item)) ## add new line
		# ecriture vers le fichier ouvert à traiter avec le format suivant "'{}',"
		# où {} est un objet de la liste
		treatment_file.write("{} ".format(item))
