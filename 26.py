Temp = input("ป้อนอุณหภูมิ (องศา) : ")

degree= int(Temp[ : -1])
unit = Temp[-1].upper()

if unit=="c":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮต์"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"

print("แปลงตัวเลข = ",Temp,"เป็น",unit_result,"=",result)