import random

num_a_deviner = random.randint(1,50) 
number_recu = int(input("Salut, Le jeux consiste a deviner un nombre entre 0 et 50 en 5 essays.\nDevine un nombre: "))

stop = False;
count = 1

while not(stop):
	count +=1
	if number_recu > num_a_deviner:
		number_recu = int(input("Le nombre est plus petit.\nDevine de nouveau le nombre: "))
	elif number_recu < num_a_deviner:
		number_recu = int(input("Le nombre est plus grand.\nDevine de nouveau le nombre: "))
	else:
		print("Felicitation, Vous avez gagne apres ", count, "essays!!! ... Le Nombre est: ", num_a_deviner)
		stop = True

	if count == 5:
		stop = True
		print("Vous avez Perdu apres 5 essays.\nLe Nombre est: ", num_a_deviner)
		break;

print("Fin du jeu, Merci!!!")




