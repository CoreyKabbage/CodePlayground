import os
import sys

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['color'] = 'yellow'
alien_0['points'] = 10

print(alien_0['color'])
print(alien_0['points'])

points = alien_0['points']
print(f"You earned {points} points!")

print(alien_0)

alien_0['xpos'] = 25
alien_0['ypos'] = 10

print(alien_0)

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0['xpos'] = 0
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Fast alium!
    x_increment = 10

alien_0['xpos'] = alien_0['xpos'] + x_increment
print(f"New Position: {alien_0['xpos']}")

del alien_0['points']
print(alien_0)

del alien_0
os.system("pause")

# 6-5

rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'missipi': 'usa',
}

for river in rivers:
    locale = rivers[river]
    if locale == 'usa':
        print(f"The {river.title()} river is in {locale.upper()}.")
    else:
        print(f"The {river.title()} river is in {locale.title()}")

# 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'corey': 'c#'
}

poll_names = {'corey', 'benji', 'joachim',
              'jen', 'javier', 'kurt', 'louie', 'sarah'}

for name in poll_names:
    if name in favorite_languages:
        print(f"Thanks for responding, {name.title()}!")
    else:
        print(f"{name.title()}, what is your favorite language?")

# 6-4

print("Favorite languages survey:")
for name in favorite_languages.keys():
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, you love {language}!")

# ExtraCredit

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'blue', 'points': 10}
alien_2 = {'color': 'purple', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

del alien_0, alien_1, alien_2

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print('First 5 Aliens')

for alien in aliens[:5]:
    print(alien)
    print('...')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

print('Same 5 Aliens')

for alien in aliens[:5]:
    print(alien)
    print('...')

os.system("pause")

# Store pizza information.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# 6-7

friends = {
    'cday': {
        'first': 'corey',
        'last': 'day',
        'location': 'elizabeth',
    },
    'mowen': {
        'first': 'missie',
        'last': 'owen',
        'location': 'parker',
    },
    'powen': {
        'first': 'patrick',
        'last': 'owen',
        'location': 'parker',
    },
    'nhurst': {
        'first': 'nick',
        'last': 'hurst',
        'location': 'denver',
    },
    'towen': {
        'first': 'tom',
        'last': 'owen',
        'location': 'parker',
    },
}

scientists = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'america',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'france',
    },
    'inewton': {
        'first': 'isaac',
        'last': 'newton',
        'location': 'england'
    },
    'ggalilei': {
        'first': 'galileo',
        'last': 'galilei',
        'location': 'italy'
    },
    'shawking': {
        'first': 'stephen',
        'last': 'hawking',
        'location': "cambridge",
    },
}

actors = {
    'jnicholson': {
        'first': 'jack',
        'last': 'nicholson',
        'location': 'california',
    },
    'mbrando': {
        'first': 'marlon',
        'last': 'brando',
        'location': 'california',
    },
    'rdniro': {
        'first': 'robert',
        'last': 'de niro',
        'location': 'california',
    },
    'apacino': {
        'first': 'al',
        'last': 'pacino',
        'location': 'california',
    },
    'ddaylewis': {
        'first': 'daniel',
        'last': 'day-lewis',
        'location': 'california',
    },
}

groups = [
    actors,
    scientists,
    friends,
]

for group in groups:
    for person, person_info in group.items():
        print(f"\nPerson: {person}")
        full_name = f"{person_info['first'].title()} {person_info['last'].title()}"
        location = person_info['location'].title()
        print(f"Full name: {full_name}")
        print(f"Location: {location}")