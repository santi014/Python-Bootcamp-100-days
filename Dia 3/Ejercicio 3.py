print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print ("You can ride the rollercoaster")
  age = int(input("What is your age "))
  if age <= 12:
    print("Paga 5 dolares")
  elif age <= 18:
    print("Paga 7 dolares")
  else:
    print("Paga 12 dolares")
else:
  print("Sorry, you are too small") 