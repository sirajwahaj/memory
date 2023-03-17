import game_level
import sorted_list

# this function is checking users guess
def check_users_guess(x, y):
       return x == y
     

    
while True:
    complixity_level = int(input("Choose which the level: \n    1- easy \n  2- medium \n    3- Hard \n" ))

    if complixity_level not in [1 , 2, 3]:
         continue
        
    # Computer guess and print it on the screen
    computer_selected_string = game_level.selecting_random_characters(complixity_level)
    # User has to remember this string
    sorted_list.show_ordered_string(computer_selected_string)   
    # Showing unordered string     
    print(computer_selected_string)
    # User guess
    user_guess = input('Enter the text in ordered form: ')
    if check_users_guess(computer_selected_string, user_guess):
        print('Congratulations you have guessed correctly')
        break
    else:
            print('Entered string wasnt correct. Try again')
