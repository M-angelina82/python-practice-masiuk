name = "Angelina"
surname = "Masiuk"
group = "IT-31"

print(f"{name} {surname}")

vowels = 0
consonants = 0

for letter in name + surname:
    if letter.lower() in "aeiouy":
        vowels += 1
    else:
        consonants += 1

total_letters = len(name + surname)

print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {total_letters}")