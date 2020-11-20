import printing_functions
from functions import *

exercise = int(input("Which exercise?\n"))

def display_message():
    print("This is a message.")

def favorite_book(title):
    print(f"My favorite book is called {title.title()}.")

def make_shirt(size, message):
    print(f"Okay, you'd like a {size} shirt that says '{message}', right?")

def define_city(city_name, city_location):
    print(f"The city of {city_name} is in {city_location}.")

def city_country(city_name, country):
    loc_pair = f"{city_name.title()}, {country.title()}"
    return loc_pair

def album_parse(title, artist, tracks=''):
    if tracks:
        info = {'Title':title, 'Artist':artist, 'Tracks':tracks}
        return info
    else:
        info = {'Title':title, 'Artist':artist}
        return info
def make_album(title, artist):
    defalbum = True
    while defalbum:
        print(f"Your album is {title.title()} by {artist.title()}, right?")
        correct = input("Correct? Y/N")
        if correct == "Y":
            break
        else:
            pass

def show_messages(messagelist):
    for message in messagelist:
        print(message)

def send_messages(message, messagelist=[]):
    if message:
        print(message)
        messagelist.append(message)

def make_sandwich(*ingredient):
    ingredients = []
    ingredients.append(ingredient)
    for item in ingredients:
        print(f"You want {item} on your sandwich, correct?")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

if exercise == 1:
    #8-1
    display_message()
elif exercise == 2:
    #8-2
    favorite_book(input("What is your favorite book?\n"))
elif exercise == 3:
    #8-3
    make_shirt("medium", "this *is* my alter ego")
    make_shirt(message="get in mah bellah", size="large")
elif exercise == 4:
    #8-4
    size = "large"
    message = "I love Python"
    make_shirt(size, message)
    size = "medium"
    make_shirt(size, message)
    make_shirt(size="small", message="I love C#")
elif exercise == 5:
    #8-5
    define_city("Chicago", "USA")
    define_city(city_location="Buttkavic", city_name="Shartz")
elif exercise == 6:
    #8-6
    print(city_country("auckland", "new zealand"))
    print(city_country("san antonio", "united states"))
    print(city_country("recife", "brazil"))
elif exercise == 7:
    #8-7
    album = album_parse("the green book", "twiztid")
    print(f"{album['Title'].title()} is an album by {album['Artist'].title()}.")
    album = album_parse("cool is just a number", "i fight dragons", "7")
    print(f"{album['Title'].title()} is an album by {album['Artist'].title()} with {album['Tracks']} tracks.")
elif exercise == 8:
    #8-8
    make_album(input("Album name?\n"), input("Artist name?\n"))
elif exercise == 9:
    #8-9
    messagelist = ["This is a message.", "This is another message.", "This is yet another message."]
    show_messages(messagelist)
elif exercise == 10:
    #8-10
    message = input("Type a message.")
    send_messages(message)
elif exercise == 11:
    #8-11
    messagelist = ["This is a message.", "This is another message.", "This is yet another message."]
    send_messages("New Message", messagelist)
    print(messagelist)
elif exercise == 12:
    #8-12
    response = 0
    while response < 3:
        ingredient = input("Enter an ingredient for your sandwich!")
        make_sandwich(ingredient)
elif exercise == 13:
    #8-13
    user_info = build_profile("Corey", "Kabbage", trait1="Kind", trait2="Forgetful", trait3="Elfboi")
    print(user_info)
    print(f"{user_info['first_name'].title()} {user_info['last_name'].title()} is {user_info['trait1']}, {user_info['trait2']}, and {user_info['trait3']}.")
elif exercise == 14:
    #8-14
    car = make_car('Tesla', 'Cybertruck', color="Stainless", option1="heated seats", option2="heated steering wheel")
    print(car)
elif exercise == 15:
    #8-15
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    printing_functions.print_models(unprinted_designs, completed_models)
    printing_functions.show_completed_models(completed_models)
elif exercise == 16:
    #8-16
    danceindex = int(input("What dance would you like to see? 1-3\n"))
    dance(danceindex)
elif exercise == 17:
    #Already following the guidelines. lol
else:
    pass