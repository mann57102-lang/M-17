import numpy
import matplotlib.pyplot as plt

# number of samples
sample_sizes = [1, 10, 50, 100]

# list of sample means
sample_means = []

# Generating 1, 10, 50, 100 random numbers from -40 to 40
# taking their mean and appending it to list sample_means.
for sample_size in sample_sizes:

    # Generating seed so that we can get same result
    # every time the loop is run...
    numpy.random.seed(1)

    generated_means = [
        numpy.mean(numpy.random.randint(-40, 40, sample_size))
        for _ in range(1000)
    ]

    sample_means.append(generated_means)

plot_index = 0

# plotting all the means in one figure
figure, axes = plt.subplots(2, 2, figsize=(6, 6))

for row in range(0, 2):
    for column in range(0, 2):

        # Histogram for each sample stored in sample_means
        axes[row, column].hist(sample_means[plot_index], 10, density=True)
        axes[row, column].set_title(label=sample_sizes[plot_index])

        plot_index = plot_index + 1

plt.show()
