import random

INTERVALS = 10  # number of intervals
tabulated_value = 16.919  # assumed LOS=5% and DF=9

def main():
    x0 = 7  # seed
    a = 5
    c = 3
    m = 100
    n = 100  # size of the sample
    lb = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  # lower bounds of the intervals
    ub = [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]  # upper bounds of the intervals
    observed = [0] * INTERVALS  # observed frequencies
    expected = n // INTERVALS  # expected frequency
    array = []  # to store the random numbers generated
    final = 0
    N = 0

    print("The random numbers are:")

    # Generate random numbers between 0 and 99 using m=100 and mixed congruential method
    for _ in range(n):
        x0 = (a * x0 + c) % m
        array.append(x0)
        print(x0, end=" ")
    print()

    # Calculate observed frequency for each interval
    for num in array:
        for j in range(INTERVALS):
            if lb[j] <= num <= ub[j]:
                observed[j] += 1
                break

    # Calculate N(total frequency), Calculation(((Oi-Ei)^2/Ei)), final
    calculation = []
    for i in range(INTERVALS):
        calc = ((observed[i] - expected) ** 2) / expected
        calculation.append(calc)
        final += calc
        N += observed[i]

    # Display in tabulated format
    print("\n---------------------------------------------------------------------")
    print("S.No \t\t Oi \t\t Ei \t\t((Oi-Ei)*(Oi-Ei))/Ei ")
    print("---------------------------------------------------------------------")
    for i in range(INTERVALS):
        print(f"{i+1} \t\t {observed[i]} \t\t {expected}\t\t {calculation[i]}")
    print("---------------------------------------------------------------------")
    print(f" \t\t{N} \t\t\t\t {final}")

    # Compare tabulated and calculated value and conclude if Ho is accepted
    if final <= tabulated_value:
        print(f"\nThe calculated value = {final} < Tabulated value = {tabulated_value}. "
              "So, the null hypothesis is not rejected and hence the random numbers are uniform.")
    else:
        print(f"\nThe calculated value = {final} > Tabulated value = {tabulated_value}. "
              "So, the null hypothesis is rejected and hence the random numbers are not uniform.")

if __name__ == "__main__":
    main()
