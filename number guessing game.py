from random import *
def main():
    guesser()

def guesser():
    number = randint(1,10)
    guess = int(input("Guess the number: "))

    if number == guess:

        print("Congratulations, you have won!")

    else:
        
        print("We are sorry, but you have lost..")

if __name__ == "__main__":main()