#Variables
my_variable = "esto es una variable"
#Imprimir en consola el valor de la variable
print(my_variable) #-> esto es una variable

my_int_variable = 10
print(my_int_variable) #-> 10

my_bool_variable = True
print(my_bool_variable) #-> True

#Concatenamos variables
print(my_variable, my_int_variable, my_bool_variable) #->Concatena los valores de las variables


#cambiamos rl tipoo de las variables
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) #-> Type Integer

#creamos variables en una misma linea
name, surname, alias, age = "jefry", "yair", "yfryxv", 20
print("me llamo", name, surname, "mi edad es de",age, "y mi alias es" , alias)

name=(input("cual es tu nombre: "))
age=(input("cual es tu edad: "))

print(name)
print(age)

#definimos una variable con un valor por defecto
my_name = "yefry"
edad = 20

print("mi nombre es", my_name, "y mi edad es", edad)
