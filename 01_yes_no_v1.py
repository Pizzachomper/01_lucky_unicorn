show_instructions = ""
while show_instructions.lower() != "xxx":
    #ask the user if they have played before
    show_instructions = input("Have you played before?").lower()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print ("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    else:
        print("please answer yes / no")