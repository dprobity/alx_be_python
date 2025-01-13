# daily_reminder.py

# Ask the user for the task description
task = input("Enter your task: ")

# Ask for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Use Match Case statement to handle different priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = "Invalid priority. Please enter 'high', 'medium', or 'low'."

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder = "Invalid input for time-bound. Please enter 'yes' or 'no'."

# Print the final reminder
print(reminder)
