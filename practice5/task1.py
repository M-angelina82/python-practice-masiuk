# Task 1, Masiuk, IT-31

birth_day = 1
height_meters = 1.65
full_name = "Angelina Masiuk"
has_scholarship = False

print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"height_meters = {height_meters}, type = {type(height_meters)}")
print(f"full_name = {full_name}, type = {type(full_name)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

print("\nBefore type change:")
print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

birth_day = "first"
has_scholarship = 0.0

print("\nAfter type change:")
print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")

print(f"String concatenation: {birth_day + ' day'}")