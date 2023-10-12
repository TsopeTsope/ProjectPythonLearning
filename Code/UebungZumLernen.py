liste = ['Pierre', 'Paul']
print("1- ", liste)

# Rajoute l'élément à la fin de la liste
liste.append('Jacques')
print("2- ", liste)

# Insérer un élément à une position définie dans la liste
liste.insert(0, 'Nazer')
print("3- ", liste)

# Fusionne la liste ajoutée à la liste existante
liste.extend(['Bertrand', 'John'])
print("4- ", liste)

liste += ['Camille']
print("5- ", liste)





liste = ['Pierre', 'Paul']

# Enlève l'élément 'Pierre'
liste.remove('Pierre')

# Enlève l'élément situé à l'indice 1
# Et retourne l'élément supprimé dans la variable element_enleve (ici: 'Paul')
element_enleve = liste.pop(2)

# Enlève l'élément situé à l'indice 0 (ici: 'Pierre')
del liste[0]
