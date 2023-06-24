def randomNumber(k):
    if len(k)<3 :
        return
    
    if k =="100":
        print("ถูกหวย")
        return 2000
    else :
        print("ไม่ถูก")
        return 0
    
money=randomNumber("800")
print("เงินรางวัล =",money)
