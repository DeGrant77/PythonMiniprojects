math_grade = int(input("Enter the score you received for Maths:"))
english_grade = int(input("Enter the score you received for English:"))
pe_grade = int(input("Enter the sore you received for PE:"))
sci_grade = int(input("Enter the score you received for Science:"))
art_grade = int(input("Enter the score you received for Art:"))

letgrade = ""
def subject_grade(grade):
    for i in range(93, 101):
        if grade == i:
            letgrade = "A"

    for i in range(90, 93):
        if grade == i:
            letgrade = "A-"
    for i in range(87, 90):
        if grade == i:
            letgrade = "B+"

    for i in range(83, 87):
        if grade == i:
            letgrade = "B"

    for i in range(80, 83):
        if grade == i:
            letgrade = "B-"

    for i in range(77, 80):
        if grade == i:
            letgrade = "C+"


    for i in range(73, 77):
        if grade == i:
            letgrade = "C"
    for i in range(67,70):
        if grade == i:
            letgrade = "D+"

    for i in range(63, 67):
     if grade == i:
        letgrade = "D"

    for i in range(60, 63):
        if grade == i:
            letgrade = "D-"

    for i in range(0, 60):
        if grade == i:
            letgrade = "F"
    if grade > 100 or grade < 0:
        print("None")
    return letgrade

maths = subject_grade(math_grade)
english = subject_grade(english_grade)
PE = subject_grade(pe_grade)
Sci = subject_grade(sci_grade)
art = subject_grade(art_grade)
print("")
print("Your Math score is " + str(math_grade) + ", you got " + maths)
print("Your English score is " + str(english_grade) + ", you got " + english)
print("Your PE score is " + str(pe_grade) + ", you got " + PE)
print("Your Science score is " + str(sci_grade) + ", you got " + Sci)
print("Your Art score is " + str(art_grade) + ", you got " + art)