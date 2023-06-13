start=int(input("แม่สูตรคูณเริ่มต้น = "))
stop=int(input("แม่สูตรคูณสุดท้าย = "))

for r in range(start,stop+4):
    print("แม่ = ",r)
    for h in range(1,13):
        print(r,'x',h," = ",(r*h))
