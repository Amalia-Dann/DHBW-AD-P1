Height = float(input("Please type in your height: "))
Weight = float(input("Please type in your weight: "))
m = Height / 100
B = round(float(Weight / m ** 2), 1)
print(B)

if B <= 18.5:
    print("Underweight")
elif (B > 18.5) and (B <= 25):
    print("Normal")
elif (B > 25) and (B <= 30):
    print("Overweight")
else:
    print("Health is at risk!\n Need to lose")
