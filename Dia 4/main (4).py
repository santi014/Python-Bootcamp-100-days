import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista_imagenes = [rock,paper,scissors]

user_choice = int(input("Seccionar 0 para roca, 1 para papel, 2 para tijeras: "))
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
else:
  print(lista_imagenes[user_choice])
  print("La computadora selecciono")
  computer_choice = random.randint(0,2)
  print(lista_imagenes[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")
    