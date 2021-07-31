# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_float = float(height)
print(type(height_float))
weight_int = int(weight)
print(type(weight_int))
# Formula es 
#(PESO/(ALTURA **2)
bmi = (weight_int/(height_float ** 2))
print ("El indice de masa corporal es", bmi)







