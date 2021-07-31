import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cantidad_items = len(names)
numero_pagador = random.randint(0,cantidad_items-1)
nombre_persona = names[numero_pagador]
print(f"Lo siento eres {nombre_persona} te toca pagar la cuenta esta vez")