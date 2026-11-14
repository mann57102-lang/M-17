red_shirts = int(input("Enter number of red shirts: "))
blue_shirts = int(input("Enter number of blue shirts: "))
white_shirts = int(input("Enter number of white shirts: "))

total_shirts = red_shirts + blue_shirts + white_shirts

probability_blue = blue_shirts / total_shirts
probability_red = red_shirts / total_shirts

probability_red_given_blue = probability_red
joint_probability = probability_blue * probability_red

print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round(probability_red_given_blue, 3))

print("Probability that the second shirt is red and the first shirt is blue: ")
print(round(joint_probability, 3))
