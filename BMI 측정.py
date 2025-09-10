def BMI():
    bmi = int(input("당신의 bmi는?"))
    if bmi >= 18.5 and bmi <= 24.99:
        print("정상")
    elif bmi > 24.99 and bmi <= 29.99:
        print("과체중")
    elif bmi < 18.5:
        print("저체중")
    else:
        print("비만")
BMI()

