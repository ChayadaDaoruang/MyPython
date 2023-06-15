#ตารางหมากฮอต



number=int(input("ขนาด = "))
for row in range(number):
    for column in range(number):
        if (row+column)%2 == 0 :
            print("c",end="")
        else :
            print("o",end="")

    print(" ")

    