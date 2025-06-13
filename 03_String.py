### String ###
my_string = "Hola, soy un string"
my_new_string = "y estoy aprendiendo Python"

print(len(my_string))  # Imprime el string original
print(len(my_new_string))  # Imprime el nuevo string 

print(my_string + " " + my_new_string)  # Concatena los dos strings

### formateo ###

name, surname, age = "jefry", "yair", 20
print("Me llamo {} {} y tengo {} años" .format(name, surname, age))
print(f"Me llamo %s %s y tengo %d años" %(name, surname, age))
print(f"Me llamo {name} {surname} y tengo {age} años")  # Usando f-strings
print("Me llamo {0} {1} y tengo {2} años".format(name, surname, age))  # Usando format



