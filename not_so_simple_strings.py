#Import the necessary module to make the script wait for t seconds.
import time

#Initialize the name in lowercase, then make it a single variable.
first_name = "maggie"
last_name = "maggz"
full_name = "{} {}".format(first_name, last_name)

#Print the name in Title case.
print("Hello, " + full_name.title() + "!")

#Initialize another variable
favorite_uncle = '   Corey '

#Print the new variable, but without stripped whitespaces.
print("\nYour favorite uncle is " + favorite_uncle + "!")

#Wait for 1 second.
time.sleep(1);

#Print a reference to the error.
print ("\nThat wasn't right... Let's try again.");
favorite_uncle = 'Bubby'

time.sleep(1);

#Print the same line as before, stripping out the whitespace.
print("\nYour favorite uncle is " + favorite_uncle.strip() + "!")

#Initialize the quote, and who said it.
famous_quote = '"The journey of a thousand miles begins with a single step."'
famous_person = "Lao Tzu"

time.sleep(1)

#Print the previous variables, with some escaped characters - \n is a new line and \t is a tab indentation.
print("\n\tSince you're learning, this quote might help you stay motivated: \n\t" + famous_person +  ' says, ' + famous_quote)

#Wait until Enter is pressed so you can actually see the message before it disappears.
input('\nPress enter to exit...')
