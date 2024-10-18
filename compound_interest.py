import sys

def compound_interest(principal, monthly_contributions, interest_rate, years):
    amount = principal
    for i in range(years):
        amount *= (1 + interest_rate)
        amount += 12 * monthly_contributions
    
    return amount

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python my_file.py <principal> <monthly_contributions> <interest_rate> <years>")
        sys.exit(1)
    
    # Convert arguments to integers (or adjust as needed)
    arg1 = float(sys.argv[1])
    arg2 = float(sys.argv[2])
    arg3 = float(sys.argv[3])
    arg4 = int(sys.argv[4])

    # Call the function with the provided arguments
    ci = compound_interest(arg1, arg2, arg3, arg4)
    print(ci)