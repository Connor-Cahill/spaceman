##### LEFT OFF: started setting up game loop: right now it pops char from mystery list if it is guess correctly.
### when list is empty the game ends. Game also ends when user enter "exit"


##Need to format terminal, show relevant info between every turn


import string
import random
#create a list of possible mystery words
possible_words = ['earth', 'winter', 'lake', 'computer', 'something']
# set variable that stores number of missed counts
num_wrong_guesses = 0
#set empty list for missed guesses
wrong_guesses = []
correct_guesses = []

#set mystery word to random word from word list to mystery word
mystery_word = random.choice(possible_words)
#mystery word set as string, make into list and IF correct guess, print letter from word#
mystery_list = list(mystery_word)

print(mystery_list)

def check_type(word):
    """Takes user input and checks to make sure it is a letter """
    if word.isalpha():
        return True
    else:
        return False
        print('Must be a letter, guess again.')
def print_info():
    print('These are the correct guesses so far: ')
    print(correct_guesses)
    print('Here are the wrong guesses so far: ')
    print(wrong_guesses)

game_loop = True
#Setup game loop: ------ GAME LOGIC UNDER WHILE LOOP 
while game_loop == True:
    #while loop should run until the number of missed guesses = 7 OR the user inputs exit()
    user_guess = input('Please input 1 letter, enter "exit" to quit: ')
    user_guess = user_guess.lower()
    print(chr(27) + "[2J")
    if user_guess in mystery_list:
        print('Good guess, thats a correct letter')
        correct_guesses.append(user_guess)
        val = mystery_list.index(str(user_guess))
        #For right guess delete the letter in mystery
        mystery_list.pop(int(val))
        print_info()
        #if user guesses all letters in word USER WINS
        if mystery_list == []:
            print('Congratulations You Guessed The Word: ' + mystery_word)
            game_loop = False
            ##For user to exit
    elif user_guess == 'exit':
        game_loop = False
        ##If user guesses already guessed letter it forces a reguess
    elif user_guess in wrong_guesses or user_guess in correct_guesses:
        print('You already guess that letter, please guess again.')
        game_loop = True
    elif user_guess == '':
        print('You must have an input')
        #If user inputs an input longer than 1 letter forces a reguess
    elif len(user_guess) > 1:
        print('You can only guess one letter.')
        ##If user inputs a number it forces a reguess
    elif check_type(user_guess) == False:
        print('Your guess should be a number!')
        ##if the user guesses wrong
    else:
        #if 7 wrong guesses game is over
        if num_wrong_guesses == 7:
            print('You guess wrong 7 times, game over!')
            game_loop = False

        wrong_guesses.append(user_guess)
        #add another wrong guess
        num_wrong_guesses += 1
        print('You guessed wrong, thats ' + str(num_wrong_guesses) + '/7 wrong guesses.')
        print_info()



#in while loop as user input that allows user to guess letter
    #then display whether the guess was correct or incorrect
    #print # of incorrect guesses and letters guessed
    # print correct letters guessed

    ##USER GUESS
        #if user guess is in wrong_guesses list, ask to input another letter
        #if user guess is in word, display letters in word
