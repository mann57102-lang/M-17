import scipy.stats as stats

# value of interest
# change this
number_of_heads = 3

# sample size
# change this
number_of_trials = 10

# calculate probability
probability_exact_heads = stats.binom.pmf(number_of_heads, number_of_trials, 0.5)
print("Probability of getting 3 heads")
print(probability_exact_heads)

probability_more_than_two_heads = (
    1 - stats.binom.pmf(0, n=10, p=0.5)
    - stats.binom.pmf(1, n=10, p=0.5)
    - stats.binom.pmf(2, n=10, p=0.5)
)

print("Probability of getting more than 2 heads")
print(probability_more_than_two_heads)
