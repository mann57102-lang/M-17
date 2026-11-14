import random

def ball_selection_experiment():
    # defining our balls as lists
    ball_list = ['Blue', 'Red', 'Green']

    # "flipping" coins randomly
    selected_ball = random.choice(ball_list)

    # Finding the probability
    probability = ball_list.count('Red') / len(ball_list)
    print("Probability of Picking Red Ball is:", probability)

    # checking if red ball was picked
    if selected_ball == 'Red':
        return 'Red Ball was Picked'
    else:
        return 'Better Luck Next Time'

result = ball_selection_experiment()
print(result)
