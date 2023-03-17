import random
import string

# Defining charaters rang for different levels
string_level_one = string.digits
string_level_two = string.ascii_letters
string_level_three = string.ascii_letters + string.digits

def selecting_random_characters(level):
    string_levels = ""
    # Choosing the level of the game

    if level == 1:
        string_levels = string_level_one
    elif level == 2:
        string_levels = string_level_two
    elif level == 3:
        string_levels = string_level_three
    else:
        return False
    #Choosing a string by Computer
    conver_to_list = list(string_levels)
   #
    start_index = random.randint(0, len(conver_to_list)-1)
    end_index = start_index + 8
    random_charaters = conver_to_list[start_index:end_index]
    random.shuffle(random_charaters)
    shuffled_string = ''.join(random_charaters)
    return shuffled_string
