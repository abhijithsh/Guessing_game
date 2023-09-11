from random import shuffle

def shuffled_list():
    mylist = [' ','O',' ',' ',' ',' ']
    shuffle(mylist)
    return mylist

def player_guess():
    print("Simple Game Rules: Choose a number from 0-5, If the chosen number gets equal to the shuffled position you won")
    guess = ''
    while guess not in ['0','1','2','3','4','5']:
        guess = input("Pick a number 0,1,2,3,4,5: ")
    else:
        pass
    return int(guess)

def game_logic(mylist,guess):
    if mylist[guess] == 'O':
        print("Yaaay correct guess")
        
    else:
        print("Nope your guess was wrong")
        print(mylist)

    


list = shuffled_list()
guess = player_guess()
game_logic(list,guess)