TAB_CHISQUARE_4D = 9.49
TAB_CHISQUARE_3D = 5.99

def poker_test():
    num = int(input("Please choose your test:\n 1. Three digit poker test\n 2. Four digit poker test\n"))

    if num not in [1, 2]:
        print("Please choose either 1 or 2")
        return

    n = int(input("How many numbers did you generate: "))

    CAL_CHISQUARE = 0.0

    if num == 2:
        four_diff = int(input("\nEnter the observed frequencies of:\nFour different digits: "))
        four_of_a_kind = int(input("Four same digits: "))
        three_of_a_kind = int(input("Three of a kind: "))
        one_pair = int(input("One Pair: "))
        two_pair = int(input("Two Pair: "))

        if (four_diff + four_of_a_kind + three_of_a_kind + one_pair + two_pair) != n:
            print(f"\nThe sum is not equal to {n}")
            return
        
        probabilities_4d = [0.504, 0.001, 0.036, 0.432, 0.027]
        observed_frequency_4d = [four_diff, four_of_a_kind, three_of_a_kind, one_pair, two_pair]
        expected_frequency_4d = [prob * n for prob in probabilities_4d]

        print("----------------------------------------------------------------------")
        print("\nThe Observed frequencies are:")
        for freq in observed_frequency_4d:
            print(f"\t{freq}", end="")
        
        print("\nAnd their respective expected frequencies are:")
        for freq in expected_frequency_4d:
            print(f"\t{int(freq)}", end="")
        
        for obs, exp in zip(observed_frequency_4d, expected_frequency_4d):
            CAL_CHISQUARE += ((obs - exp) ** 2) / exp
        
        print("\n----------------------------------------------------------------------")
        print(f"The sum of calculated chi square statistics is : {CAL_CHISQUARE}")
        print(f"The tabulated value for chi-square is {TAB_CHISQUARE_4D}")
        
        if CAL_CHISQUARE <= TAB_CHISQUARE_4D:
            print("\n\nSo, the generated random numbers are independent.")
        else:
            print("\n\nSo, the generated random numbers are not independent.")
    
    elif num == 1:
        three_diff = int(input("\nEnter the observed frequencies of:\nThree different digits: "))
        three_of_a_kind = int(input("Three same digits: "))
        one_pair = int(input("One Pair: "))

        if (three_diff + three_of_a_kind + one_pair) != n:
            print(f"\nThe sum is not equal to {n}")
            return
        
        probabilities_3d = [0.72, 0.01, 0.27]
        observed_frequency_3d = [three_diff, three_of_a_kind, one_pair]
        expected_frequency_3d = [prob * n for prob in probabilities_3d]

        print("----------------------------------------------------------------------")
        print("The Observed frequencies are:")
        for freq in observed_frequency_3d:
            print(f"\t{freq}", end="")
        
        print("\nAnd their respective expected frequencies are:")
        for freq in expected_frequency_3d:
            print(f"\t{int(freq)}", end="")
        
        for obs, exp in zip(observed_frequency_3d, expected_frequency_3d):
            CAL_CHISQUARE += ((obs - exp) ** 2) / exp
        
        print(f"\nThe sum of calculated chi square statistics is : {CAL_CHISQUARE}")
        print(f"The tabulated value for chi-square is {TAB_CHISQUARE_3D}")
        
        if CAL_CHISQUARE <= TAB_CHISQUARE_3D:
            print(f"\nSo,{CAL_CHISQUARE} <= {TAB_CHISQUARE_3D} the generated random numbers are independent.")
        else:
            print(f"\nSo,{CAL_CHISQUARE} > {TAB_CHISQUARE_3D} the generated random numbers are not independent.")

if __name__ == "__main__":
    poker_test()
