# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_2lowercase = name1.lower() +" " + name2.lower()
print (names_2lowercase)
T =names_2lowercase.count("t")
R =names_2lowercase.count("r")
U =names_2lowercase.count("u")
E =names_2lowercase.count("e")
true = T + R + U + E
L =names_2lowercase.count("l")
O =names_2lowercase.count("o")
V =names_2lowercase.count("v")
R =names_2lowercase.count("e")
love = L + O + V + E
true_love =str(true)+ str(love)
true_love_int =int(true_love)
print(true_love_int)
if true_love_int < 10 and true_love_int > 90:
  print(f"Tu puntaje es {true_love_int}, se llevan como la coca cola y el mentos")
elif true_love_int >= 40 and true_love_int <=60:
  print(f"Tu puntaje es {true_love_int}, se llevan bien")
else:
  print(f"Tu puntaje es {true_love_int} ")