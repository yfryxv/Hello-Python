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

### desempaquetado de caracteres ###
lenguaje = "Python"
a,b,c,d,e,f=lenguaje
print(a)  # Imprime la primera letra de la cadena
print(b)  # Imprime la segunda letra de la cadena   
print(c)  # Imprime la tercera letra de la cadena
print(d)  # Imprime la cuarta letra de la cadena           
print(e)  # Imprime la quinta letra de la cadena
print(f)  # Imprime la sexta letra de la cadena

### Divicion
lenguaje_slice = lenguaje[1:3]
print(lenguaje_slice) # Imprime una parte de la cadena (desde el índice 1 hasta el 3, sin incluir el 3)

lenguaje_reves = lenguaje[::-1]
print(lenguaje_reves)  # Imprime la cadena al revés

print(lenguaje.capitalize())  # Capitaliza la primera letra de la cadena
print(lenguaje.upper())  # Convierte toda la cadena a mayúsculas
print(lenguaje.lower())  # Convierte toda la cadena a minúsculas    
print(lenguaje.count("o"))  # Cuenta cuántas veces aparece la letra "o" en la cadena
print(lenguaje.find("P"))  # Encuentra la posición de la letra "P" en la cadena
print(lenguaje.replace("P", "J"))  # Reemplaza la letra "P" por "J" en la cadena
print(lenguaje.startswith("P"))  # Verifica si la cadena comienza con "P"
print(lenguaje.endswith("n"))  # Verifica si la cadena termina con "n"
print(lenguaje.split("t"))  # Divide la cadena en una lista usando "t" como separador
print(lenguaje.isnumeric())  # Verifica si la cadena es numérica (False en este caso)
print(lenguaje.isalpha())  # Verifica si la cadena contiene solo letras (True en este caso)
print(lenguaje.isalnum())  # Verifica si la cadena es alfanumérica (True en este caso)
print(lenguaje.isspace())  # Verifica si la cadena contiene solo espacios (False en este caso)
print(lenguaje.index("y"))  # Encuentra la posición de la letra "y" en la cadena

