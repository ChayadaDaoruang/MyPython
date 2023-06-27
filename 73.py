data={"191":"เหตุด่วน","1669":"รถพยาบาล"}

def searcNumber(message):
    for key,value in data.items():
        if value==message:
            print("เบอร์ติดต่อ =",key)
        else :
            print("ไม่มีข้อมูล")
            return
        
message=input("ใส่ข้อมูล =")
searcNumber(message)
