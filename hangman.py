import random                       

textfile = open("hangman_wordlist.txt", "r")                                # pre-game, setting the variables
all_words = tuple(textfile.readlines())
textfile.close()

difficulty = 1 #initial value
wordlist = []
if difficulty == 1:                                                         # easy
    health = 10
    for word in all_words:
        if len(word.rstrip("\n")) >= 10:
            wordlist.append(word.rstrip("\n"))
elif difficulty == 2:                                                       # medium
    health = 8
    for word in all_words:
        if len(word.rstrip("\n")) >= 6 and len(word.rstrip("\n")) <= 9:
            wordlist.append(word.rstrip("\n"))
elif difficulty == 3:                                                       # hard
    health = 6
    for word in all_words:
        if len(word.rstrip("\n")) == 4 or len(word.rstrip("\n")) == 5:
            wordlist.append(word.rstrip("\n"))            

chosen_word = random.choice(wordlist)
used_letters = []

while health > 0:                                                           # the game itself

    puzzle = ""
    for letter in chosen_word:
        if letter in used_letters:
            puzzle += letter
        else:
            puzzle += "_"
    puzzle = f"{puzzle}  ({len(puzzle)})"                                   # this should be displayed
    
    used = []
    for letter in used_letters:
        if letter not in used:
            used.append(letter)
    used = "[" + ", ".join(sorted(used)) + "]"

    if "_" not in puzzle:                                                   # winning condition
        print("You won")
        break

    print(f"{puzzle}\nused letters: {used}\nhealth = {health}")
    guess = input(">")                                                      # I assume that there is a more sophisticated way to get the input and that You'll figure it out
    if len(guess) == 1 and guess.isalpha():
        if guess in chosen_word:
            used_letters.append(guess)
            print("Good")
        else:
            used_letters.append(guess)
            health -= 1
            print("Incorrect")
    else:
        print("Invalid input")
else:
    print(f"You lost, the correct word was: {chosen_word}")