import scipy.stats as stats

# expected value = 10, probability of observing 6
probability_exactly_six_days = stats.poisson.pmf(6, 10)
print("probability of raining for exactly 6 days :", probability_exactly_six_days)

# expected value = 10, probability of observing 12-14
probability_twelve_to_fourteen_days = (
    stats.poisson.pmf(12, 10)
    + stats.poisson.pmf(13, 10)
    + stats.poisson.pmf(14, 10)
)

print("probability of raining for 12-14 days :", probability_twelve_to_fourteen_days)
