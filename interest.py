import sys

def interest_calculator(principal, interest_rate, compounds_per_year, years, verbose=True):
    current_amount = principal
    print(f"Principal = {principal}")
    print()
    print("Amount after:")
    for year in range(years):
        for comp in range(compounds_per_year):
            current_amount *= (1 + (interest_rate / compounds_per_year))
        print(f"Year {year + 1}: ${current_amount}")

if __name__ == '__main__':
    principal = float(sys.argv[1])
    interest_rate = float(sys.argv[2])
    compounds_per_year = int(sys.argv[3])
    years = int(sys.argv[4])
    interest_calculator(principal, interest_rate, compounds_per_year, years, True)