#First, let's make a list of magicians' last names.
magicians = ['houdini', 'copperfield', 'angel']

#Now, we will do a looping operation on these names, filling in the names where is appropriate.
for magician in magicians:
    #Indented lines are part of the loop. The colon above creates this loop and tells Python to expect indentations.
    print(f"{magician.title()} is a prolific magician.")
    print(f"I can't wait to see what {magician.title()} will perform!\n")

#Finally, we conclude the entire message with a goodbye.
print("That concludes the introductions! Goodbye.\n")

#Use a range to find the numbers between the two values, and print them.
for value in range(1,6):
    print(value)

print("\n")

#More involved creation of a list using ranges, this time with a 3rd argument to define the step size.
even_numbers = list(range(2,21,2))
print("Even numbers:\n")
print(even_numbers)
print("\n")

#Make a list of all values from 1 to 100000
value = list(range(0,100001))

#Do some operations on the list, min, max, and a sum of the entire list.
print("Minimum, maximum, and sum:\n")
print(min(value))
print(max(value))
print(sum(value))
print("\n")
#Make a list of odd numbers from 1 to 20.
odd_numbers = list(range(1,21,2))

#Print the result of the list, in sequential order.
print("Odd numbers:\n")
for value in odd_numbers:
    print(value)
print("\n")
#Establish the multiples that will go up to 30 when multiplied by 3.
multiples = list(range(2,11))

#Multiply the values to show the multiples of 3 up to 30.
print("Multiples of 3:\n")
for value in multiples:
    print(value*3)
print("\n")

multiples = list(range(0,11))

print("Cubes from 1-10:\n")
for value in multiples:
    print(value**3)
print("\n")
