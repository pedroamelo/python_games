import random
import games

def play_divination():

    print("*********************************")
    print("*Welcome to the Divination Game!*")
    print("*********************************")

    secret_number = random.randrange(1,100) #random number from 1 to 99
    tries = 0
    score = 1000

    print("What difficulty you want to play?")
    print("(1)Easy (2)Normal (3)Hard")
    difficulty = int(input("Select the difficulty: "))

    if(difficulty == 1):
        tries = 9
    elif(difficulty == 2):
        tries = 7
    else:
        tries = 4


    for rounds in range(1,tries + 1):
        
        print("Try", rounds, "of", tries)
        guess_str = input("Type a number between 1 and 99: ")

        print("You typed {}".format(guess_str))

        guess = int(guess_str)
        
        if (guess < 1 or guess > 99):
            print("You typed wrong! Type a number between 1 and 99")
            continue

        hit    = guess == secret_number
        higher = guess > secret_number
        lower  = guess < secret_number

        if(hit):
            if(difficulty == 2):
                score = round(score * 1.2)
            if(difficulty == 3):
                score = round(score * 1.5)         
            print("Awesome! You guessed right and made {} points!".format(score))
            break
        else:
            if(higher):
                print("You guessed higher, try a lower number!")
            elif(lower):
                print("You guessed lower, try a higher number!")
            gapscore = abs(secret_number - guess)
            score = score - gapscore

    print("End of the game!")
    
    print("Do you want to play again or do you want to get back to games?")
    print("(1)Play again (2)Back to games (Any number)Exit the Game")
    choice = int(input("Choose: "))
    if(choice == 1):
        play_divination()
    elif(choice == 2):
        games.play_games()
    else:
        print("Thank you for playing!")
    
   
if(__name__ == "__main__"):
    play_divination()