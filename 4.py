def calculate_probability(event_a, event_b, possible_outcomes):
    # probability of event a
    probability_a = len(event_a) / len(possible_outcomes)

    # probability of event b
    probability_b = len(event_b) / len(possible_outcomes)

    # intersection of events a and b
    common_events = event_a.intersection(event_b)

    # probability of intersection of events a and b
    common_probability = len(common_events) / len(possible_outcomes)

    # add return statement here
    return (probability_a + probability_b - common_probability)


# rolling a die once and getting an even number or an odd number
even_numbers = {2, 4, 6}
numbers_greater_than_two = {3, 4, 5, 6}
possible_rolls = {1, 2, 3, 4, 5, 6}

# call function for final result
print('Probability of Getting an even number or a number greater than 2')
print(calculate_probability(even_numbers, numbers_greater_than_two, possible_rolls))
