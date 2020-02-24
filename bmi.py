weight = input('你的體重是: ')
weight = float(weight)
height = input('你的身高是: ')
height = float(height)
bmi = weight / height**2
bmi = int(bmi)
print('你的BMI值是:', bmi)