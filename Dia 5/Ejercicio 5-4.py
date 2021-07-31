#Write your code below this row 👇
total = 0 
for new_variable in range (2,101,2):
  total +=new_variable
print(f'La suma de los numeros pares son {total}')

#Alternativa 
total = 0
for new_variable in range(1,101):
  if new_variable % 2 == 0:
    total +=new_variable
print(f"La suma de los numeros pares en total es {total}")
