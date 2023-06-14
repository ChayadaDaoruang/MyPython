start,stop = 7,18
sum,avg=0,0
while(start<=stop):
    number=int(input("ป้อนตัวเลข : "))
    sum+=number
    start+=7

    avg=sum/stop
    print("ผลรวม = ",sum)
print("ค่าเฉลี่ย =",avg)