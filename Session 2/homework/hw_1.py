Heigh = float(input('chiều cao (cm): '))
Mass = float(input('cân nặng (kg): '))
Heigh_Convert = Heigh/100
BMI = Mass/Heigh_Convert**2

if BMI < 16:
    print('Severely underweight')
elif BMI < 18.5:
    print('Underweight')
elif BMI < 25:
    print('Normal')
elif BMI < 30:
    print('Overweight')
else:
    print('Obese')