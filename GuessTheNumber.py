import random

def GuessTheNumber():
    rando = random.randint(0,10)
    intro = input("Hi there, Welcome to GUESS THE NUMBERRRRRRR between 1 and 10!!!! \nAre You Ready? \nEnter Your Guess -> ")

    def guess(intro):
        if(rando == int(intro)):
            print("OMG YOU ARE TOO SMART")
        if(rando < int(intro)):
            print("LOWER")
            newTry = input("Try Again -> ")
            guess(newTry)
        if(rando > int(intro)):
            print("HIGHER")
            newTrys = input("Try Again -> ")
            guess(newTrys)

    guess(intro)




GuessTheNumber()