"""
you are developing a health app and need to improve a python program that calculate the BMI of ur body.
ur program will calculate and describe the health condition in categories following
underweight : BMI <18.5
normal weight : 25 <= BMI <30
obese: BMI >= 30
"""

height = float(input("Enter height(in meter ) : "))
weight = int(input("Enter weight (in kg) : "))
BMI = weight/ ( height * height)

if BMI < 18.5:
    print("underweight ")

elif 18.5 <= BMI < 25:
    print("normal weight ")

elif 25 <= BMI <30:
    print("overweight ")

elif BMI >= 30:
    print("obese")

print(BMI)

#end
