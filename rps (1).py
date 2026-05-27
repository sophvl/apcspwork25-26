#Sophia Chen
#Rock paper scissors game
#Initialize
import random
print("Welcome to the rock paper scissors game!")
wins = 0
losses = 0
ties = 0
#functions
def rps():
    global wins
    global losses
    global ties
    while True:
        person = input("Enter a number 1(rock), 2(paper), 3(scissors), or quit: ")    #Asks the user to input a number
        comp = random.randint(1,3)
        if person == comp:    #A tie if the user and the computer have the same result
            print("tie")
            ties = ties + 1
            print("wins: " + str(wins))
            print("losses: "+ str(losses))
            print("ties: "+ str(ties))
            continue
        elif person == "1" and comp == 3:
            print("You just earned 1 point, rock beats scissors")
            wins = wins + 1
            print("wins: " + str(wins))
            print("losses: "+ str(losses))
            print("ties: "+ str(ties))
            continue
        elif person == "2" and comp == 1:
            print("You just earned 1 point, paper beats rock")
            wins = wins + 1
            print("wins: " + str(wins))
            print("losses: "+ str(losses))
            print("ties: "+ str(ties))
            continue
        elif person == "3" and comp == 2:
            print("You just earned 1 point, scissors beats paper")
            wins = wins + 1
            print("wins: " + str(wins))
            print("losses: "+ str(losses))
            print("ties: "+ str(ties))
            continue
        elif person == "quit":     #stops the game only if the user chooses to quit
            break
        else:
            print("You lost!")
            losses = losses + 1
            print("wins: " + str(wins))
            print("losses: "+ str(losses))
            print("ties: "+ str(ties))
            continue
#main
rps()
