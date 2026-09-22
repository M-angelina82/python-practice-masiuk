# Task 5, Masiuk, IT-31

birth_day = 1

is_positive = birth_day > 0
is_even = birth_day % 2 == 0
is_positive_and_even = is_positive and is_even

print(f"Birth day: {birth_day}")
print(f"Is the birth day positive? {is_positive}")
print(f"Is the birth day even? {is_even}")
print(f"Is the birth day positive and even? {is_positive_and_even}")

birth_month = 1
birth_day_month_product = birth_day * birth_month

product_is_positive = birth_day_month_product > 0
product_is_even = birth_day_month_product % 2 == 0
product_is_positive_and_even = product_is_positive and product_is_even

print(f"\nDay multiplied by month: {birth_day_month_product}")
print(f"Is the product positive? {product_is_positive}")
print(f"Is the product even? {product_is_even}")
print(f"Is the product positive and even? {product_is_positive_and_even}")