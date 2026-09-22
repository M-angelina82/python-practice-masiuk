# Task 4, Masiuk, IT-31

a = 1
b = 1
surname = "Masiuk"
c = len(surname)

first_result = a < c
second_result = c > b
third_result = a <= b <= c
fourth_result = a != b
fifth_result = a + b >= c
sixth_result = c <= a + b

print(f"a < c = {first_result}, type = {type(first_result)}")
print(f"c > b = {second_result}, type = {type(second_result)}")
print(f"a <= b <= c = {third_result}, type = {type(third_result)}")
print(f"a != b = {fourth_result}, type = {type(fourth_result)}")
print(f"a + b >= c = {fifth_result}, type = {type(fifth_result)}")
print(f"c <= a + b = {sixth_result}, type = {type(sixth_result)}")