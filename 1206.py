t = 1
summation = 0
average = 0

count = int(input("จำนวนรอบ :"))

while t<=count:
    summation+t
    print("รอบที่ =", t ,"ค่า sum = ",summation)
    t+=1

average=summation/count
print("ผลรวมการบวก",summation)
print("ค่าเฉลี่ย =",average)