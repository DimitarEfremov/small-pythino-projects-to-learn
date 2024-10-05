# To be replace with question, what kind of game does the user want to play.
print('Welcome! Do you you want to play a game of dice?')

user_answer = input('Please select Y or N: ')
game_code = 0
counter_for_invalid_answers = 0

while game_code == 0:
    if user_answer == 'y' or user_answer == 'Y':
        print('Lets play dice')
        game_code = 1
    elif user_answer == 'n' or user_answer == 'N':
        # to be replace with if the user wants to play another game
        print('See you soon! ;)')
        exit(0)
    else:
        counter_for_invalid_answers += 1
        if counter_for_invalid_answers > 5:
            print('Too many invalid answers')
            exit(0)
        user_answer = input('Invalid input, please select \'Y\' or \'N\': ')



