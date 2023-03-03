import datetime

# Ask for user's date of birth and gender
dob = input("Enter your date of birth (format: YYYY): ")
gender = input("Enter your gender (M/F): ")

# Convert dob string to a datetime object
dob = datetime.datetime.strptime(dob, '%Y')

# Calculate the year the person would have been 5, 15, and 25 years old
year_5 = dob.year + 5
year_15 = dob.year + 15
year_25 = dob.year + 25

# Print the results
print("If you were born on {}, you would have been:".format(dob.strftime('%Y')))
print("- 5 years old in the year {}".format(year_5))
print("- 15 years old in the year {}".format(year_15))
print("- 25 years old in the year {}".format(year_25))
