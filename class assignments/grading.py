def grading ():
    name = input("What is your name? ")

    print(f"Hello {name}, enter your marks for the following 5 subjects:")
    maths = int(input("Maths: "))
    english = int(input("English: "))
    kiswahili = int(input("Kiswahili: "))
    physics = int(input("Physics: "))
    chemistry = int(input("Chemistry: "))

    if maths <0 or maths > 100 or english <0 or english > 100 or kiswahili <0 or kiswahili > 100 or physics <0 or physics > 100 or chemistry <0 or chemistry > 100:
        print("Invalid marks")
        return

    total = maths + english + kiswahili + physics + chemistry
    average = total / 5

    if average < 39 and average > 0:
        grade = "D"
    elif average < 59:
        grade = "C"
    elif average < 69:
        grade = "B"
    elif average < 1 and average > 100:
        print("Invalid marks")
    else:
        grade = "A"

    print(f"Hello {name}, your average is {average}, total is {total} and your grade is {grade}.")

grading()
