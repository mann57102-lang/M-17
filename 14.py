import scipy.stats as stats

## Checkpoint 1
# calculate probability of more than 20
probability_more_than_20 = 1 - stats.poisson.cdf(20, 15)

# print probability of more than 20
print(probability_more_than_20)

## Checkpoint 2
# calculate probability from 17 to 21
probability_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

# print probability from 17 to 21
print(probability_17_to_21)
