height = float(input("What is your height in meters?"))

weight = int(input("What is your weight in kilograms?"))

bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"{bmi}, underwieght")
elif bmi < 25:
    print(f"{bmi}, normal")
elif bmi < 30:
    print(f"{bmi}, slight overweight")
elif bmi <= 35:
    print(f"{bmi}, obese")
else:
    print(f"{bmi}, clinically obese")