# Task 6, Masiuk, IT-31

name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_in_range = 18 <= age <= 60
age_is_even = age % 2 == 0
both_conditions = age_in_range and age_is_even
at_least_one_condition = age_in_range or age_is_even
years_to_60 = 60 - age

print(f"\nHello, {name}!")
print(f"Age: {age}")
print(f"Age is from 18 to 60 inclusive: {age_in_range}")
print(f"Age is even: {age_is_even}")
print(f"Age is from 18 to 60 and even: {both_conditions}")
print(f"At least one condition is true: {at_least_one_condition}")
print(f"Years until 60: {years_to_60}")