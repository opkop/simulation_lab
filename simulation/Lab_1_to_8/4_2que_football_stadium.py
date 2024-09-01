def main():
    # Define the rates
    arrival_rate = 1.0  # λ = 1 customer per minute
    service_rate = 3.0  # μ = 3 customers per minute (1 customer per 20 seconds)

    # Calculate the utilization factor
    rho = arrival_rate / service_rate

    # Calculate the expected time in the system (W)
    W = 1.0 / (service_rate - arrival_rate)  # in minutes

    # Calculate the total time spent to reach the seat
    time_to_seat = W + 1.5  # in minutes

    print("Expected time spent in the system (waiting + service): {:.2f} minutes".format(W))
    print("Total time spent to be seated: {:.2f} minutes".format(time_to_seat))

    # Check if the fan will be seated in time if they arrive 2 minutes before the game starts
    if time_to_seat <= 2.0:
        print("The fan can expect to be seated in time for the kick-off.")
    else:
        print("The fan will not be seated in time for the kick-off.")

if __name__ == "__main__":
    main()
