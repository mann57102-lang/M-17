probability_strep_throat = 0.2

probability_positive_with_strep = 0.2 * 0.85
probability_positive_without_strep = 0.8 * 0.02

total_probability_positive = probability_positive_with_strep + probability_positive_without_strep

probability_positive_given_strep = 0.85

final_probability = (probability_strep_throat * probability_positive_given_strep) / total_probability_positive

print("Probability of person testing positive having step throat is :", round(final_probability, 3))
