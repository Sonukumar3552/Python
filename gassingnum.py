import random

def number_gussing_game(user_number,level):
    if level == 'Hard':
        attemp = 5
    else:
        attemp = 10
     

    count = 0
    computer_guess = random.randint(1,10)
    # print(computer_guess)
    game_end = False
    while not game_end:
        if user_number == computer_guess:
            print(f"you win in {count+1} attemp")
            game_end = True
            return True

        elif computer_guess>user_number:
            print('Too low')
            print(f"you have {attemp-1} attemp remain")
            attemp-=1
            count+=1
            
        elif computer_guess<user_number:
            print("too high")
            print(f"you have {attemp-1} attemp remain")
            attemp-=1
            count+=1   
            
        if attemp == 0:
            print(f"you have {attemp} attemp you lose and guessing number is {computer_guess}")

            game_end = True
            return False
        user_number = int(input('Guess again: '))
        


print('Wellcome to number guessing game !')
level = input("select defculty level type 'Hard' or 'Easy' : " )

if level == 'Hard':
    print('You have only 5 attemp to guess a number \n')
       
else:
    print('You have 10 attemp to guess a number \n')

user_guess = int(input('Guess the number between 1 to 100 :'))
number_gussing_game(user_number=user_guess,level=level)