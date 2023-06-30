while True:
    try:
        number1=int(input("ใส่ตัวเลข 1 :"))
        number2=int(input("ใส่ตัวเลข 2 :"))
        if number1 ==0 and number2 ==0:
            break
        result=number1/number2
        print(result)
    except ValueError:
        print("ใส่ตัวเลข")
    except ZeroDivisionError:
        print("ห้ามหารด้วยศูนย์")
    finally :
        print("ทำงานต่อไป")
