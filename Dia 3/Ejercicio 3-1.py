# 🚨 Don't change the code below 👇
altura = float(input("Altura en m: "))
peso = float(input("Peso en kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = peso / (altura*altura)
print (round(BMI,2))
if BMI < 18.5:
  print("Tu BMI es {:.2f}, tienes peso por debajo de la media".format(round(BMI,2)))
elif BMI > 18.5 and BMI < 25:
  print(f"Tu BMI es {BMI:.2f}, tienes peso normal")
elif BMI > 25 and BMI < 30:
  print("Tu BMI es {:.2f}, tienes sobrepeso".format(round(BMI,2)))
elif BMI > 30 and BMI < 35:
  print("Tu BMI es {:.2f}, tienes obesidad".format(round(BMI,2)))
else:
  print("Obesidad clinica")