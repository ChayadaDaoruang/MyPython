#Assignment หาค่ามากที่สุด / ต่ำสุด / ผลรวม
number=[]
while True :
    y=int(input("ใส่ตัวเลข :"))
    if y<0:
        break
    number.append(y)

print(number)
print("ค่าที่น้อยที่สุด คือ",min(number))
print("ค่าที่น้อยที่สุด คือ",max(number))
print("ผลรวม คือ",sum(number))
