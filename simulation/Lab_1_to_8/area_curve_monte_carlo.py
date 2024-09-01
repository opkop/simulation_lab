import random

def f(x):
    # Define the function whose area under the curve is to be estimated
    return x**2  # Example function: f(x) = x^2

def monte_carlo_area_estimate(num_points, x_min, x_max, y_min, y_max):
    points_below_curve = 0
    
    for _ in range(num_points):
        # Generate random x and y coordinates within the bounding box
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        
        # Check if the point lies below the curve
        if y <= f(x):
            points_below_curve += 1
            
    # Estimate the area under the curve using the ratio of points below the curve to total points
    total_area_of_box = (x_max - x_min) * (y_max - y_min)
    area_under_curve = total_area_of_box * (points_below_curve / num_points)
    return area_under_curve

# Define the bounds of the bounding box
x_min = 0  # Minimum x-value
x_max = 1  # Maximum x-value
y_min = 0  # Minimum y-value (assuming the curve lies above the x-axis)
y_max = 1  # Maximum y-value (assuming the curve lies below the y_max)

# Number of points to generate
num_points = int(input("Enter the number of points for Monte Carlo simulation: "))

# Estimate the area under the curve using Monte Carlo simulation
area_estimate = monte_carlo_area_estimate(num_points, x_min, x_max, y_min, y_max)
print("Estimated area under the curve using Monte Carlo simulation:", area_estimate)
