def calculate_mm1_queue(arrival_rate, service_rate):
    # Calculate the utilization factor (ρ)
    rho = arrival_rate / service_rate

    # Calculate the probability that the system is empty (P0)
    P0 = 1 - rho

    # Calculate the expected number of customers in the system (L)
    L = arrival_rate / (service_rate - arrival_rate)

    # Calculate the expected number of customers in the queue (Lq)
    Lq = (arrival_rate**2) / (service_rate * (service_rate - arrival_rate))

    # Calculate the expected time a customer spends in the system (W)
    W = 1 / (service_rate - arrival_rate)

    # Calculate the expected time a customer spends waiting in the queue (Wq)
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))

    # Print the results
    print("Utilization factor (ρ): {:.4f}".format(rho))
    print("Probability that the system is empty (P0): {:.4f}".format(P0))
    print("Expected number of customers in the system (L): {:.4f}".format(L))
    print("Expected number of customers in the queue (Lq): {:.4f}".format(Lq))
    print("Expected time a customer spends in the system (W): {:.4f} minutes".format(W))
    print("Expected time a customer spends waiting in the queue (Wq): {:.4f} minutes".format(Wq))

if __name__ == "__main__":
    # Input values for arrival rate and service rate
    arrival_rate = float(input("Enter the arrival rate (λ) in customers per minute: "))
    service_rate = float(input("Enter the service rate (μ) in customers per minute: "))

    # Calculate and display the measures of the M/M/1 queue
    calculate_mm1_queue(arrival_rate, service_rate)
