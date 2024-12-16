# This script will calculate the users monthly savings based on based on inputted monthly income and exepenses, it will the project this savings over a year, assumming a fixed interest rate, to demonstrate compound intereste's effect on savings

#prompt the user for input

income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))


# Calculating the monthly savings

monthly_savings = income - expenses

# Calculating the projected annual savings 

projected_annual_savings = savings * 12 + (savings * 12  * 0.05)


# Printing the results

print(f"Your monthly savings are ${savings}. ")
print(f"Projected savings afetr one year, with interest, is: ${projected_annual_savings}.")


