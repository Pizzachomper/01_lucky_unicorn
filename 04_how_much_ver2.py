# Functions go here
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


# Main routine goes here
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
