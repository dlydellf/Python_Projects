#
# Python: 3.9.4
#
# Author: Douglas L. Foreman
#
# Purpose:  The Tech Academy (Python Course) - Creating our first program.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game (called "Nice or Mean").
#

def start(nice=0, mean=0, name=''):
    # Get user's name:
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    

def describe_game(name):
    '''
        Check if this is a new game or not.
        If it IS new, get the user's name.
        If it is NOT new, thank the player for
        playing again, then continue the game.
    '''
    # Meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name.
    if name != '':
        print('\nWelcome back, {} - thank you for playing again!'.format(name))
    else:
        stop = True
        while stop:
            if name == '':
                name = input("\nHi! What's your name? \n>>> ").capitalize()
                if name != '':
                    print("\nWelcome, {}! We hope you'll enjoy \nplaying this 'Nice or Mean' Python game!".format(name))
                    print('--------------------------------------')
                    print('\nIn this game, you will be greeted by \nseveral different people. You can \nchoose to be nice or mean, and at the')
                    print('end of the game, your fate will be \nbased on your decisions. \nGood luck!')
                    stop = False
    return name

  
def nice_mean(nice,mean,name):
    questionTime = True # Asking the ? has been separated from user's choice to avoid repeating the ? if an Exception is raised:
    while questionTime:
        show_score(nice,mean,name)
        choice = input('\nA stranger approaches you for a \nconversation.  Will you be nice, \nor mean? (N/M) \n>>>: ').lower()
        decisionTime = True
        while decisionTime:
            if choice == 'n':
                print('\nYour niceness is contagious! \nThe stranger walks away, smiling...')
                nice += 1
                decisionTime = False # Steps us out of the nested while loop, just as...
                questionTime = False # ...steps us out of the parent while loop.
            elif choice == 'm':
                print('\nHow rude!  The stranger glares at \nyou menacingly before storming off.')
                mean += 1
                decisionTime = False
                questionTime = False
            else:
                choice = input('\nPlease choose one of these two: \neither "N" for nice or "M" for mean \n>>>: ').lower() # decisionTime still = T, so back to nested while loop's beginning
    score(nice,mean,name) # Passing the 3 variables to the score()


def show_score(nice,mean,name):
    print('\n{}, your current totals are: \n({}, Nice) and ({}, Mean)'.format(name,nice,mean))


def score(nice,mean,name):
    # score() is passed the 3 variables' values
    if nice > 2: # if condition is valid, call win() & pass in its parameter
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose() & pass in its parameter
        lose(nice,mean,name)
    else:       # else, call nice_mean() & pass in its 3 parameters
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitute the {} wildcards with our variables' values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again() & pass in its parameter
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variables' values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty, beat-up \nvan by the river, wretched and alone!".format(name))
    # Call again() & pass in its parameter
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input('\nDo you want to play again? (Y/N):\n>>> ').lower()
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print('\nOh, so sad, sorry to see you go!')
            stop = False
            quit()
        else:
            print('\nEnter ( Y ) for "Yes", ( N ) for "No":\n>>> ')


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variable, as the same user is playing again
    start(nice,mean,name)

        

if __name__ == '__main__':
    start()
