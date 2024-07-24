# here we will se if , elif and else statement i python as well as match in python
#  we'll create a program that will recomment a game to player as per their requirement 
def main():
    print("What kind of game do you want??")
    difficulty = input("Level of difficulty: Difficult or Casual? ")
    if not (difficulty == 'Difficult' or difficulty =='Casual'):
        print("Enter a valid difficulty")
        return  # Exit the function if invalid input
    
    #  not keyword turns Flase into True and True into False

    players = input("do you want to play Single-Player or Multi-Player? ")
    
    mode = input("How do you want to play game: Online or Offline? ")
    if not (mode =='Online' or mode=='Offline'):
        print("Enter a valid mode of game")
        return
    
    if mode == 'Offline':
        if not (players == "Single-Player" or players =='Multi-Player'):
            print("Enter valid no. of players")
            return  # Exit the function if invalid input
        useIfElifElse(difficulty,players)
    else:
        useMatch(difficulty,players)
# both useIfElifElse and useMatch function have same execution 

def useIfElifElse(difficulty,players):
    if difficulty == 'Difficult' and players == 'Single-Player':
        recommend('Sudoku')
    elif difficulty == 'Difficult' and players == 'Multi-Player':
        recommend('Chess')
    elif difficulty == 'Casual' and players == 'Multi-Player':
        recommend('Uno')
    else:
        recommend('Jigsaw Puzzle')

def useMatch(difficulty,players):
    #    match is same as switch in C and JAVA
        match (difficulty, players):
            case ('Difficult', 'Single-Player'):
                recommend('Dark Souls')
            case ('Difficult', 'Multi-Player'):
                recommend('League of Legends')
            case ('Casual', 'Single-Player'):
                recommend('Stardew Valley')
            case ('Casual', 'Multi-Player'):
                recommend('Among Us')
            case _:   # the '_' is used for default case
                recommend('Minecraft')
            


def recommend(game):
    print("You Should Play",game)

main()


 