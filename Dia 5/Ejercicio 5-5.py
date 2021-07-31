#Write your code below this row 👇
for variable in range (1,101):
  if variable % 3 == 0 and variable % 5 == 0:
    print('fizzbuzz')
  elif variable % 3 == 0:
    print("fizz")
  elif variable % 5 == 0:
    print('buzz')
  else: 
    print(variable)
