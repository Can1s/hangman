import random

lst = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(lst)
temp = "-" * len(random_word)
string = list()
fault = 8
print("H A N G M A N \n")
while True:
    action = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if action.__eq__("exit"):
        break
    else:
        while True:
            if fault > 0 and temp.__eq__(random_word):
                print(random_word)
                print("You guessed the word!")
                print("You survived!")
                break
            elif fault == 0:
                print("You are hanged!")
                break
            else:
                print()
                print(temp)
                letter = input("Input a letter: ")
                if letter.isalpha() and letter.islower() and len(letter) == 1:
                    if letter in string:
                        print("You already typed this letter")
                        continue
                    else:
                        string.append(letter)
                    if letter in random_word:
                        count = -1
                        for char in random_word:
                            count += 1
                            if char == letter:
                                t = list(temp)
                                t[count] = letter
                                temp = "".join(t)
                    else:
                        print("No such letter in the word")
                        fault -= 1
                else:
                    if len(letter) != 1:
                        print("You should input a single letter")
                    else:
                        print("It is not an ASCII lowercase letter")
