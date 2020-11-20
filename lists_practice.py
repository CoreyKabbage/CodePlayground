#Initialize a list of names from my family.
names = ['missie', 'pat', 'maggie', 'mia', 'corey']

#print the raw list.
print(names)

#Print individual items from the list.
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())

#Initialize a message using the list.
message = f"\nMy sister's name is {names[0].title()}, and her husband is {names[1].title()}. They have two daughters named {names[2].title()} and {names[3].title()}. I am their uncle, and my name is {names[4].title()}."

#Print the message.
print(message)

#Some greetings using the names.
print(f"Hey {names[0].title()}, I hope you like the programs I've written!")
print(f"{names[1].title()}, I love the music recommendations!")
print(f"{names[2].title()} and {names[3].title()}, I'm so glad I get to be a part of your lives, because you make me believe I can help those who need positivity.")
print(f"Remember, {names[4].title()} will always love and support you no matter what.\n")

#Another list of my favorite bands.
bands = ['i fight dragons', 'dubmood', 'the men that will be blamed for nothing', 'gorillaz', 'desert dwellers']

#Print the raw list.
print(bands)

#Printing the list in a series of statements.
print(f"\nUsually, I listen to music by {bands[4].title()} to meditate.")
print(f"Other times, I listen to {bands[0].title()} when I am anxious.")
print(f"{bands[1].title()} is what I like to amp myself up with.")
print(f"{bands[2].title()} and {bands[3].title()} are just plain good music.")

#Changing an item in the list.
bands[2] = 'the men that will not be blamed for nothing'

#Print the correction.
print(f"Oops, it's actually {bands[2].title()}, not what I wrote before!\n")

#Adding items to the list, with one useless item to be removed.
bands.append('the decemberists')
bands.append('wilco')
bands.append('blahblahblah')

#Print the new list raw.
print(bands)

#Print the new items.
print(f'\n{names[1].title()} has recommended the bands {bands[5].title()} and {bands[6].title()} to me as well!\n')

#Remove the last, useless item.
popped_item = bands.pop(7)

#Print the corrected list.
print(bands)
print(popped_item + " was a mistake!")

#Sort the list alphabetically.
bands.sort()
num_bands = len(bands)
#print the sorted list
print(bands)
print(f'There are {num_bands} bands in the list.')

bands.clear()
#Print the (hopefully!) now-empty list.
print(bands)
