from datetime import datetime

# Accept separate inputs for year, month, and day from the user
year_input = input("Enter the year (YYYY): ")
month_input = input("Enter the month (e.g., January): ")
day_input = input("Enter the day (DD): ")

# Combine inputs into a single date string
date_input = f"{year_input} {month_input} {day_input}"

# Parse the input date
try:
    date_object = datetime.strptime(date_input, "%Y %B %d")
    # Get the day of the week
    day_of_week = date_object.strftime("%A")
    # Display the day of the week
    print(f"The day of the date {date_input} is {day_of_week}.")
except ValueError:
    print("Invalid date format. Please enter the date correctly.")
