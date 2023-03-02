import random

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


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)


    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


#Main routine
played_before = yes_no("Have you played this game before? ")
print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

#Ask user how much they want to play with...

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

#set balance for testing purposes
balance = how_much

rounds_played = 0

play_again = input("Press <enter> to play . . .").lower()

while play_again == "":

    #Increase # of rounds played
    rounds_played += 1
    

    # Print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    print()

    chosen_num = random.randint(1, 100)
    
    #adjust balance
    if 1 <= chosen_num <= 5: 
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = ("You got a {}. Your balance is " "${:.2f}".format(chosen, balance))

    statement_generator(outcome, prize_decoration)


    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit")

print()
print("Final balance $",balance)
print()