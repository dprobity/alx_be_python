# pattern_drawing.py

# Prompt the user for a positive integer
row = int(input("Enter the size of the pattern: "))

# Validate that the input is a positive integer
if row <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through rows
    j = 0
    while j < row:
        # Use a for loop to print asterisks for each row
        for i in range(row):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        j += 1
