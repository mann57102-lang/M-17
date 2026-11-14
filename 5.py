def calculate_joint_probability(student, dining):

    if student == 1:
        student_probability = 0.3
        if dining == 1:
            dining_probability = 0.75
        else:
            dining_probability = 0.25
        print("Probability of a given b:", dining_probability)

    if student == 2:
        student_probability = 0.7
        if dining == 1:
            dining_probability = 0.6
        else:
            dining_probability = 0.4
        print("Probability of a given b:", dining_probability)

    joint_probability = student_probability * dining_probability
    return round(joint_probability, 3)


print("Check the probability of any event occuring. First enter your choices.")

print("Is the student a Freshman? \n 1. Yes \n 2. No")
student_choice = int(input("Enter your choice (1/2): "))

print("Is student eating in dining hall? \n 1. Yes \n 2. No")
dining_choice = int(input("Enter your choice (1/2): "))

print("Here is the probability of both the events occuring :", calculate_joint_probability(student_choice, dining_choice))
