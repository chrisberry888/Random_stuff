def interest_calculator(principal, deposit_amount, deposits_per_year, apr, compounds_per_year, years=30):
    balance_from_deposits = principal
    interest_from_deposits = 0
    interest_from_interest = 0
    days_per_deposit = 365//deposits_per_year + 1
    days_per_compound = 365//compounds_per_year + 1


    has_interest_surpassed_deposits = False
    for year in range(years):
        for day in range(365):
            if day % days_per_compound == 0:
                interest_from_interest += (interest_from_interest + interest_from_deposits) * apr/compounds_per_year
                interest_from_deposits += balance_from_deposits * apr/compounds_per_year
            if day % days_per_deposit == 0:
                balance_from_deposits += deposit_amount
        
        if not has_interest_surpassed_deposits and balance_from_deposits < (interest_from_deposits + interest_from_interest):
            has_interest_surpassed_deposits = True
            print(f"Money from interest surpassed money from deposits after {year} years and {day} days.")

    print("\nSUMMARY:")
    print(f"Total balance after {years} years: ${balance_from_deposits+interest_from_deposits+interest_from_interest}")
    print(f"Total balance from all deposits: ${balance_from_deposits}")
    print(f"Total balance from interest: ${interest_from_deposits + interest_from_interest}")
    print(f"Total balance from interest accrued solely from interest balance: ${interest_from_interest}")

interest_calculator(0, 580, 12, .10, 2)