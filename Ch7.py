import os
import sys
exercise = int(input("Which exercise?\n"))

if exercise == 1:
    #7-1. Rental Car
    car = input("What kind of car do you want?\n")

    print(f"I'll look into getting a {car} for you.")
elif exercise == 2:
    #7-2. Restaurant Seating
    guests = input("How many people do you plan to have for dinner?\n")
    guests = int(guests)

    if guests < 8:
        print("Very well, I'll take you to a table.")
    else:
        print("I'm sorry, it will be a bit of a wait for more than 8 people.")
elif exercise == 3:
    #7-3
    number = input("Enter a number.")
    number = int(number)

    if number % 10 == 0:
        print("This is a multiple of 10.")
    else:
        print("This isn't a multple of 10.")
elif exercise == 4:
    #7-4
    run = True
    toppings = []
    while run != False:
        topping = input("Enter a pizza topping, or 'quit' to quit.\n")
        if topping == "quit":
            run = False
            print("Okay, you want these toppings on your pizza:")
            print(toppings)
        else:
            toppings.append(topping)
elif exercise == 5 or exercise == 6:
    #7-5
    ages = []
    people = 0
    while True:
        people += 1
        age = int(input("How old are you?'n"))
        if age <= 3:
            print("Your ticket is free.")
        elif age >= 4 and age <= 12:
            print("Your ticket is $10")
        elif people > 3:
            break
        else:
            print("Your ticket is $15")

    #7-6
    #See 7-5
elif exercise == 7:
    #7-7

    count = 0

    while True:
        count += 1
        print(count)
        if count >= 50000:
            break
elif exercise == 8:
    #7-8
    sandwich_orders = ["reuben", "pastrami", "croque monseur", "cuban", "pastrami", "meatball sub", "grilled cheese", "pastrami"]
    finished_sandwiches = []

    for sandwich in sandwich_orders:
        print(f"Your {sandwich.title()} sandwich is ready!")
        finished_sandwiches.append(sandwich)
    print("All sandwiches have been made!\n")

elif exercise == 9:
    sandwich_orders = ["reuben", "pastrami", "croque monseur", "cuban", "pastrami", "meatball sub", "grilled cheese", "pastrami"]
    finished_sandwiches = []

    print("We're out of pastrami today, sorry!")
    for sandwich in sandwich_orders:
        if sandwich != "pastrami":
            print(f"Your {sandwich.title()} sandwich is ready!")
            finished_sandwiches.append(sandwich)
        else:
            print("Unfortunately we can't make this sandwich.")

elif exercise == 10:
    responses = {}
    polling_active = True
    while polling_active:
        name = input("What is your name?\n")
        response = input("Where would your dream vacation be?\n")
        responses[name] = response
        
        repeat = input("Is there another person ready to answer? Y/N\n")
        if repeat == "N" or repeat == "n":
            break
        elif repeat == "Y" or repeat == "y":
            pass
        else:
            print("Invalid Response...")
            
    print("\n--- Poll Results ---")
    for name,response in responses.items():
        print(f"{name.title()} wants to vacation in {response.title()}.")
else:
    print("I haven't gotten that far yet!")
    print("¯\_(ツ)_/¯")