import random

def estimate_pi(num_points):
    points_inside_circle = 0
    
    for _ in range(num_points):
        # Generate random x and y coordinates within the square [-1, 1] x [-1, 1]
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Check if the point lies within the quarter unit circle
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
            
    # Approximate pi using the ratio of points inside the circle to total points
    pi_estimate = 4 * points_inside_circle / num_points
    return pi_estimate

# Ask user to input the number of points
num_points = int(input("Enter the number of points for Monte Carlo simulation: "))

# Estimate pi using Monte Carlo simulation
pi_approximation = estimate_pi(num_points)
print("Approximation of pi using Monte Carlo simulation:", pi_approximation)
