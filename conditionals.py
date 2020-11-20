import os
import sys

#5-1
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

os.system('pause')

#5-2
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('I wanted anchovies! Not ' + requested_topping + '!')

print("Type a number:")
answer = int(input())

if answer == 42:
    print('I see you are a man of culture, as well!')
elif answer == 69 or answer == 420:
    print("LOL FUNNEE MEEM NUMBAR XD")
else:
    print('That is incorrect. Try again.')
    print(answer)

os.system('pause')

banned_users = ['bryce', 'andrew', 'lillian4207', '1337_h4x0r']
users = 'marie'
print('Banned Users:')
print(*banned_users, sep = ", ")
print(users.title() + ' is allowed to respond.')

os.system('pause')

#extracredit
print("Enter your age:")
age = int(input())

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 30
elif age >= 65:
    price = 20


print(f"Your admission price is ${price}.")

os.system("pause")

#5-5
if age < 2:
    print("You're a baby!")
elif age > 2 and age < 4:
    print("You're a toddler!")
elif age > 4 and age < 13:
    print ("You're a kid!")
elif age > 13 and age < 20:
    print ("You're a teen!")
elif age > 20 and age < 65:
    print ("You're an adult!")
elif age > 65:
    print ("You're an elder!")

os.system('pause')

#extracredit
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms!")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni!")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese!")

print("\nFinished making your pizza!\n")
requested_toppings = []

os.system("pause")

#5-3
alien_color = 'green'

if alien_color == 'green':
    print("Green alien - 5 points!")
if alien_color == 'red':
    print("Red alien - 1 point!")

#5-4 & 5-5
alien_color = input("What color of alien did you shoot?\n")

if alien_color == 'green':
    print("You earned 5 points for shooting a green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting a yellow alien!")
elif alien_color == 'red':
    print("You earned 15 points for shooting a red alien!")
else:
    print("You sure that's an alien?")

os.system('pause')

#5-7
fav_fruits = ['pineapple', 'grape', 'cherry']

if 'cherry' in fav_fruits:
    print("You love cherries!")
if 'orange' in fav_fruits:
    print("You love oranges!")
if 'banana' in fav_fruits:
    print("You love bananas!")
if 'pineapple' in fav_fruits:
    print("You love pineapples!")
if 'blueberry' in fav_fruits:
    print("You love blueberries!")

os.system('pause')

#extracredit

available_toppings = ["green peppers", 'mushrooms', 'pepperoni', 'anchovies', 'olives', 'extra_cheese']
userInput = input("Enter your preferred pizza toppings, separated with commas.\n")
if userInput:
    requested_toppings = userInput.split(",")

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we're out of green peppers.")
        elif requested_topping in available_toppings:
            print(f"You got it, adding {requested_topping}.")
        else:
            print(f"Sorry, we don't put {requested_topping} on pizza here.")
    print("\nFinished your pizza!")
else:
    print("So, you just want a cheese pizza?")

os.system("pause")

#5-8
usernames = ["geof132", "admin", "corey_kabbage", "bigdik6969", "bluwaffl"]

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello, {username}. Please administrate wisely.")
        else:
            print(f"Hello, {username}. Please behave today on the forum.")
#5-9
else:
    print("We need to find some users!")

os.system("pause")

#5-10
current_users = ["geof132", "admin", "corey_kabbage", "bigdik6969", "bluwaffl"]
new_users = ["geof123", "luvs2spooge", "bigdik6969", "josem", "nuggetofgold12"]

for user in new_users:
    if user in current_users:
        print(f"{user} is already taken, please use a different username.")
    else:
        print(f"Welcome, {user}!")
