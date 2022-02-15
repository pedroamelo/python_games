import games
import random

def play_hangman():
    print("********************************")
    print("**Welcome to the Hangman Game!**")
    print("********************************")
    
    file = open("palavras.txt", "r")
    file_words = []

    for line in file:
        line = line.strip()
        file_words.append(line)    
    
    file.close()

    position = random.randrange(0,len(file_words))


    secret_word = file_words[position].upper()
    hidden_word = ["_" for letter in secret_word]

    lose = False
    win  = False
    miss = 7
    
    while(not lose and not win):
        print(hidden_word)
        print("You have {} tries left".format(miss))

        guess = input("Type a letter: ")
        guess = guess.strip()
        print("You typed: {}".format(guess))
        
        if(guess.upper() in secret_word.upper()):
            index = 0
            for word in secret_word:
                if(guess.upper() == word.upper()):
                    hidden_word[index] = word
                index = index + 1
        else:
            miss -= 1
            print("The letter doesn't exist in the word!")
            desenha_forca(miss)        
        
        if(miss == 0):
            lose = True
            print("You lose! Try again!")
        if("_" not in hidden_word):
            win = True
            print(hidden_word)
            print("You Won! Congratulations!")
        
    print("End of the game!")

    print("Do you want to play again or do you want to get back to games?")
    print("(1)Play again (2)Back to games (Any number)Exit the Game")
    choice = int(input("Choose: "))
    if(choice == 1):
        play_hangman()
    elif(choice == 2):
        games.play_games()
    else:
        print("Thank you for playing!")
    

def desenha_forca(miss):
    print("  _______     ")
    print(" |/      |    ")

    if(miss == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(miss == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(miss == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(miss == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(miss == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(miss == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (miss == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

    
if(__name__ == "__main__"):
    play_hangman()