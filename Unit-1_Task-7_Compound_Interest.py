principal_amount_in_rupees = float(input("Enter principal in rupees: "))
rate_of_interest_in_rupees = float(input("Enter rate in percent: "))
time_in_years = float(input("Enter time in years: "))
total_amount_in_rupees = principal_amount_in_rupees * (1 + rate_of_interest_in_rupees / 100) ** time_in_years
compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees
print(f"{compound_interest_in_rupees:.2f}")