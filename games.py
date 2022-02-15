import divination
import hangman

def play_games():
    print("*********************************")
    print("********Welcome to games!********")
    print("*********************************")

    print("Choose your game: (1)Divination Game (2)Hangman Game")
    choice = int(input("Choose: "))

    if(choice == 1):
        divination.play_divination()
    elif(choice == 2):
        hangman.play_hangman()
    else:
        print("Choose a valid number!")
        play_games()

if(__name__ == "__main__"):
    play_games()