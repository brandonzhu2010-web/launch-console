print("Welcome to the Launch Console!")
name = input("What is your name? ")
print("Hi, " + name + "!")
running = True
choice = ""
words = ["fall","math","table","dog"]
while running:
    print("""Here is the menu:
    1: About me
    2. My goals
    3. Word guess game
    4. Exit""")
    choice = input("Which option would you like to choose? Just type the number: ")
    if choice == "1":
        print("Hi! My name is Brandon, I am 15 years old, and I live in Austin Texas. I like to play basketball and hang out with my friends.")
    elif choice == "2":
        print("My goals are to get an internship in Code2College, and later make it into a top college and become some type of doctor when I'm older.")
    elif choice == "3":
        print("Here are the 4 words for you to guess from: ")
        print(words)
        guess = input("Guess here: ")
        if guess == words[0]:
            print("Congrats! You got it right ")
        else:
            print("You got it wrong")
    elif choice == "4":
        running = False
        print("Goodbye!")
    else:
        print("That is not a valid choice")

