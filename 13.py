weight = int(input("น้ำหนัก 48 (kg)"))
high = int(input("สูง 155 (cm)"))

#process
#cm => m
high/=100
#calculate bml
#output
print("BMI = ",weight//(high**2))