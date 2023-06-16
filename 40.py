import random
myrandom = random.randrange(1,7) # 1 -6
P=1
correct=False
print("มีโฮกาสตอบ 35 ครั้ง \n")
print(myrandom)
while True:
    number=int(input("ใส่คำตอบ = "))
    correct=(number==myrandom)
    if not correct :
        if(number>myrandom):
            print("น้อยกว่า")
        if(number>myrandom):
            print("มากกว่า")

    if correct :
        print("ตอบถูกรับไป 0 บาท")
        break
    if number<0 or P==3:
        break
    P+=1
        