
exercise = int(input("Which exercise?"))

if exercise == 1:
    with open('text_files/learning_python.txt') as python_lines:
        lineoftext = python_lines.read()
    print(lineoftext.rstrip())
    with open('text_files/learning_python.txt') as python_lines:
        for lineoftext in python_lines:
            print(lineoftext.rstrip())
    with open('text_files/learning_python.txt') as python_lines:
        lines = python_lines.readlines()
    for line in lines:
        print(line.rstrip())

elif exercise == 2:
    with open('text_files/learning_python.txt') as python_lines:
        lineoftext = python_lines.read()
        print(lineoftext.replace('variable', 'attribute'))

elif exercise == 3:
    filename = "text_files/guest.txt"
    name = input("What is your name?\n")

    with open(filename, 'w') as file_object:
        file_object.write(name)

elif exercise == 4:
    namecollection = True
    guestindex = 0
    while namecollection:
        print("Hello and welcome to Python Inn.")
        name = input("What is your name?\n")
        time_of_stay = input("How long will you be staying with us?\n")
        guestindex += 1
        with open('text_files/guest_book.txt', 'a') as file_object:
            file_object.write(f"{name}\n")
            file_object.write(f"{time_of_stay}\n")
        if guestindex >= 3:
            break

elif exercise == 5:
    pollrunning = True
    response = 0
    while pollrunning:
        with open("text_files/programming.txt", "a") as file_object:
            question = input("Why do you like programming?\n")
            file_object.write(f"{question.rstrip()}\n")
            response += 1
        if response >= 3:
            break

elif exercise == 6:
    int1 = input("Type a number")

else:
    pass