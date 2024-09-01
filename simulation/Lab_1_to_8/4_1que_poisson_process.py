def main():
    # Define the rates
    LAMBDA = 1.0 / 10.0  # Arrival rate: 1 customer every 10 minutes
    MU = 1.0 / 5.0       # Service rate: 1 customer every 5 minutes

    # Calculate the utilization factor
    rho = LAMBDA / MU

    # a. Probability that a customer will not have to wait at the counter
    P0 = 1 - rho
    print("Probability that a customer will not have to wait: {:.4f}".format(P0))

    # b. Expected number of customers in the bank
    L = LAMBDA / (MU - LAMBDA)
    print("Expected number of customers in the bank: {:.4f}".format(L))

    # c. Time a customer expects to spend in the bank
    W = 1 / (MU - LAMBDA)
    print("Time a customer expects to spend in the bank (in minutes): {:.4f}".format(W))

if __name__ == "__main__":
    main()
