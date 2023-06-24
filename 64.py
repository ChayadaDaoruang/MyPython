def randomNumber(y):
    if y == "400" :
      print("ได้เงิน")
      return 4000
    else :
       print("ไม่ได้เงิน")
       return 0


money=randomNumber("400")
y =600
result=money - y
print("เงินค่าจ้าง =",money)
print("เงินทั้งหมดที่จะได้ =",result)

