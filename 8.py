def calculate_probability(throat_infection_choice, test_result_choice):

    if throat_infection_choice == 1:
        probability_infection = 0.2

        if test_result_choice == 1:
            probability_positive_test_given_infection = 0.85
        elif test_result_choice == 2:
            probability_positive_test_given_infection = 0.15
        else:
            print("Invalid Choice")
            return

        joint_probability = probability_infection * probability_positive_test_given_infection

        print("Probability of b given a:", probability_positive_test_given_infection)
        print("Probability of both the events occuring:", joint_probability)

    elif throat_infection_choice == 2:
        probability_infection = 0.8

        if test_result_choice == 1:
            probability_positive_test_given_infection = 0.02
        elif test_result_choice == 2:
            probability_positive_test_given_infection = 0.98
        else:
            print("Invalid Choice")
            return

        joint_probability = probability_infection * probability_positive_test_given_infection

        print("Probability of b given a:", probability_positive_test_given_infection)
        print("Probability of both the events occuring:", joint_probability)

    else:
        print("Invalid Choice")


print("Let's calculate probability. Please enter choices for the events...")

print("Person has step throat? \n 1. Yes \n 2. No")
infection_choice = int(input("Enter your choice (1/2): "))

print("Person has tested positive? \n 1. Yes \n 2. No")
test_choice = int(input("Enter your choice (1/2): "))

print("Probabilities for event a and b:")
calculate_probability(infection_choice, test_choice)
