number=int(input("ขนาด = ")) #5 => 0,1,2,3,4
number2=int(input("แถว = "))

for row in range(number) :
    for column in range(number):
        print("*",end="")
    print(" ")