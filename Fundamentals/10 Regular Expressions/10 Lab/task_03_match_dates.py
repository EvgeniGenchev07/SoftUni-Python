import re

pattern = r"\b(?P<Day>\d{2})(?P<separator>[-\./])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"
text = input()
valid_dates = re.finditer(pattern, text)
for date in valid_dates:
    current_date = date.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")


################################################   Task Description   ################################################
# 3. Match Dates
# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". 
# Use capturing groups in your regular expression.
