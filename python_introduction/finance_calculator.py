# This script will calculate the users monthly savings based on based on inputted monthly income and exepenses, it will the project this savings over a year, assumming a fixed interest rate, to demonstrate compound intereste's effect on savings

#prompt the user for input

monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))


# Calculating the monthly savings

monthly_savings = monthly_income - monthly_expenses

# Calculating the projected annual savings 

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12  * 0.05)


# Printing the results

print(f"Your monthly savings are ${monthly_savings}. ")
print(f"Projected savings afetr one year, with interest, is: ${projected_annual_savings}.")


