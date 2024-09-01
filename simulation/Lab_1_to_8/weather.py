P = [[0.8, 0.2],
     [0.6, 0.4]]

# Initial state vector (today is not rainy)
initial_state = [1, 0]  # [P(Not Rainy today), P(Rainy today)]

# Function to perform matrix multiplication
def matrix_vector_multiply(matrix, vector):
    result = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
    return result

state_tomorrow = matrix_vector_multiply(P, initial_state)

state_day_after_tomorrow = matrix_vector_multiply(P, state_tomorrow)

prob_not_rainy_day_after_tomorrow = state_day_after_tomorrow[0]

print(f"The probability that it will not rain the day after tomorrow if today is not rainy is: {prob_not_rainy_day_after_tomorrow:.2f}")