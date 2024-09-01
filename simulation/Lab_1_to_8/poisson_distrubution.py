import random
import math

def poisson_distribution(avg_arrival_rate, x):
    # Calculate the Poisson probability for given x and average arrival rate
    return (math.exp(-avg_arrival_rate) * (avg_arrival_rate ** x)) / math.factorial(x)

def generate_poisson_distribution(avg_arrival_rate, max_x):
    # Generate Poisson distribution for x = 0 to max_x
    poisson_values = []
    for x in range(max_x + 1):
        poisson_values.append(poisson_distribution(avg_arrival_rate, x))
    return poisson_values

# Average arrival rate
lambda_ = 12

# Generate Poisson distribution for x = 0 to 15
poisson_values = generate_poisson_distribution(lambda_, 15)

# Display results
print("x\t Poisson Distribution")
print("-" * 30)
for x, p in enumerate(poisson_values):
    print(f"p(X={x})\t {p}")
