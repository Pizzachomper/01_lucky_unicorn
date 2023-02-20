#functions go here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("please answer yes / no")

def instructions():
    print("^*^ How to Play ^*^")
    print()
    print("The rules of the game go here")
    print()
    return ""

def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"
    error2 = "Please enter a correct integer\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            #if the ammount is too low / too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error2)



#Main routine
played_before = yes_no("Have you played this game before? ")
print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

#Ask user how much they want to play with...

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

print("Program continues")
