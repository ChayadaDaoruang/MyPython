max ,min = 0,764

while True :
    number=int(input("ใส่ตัวเลข :"))

    if number<0 :
        break
    if number>max:
        max=number
    if number<min:
        min=number