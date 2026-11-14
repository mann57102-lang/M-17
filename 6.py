def calculate_joint_probability(orange_balls, blue_balls, total_balls):
    # probability of event a
    probability_orange = orange_balls / total_balls

    # probability of event b
    probability_blue_after_orange = blue_balls / (total_balls - 1)

    # probability of intersection of events a and b
    joint_probability = probability_orange * probability_blue_after_orange

    # add return statement here
    return round(joint_probability, 3)


# taking input for total number of orange and blue balls
orange_balls = int(input("Enter number of orange balls "))
blue_balls = int(input("Enter number of blue balls "))
total_balls = orange_balls + blue_balls


# call function for final result
print('Probability of Getting 1st orange and 2nd blue ball: ')
print(calculate_joint_probability(orange_balls, blue_balls, total_balls))
