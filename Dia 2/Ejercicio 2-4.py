#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
cuenta_costo= float(input("Cuanto es la cuenta total : "))
print(type(cuenta_costo))
propina = int(input(("Cuanto es el porcentaje de propina que se desea dar ")))
cantidad_personas = int(input("Cuantas personas son: "))
propina_porcentaje = propina / 100
propina_total = cuenta_costo * propina_porcentaje
cuenta_total = cuenta_costo + propina_total
#Importante la sintaxis para limitar valores es "{:.2f}".format(numero x)
print("La cuenta total es {:.2f} ".format(cuenta_total))
cuenta_percapita = cuenta_total / cantidad_personas
resultado = "{:.2f}".format(cuenta_percapita)
print (f"El monto que de debe de pagar por persona es  {resultado}")