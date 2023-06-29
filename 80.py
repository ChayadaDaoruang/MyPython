while True:
    try:
        name=input("ชื่อผู้ใช้ :")
        if name =="meaw":
            raise Exception("บันทึกชื่อในระบบแล้ส")
        
        number1=int(input("ใส่ตัวเลข 1 :"))
        number2=int(input("ใส่ตัวเลข 2 :"))
        if number1<0 or number2<0:
            break
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")
        
        result=number1/number2
        print(result)
    except Exception as e:
        print(e)