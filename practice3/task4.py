print("Angelina Masiuk, IT-31")

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    missed = int(input("Enter the number of missed classes: "))

    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    if missed > 16 * 0.30:
        print("Warning: more than 30% of classes were missed. No admission.")
        passed = "failed"
    elif score >= 60:
        passed = "passed"
    else:
        passed = "failed"

    print(f"Score: {score}, ECTS grade: {grade}, Result: {passed}")