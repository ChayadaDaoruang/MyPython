weight=int(input("ใส่น้ำหนัก (kg) : "))
high =int(input("ใส่ส่วนสูง (cm) : "))/100
bmi = weight/(high**2)

if bmi>=0 and bmi<18.0 :
    result="ผอม"
elif bmi>=18.5 and bmi<=22.9 :
    result="สมส่วน"
elif bmi>=23.0 and bmi<=24.9 :
    result="หนักเกิน"
elif bmi>=25.0 and bmi<=29.9 :
    result="อ้วนเวล 1"
elif bmi>=30 :
    result="อ้วนเวล 2"
else :
    result="ไม่ทราบค่า"

print("ค่า bmi = ","สรุปคือ =",result)