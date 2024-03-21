import time


# simple word hangman game using python programming
def hangman_game():
    print('''
             ~Lets play the hangman game pema sir or relatives of pema sir~ 
           ******************************************************************''')
    gamer_name = input("Enter your name:_").capitalize()
    gamer_relation = input("Enter your relation with pema singi Waiba[bro/sis/sir/mam/student/friend]:_")

    if gamer_relation == 'brother' or gamer_relation == 'bro' or gamer_relation == 'Brother':
        print("Hello {}".format(gamer_name), '{}  I know you are my relatives get ready to play hangman game'
              .format(gamer_relation))
    elif gamer_relation == 'sister' or gamer_relation == 'sis' or gamer_relation == 'Sister':
        print("Hello {}".format(gamer_name),
              '{}  I know you are my relatives get ready to play hangman game'
              .format(gamer_relation))
    elif gamer_relation == 'sir' or gamer_relation == 'Sir':
        print("Hello {}".format(gamer_name),
              "{}  I know you are my respected sir get ready to play hangman game"
              .format(gamer_relation))
    elif gamer_relation == 'mam' or gamer_relation == 'Mam':
        print("Hello {}".format(gamer_name),
              '{}  I know you are my relatives get ready to play hangman game'
              .format(gamer_relation))
    elif gamer_relation == 'student' or gamer_relation == 'Student':
        print("Hello {}".format(gamer_name),
              "{}  I know you are my close student get ready to play hangman game"
              .format(gamer_relation))
    elif gamer_relation == 'friend' or gamer_relation == 'Friend':
        print("Hello {}".format(gamer_name),
              "{}  K cha tw sathi"
              .format(gamer_relation))
    else:
        print("Hello it's {}".format(gamer_relation),
              '{} sir confuse Nahunu! I am get ready to play hangman game'
              .format(gamer_name))
    time.sleep(1)
    print("You have to make word guessing char like[A-Z or a-z]")
    print("Now start your game:")
    time.sleep(0.7)
    word = 'science'
    guesess = ''
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesess:
                print(char, end='')
            else:
                print('_', end='')
                failed += 1

        if failed == 0:
            print(" word generate")
            print("You won the game")
            exit_game()
            break
        guess = input(":Guess the char:_")
        guesess += guess

        if guess not in word:
            turns -= 1
            print("Wrong guess")
            print("you have", turns, 'turn remaining')
        if turns == 0:
            print("you lose the game")
            exit_game()


def exit_game():
    re_play = input("Do you want to re-play game?[y or n]:_")
    if re_play == 'y' or re_play == 'Y':
        hangman_game()
    else:
        print("Exit the game")


hangman_game()
