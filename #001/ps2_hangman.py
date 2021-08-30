# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "ps2_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
        if c in letters_guessed:
            pass
        else:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out_var = ''
    for c in secret_word:
        if c in letters_guessed:
            out_var += c
        else:
            out_var += '_'
        
    return out_var



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out_var = string.ascii_lowercase
    for c in letters_guessed:
        out_var = out_var.replace(c, '')
    
    return out_var
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('\n')
    letters_guessed = []
    print(len(secret_word)*'*', '       ', len(secret_word), 'Letters')
    num_of_fails = 0
    penalty = 0
    score = 0
    
    while penalty < 10 and num_of_fails < 6 and not is_word_guessed(secret_word, letters_guessed):
        guess = input('Enter One Letter then press Enter:\n')
        guess = guess.casefold()
        print('\n')
        
        #checking input validity
        if guess not in string.ascii_lowercase or len(guess) != 1:
            penalty += 1
            print('UNVALID INPUT\n',25 * '_')
            print('\n','Remaining chances:',max(6 - num_of_fails,0),30*' ','WARNINGS LEFT:',10-penalty,'\n\n')
            continue
        
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(guessed_word,'\n')
            if guess in secret_word:
                print('Good Job!', 10 * ' ',guessed_word.count('_'),'Letters to go')
                score += 1
            else:
                if guess in 'aieou':
                    num_of_fails += 2
                else:
                    num_of_fails += 1
                print('Try Again!', 10 * ' ',guessed_word.count('_'),'Letters to go')
        else:
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(guessed_word,'\n\n','You guessed this letter before!!!!!','\n','The available letters to guess are:',10*' ',get_available_letters(letters_guessed))
        
        print('\n','Remaining chances:',max(6 - num_of_fails,0),30*' ','WARNINGS LEFT:',10-penalty,'\n\n')
    
    
    if num_of_fails > 5 or penalty == 10:
        print('You   LOSE\n', 'Secret Word is:   ',secret_word)
    else:
        total_score = (6 - num_of_fails) * score
        print('Congrats!  You WIN','\n','Your Score in this game is:',10 * ' ',total_score)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and my_word[i] != other_word[i]:
                return False
        return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out_list = []
    for w in wordlist:
        if match_with_gaps(my_word, w):
            out_list.append(w)
    return out_list



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('\n')
    letters_guessed = []
    print(len(secret_word)*'*', '       ', len(secret_word), 'Letters')
    num_of_fails = 0
    penalty = 0
    score = 0
    hint = False
    
    while penalty < 10 and num_of_fails < 6 and not is_word_guessed(secret_word, letters_guessed):
        guess = input('Enter One Letter then press Enter:\n')
        guess = guess.casefold()
        print('\n')
        
        if guess == '*':
            if hint == False:
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                hint = True
            else:
                print('\nYOU ALREADY USED THE HINT!!!!\n')
            continue
        
        #checking input validity
        if guess not in string.ascii_lowercase or len(guess) != 1:
            penalty += 1
            print('UNVALID INPUT\n',25 * '_')
            print('\n','Remaining chances:',max(6 - num_of_fails,0),30*' ','WARNINGS LEFT:',10-penalty,'\n\n')
            continue
        
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(guessed_word,'\n')
            if guess in secret_word:
                print('Good Job!', 10 * ' ',guessed_word.count('_'),'Letters to go')
                score += 1
            else:
                if guess in 'aieou':
                    num_of_fails += 2
                else:
                    num_of_fails += 1
                print('Try Again!', 10 * ' ',guessed_word.count('_'),'Letters to go')
        else:
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(guessed_word,'\n\n','You guessed this letter before!!!!!','\n','The available letters to guess are:',10*' ',get_available_letters(letters_guessed))
        
        print('\n','Remaining chances:',max(6 - num_of_fails,0),30*' ','WARNINGS LEFT:',10-penalty,'\n\n')
    
    
    if num_of_fails > 5 or penalty == 10:
        print('You   LOSE\n', 'Secret Word is:   ',secret_word)
    else:
        total_score = (6 - num_of_fails) * score
        print('Congrats!  You WIN','\n','Your Score in this game is:',10 * ' ',total_score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    
    # Game loop
    while True:
        secret_word = choose_word(wordlist)
        #hangman(secret_word)
        hangman_with_hints(secret_word)
        k = input('Enter \"Y\" or \"y\" then press Enter to play another round:\n')
        if k not in 'yY' or len(k) != 1:
            print('\n\nBye Bye')
            break
        print(30 * '_','\n')

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
