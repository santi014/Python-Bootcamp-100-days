#Data Types
#Strings
print("Hello"[4])
print(123+345)
123_456_789
#Flotante
3.14159
#Boolean
True
False
#Data conversion
#Interger a String

num_char = len(input("Cual es tu nombre? "))
#Es interger
print (type(num_char))
#Se convierte a string
new_num_char = str (num_char)
print ("Tu nombre tiene " + new_num_char + " letras")
print(type(new_num_char))
print ("\n")
#Sr
a = 123
print(type(a))
a= str(123)
print(type(a))
#REGLA DE PEMDAS
#PARENTESIS
#EXPONENTE
#MULTIPLICACION
#DIVISION 
#ADICION
#SUSTRACCION

puntaje = 0
altura = 1.77
ganando = True
#f-String
#Es practico para convertir todo todo los los valores a string sin tener que ir convirtiendo 1 por 1
print(f"Tu puntaje es {puntaje},tu altura es {altura}, estas ganando? {ganando}")