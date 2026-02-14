"""
Topic: Functions in python
Description: Functions structure and common cases

"""

#Seeting functions to calculate the time cooking a lasagna:

#First we work with constants:

EXPECTED_BAKE_TIME = 40
MINUTES_EACH_LAYER = 2

#Defining the functions with their parameters:
def preparation_time_before_baking(number_of_layers):
    """Calculate the preparation time in minutes according the parameter:
       number_of_layers = int - number of layers of the lasagna

       Function that takes the number of layers of the lasagna and returns the total minutes that takes the preparation based on 
       the constant MINUTES_EACH_LAYER.
    """
    return MINUTES_EACH_LAYER*number_of_layers #returns the output of the function 


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total minutes of the preparation.
    Takes two parameters:
        number_of_layers: int - The number of layers added to the lasagna
        elapsed_bake_time: int - The number of minutes the lasagna has spent baking in the oven already
       number_of_layer = int - number of layers of the lasagna

       Function that take both parameters and returns the total minutes you have been in the kitchen cooking.
    """
    return preparation_time_before_baking(number_of_layers) + elapsed_bake_time

function_1 = preparation_time_before_baking(5)
function_2 = bake_time_remaining(20)
function_3 = elapsed_time_in_minutes(5, 20)

print(f"Preparation time before baking: {function_1}\nBake time remaning: {function_2}\nElapsed time in minutes: {function_3} ")




