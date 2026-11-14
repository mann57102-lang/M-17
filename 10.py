import numpy as np

# create 6 sided "die"
number_of_sides = int(input("enter number of sides for dice (6/12) : "))
dice = range(1, number_of_sides)

# set number of rolls
number_of_rolls = int(input("Enter number of times you want to roll the dice : "))

# roll the "die" the set amount of times
roll_results = np.random.choice(dice, size=number_of_rolls, replace=True)
print(roll_results)
