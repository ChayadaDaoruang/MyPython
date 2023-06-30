try:
    fw=open("Score.txt","a",encoding="utf-8")
    for i in range(2):
        name=input("ใส่ข้อความ : ")
        fw.writelines(name+"\n")
    fw.close()
except FileNotFoundError :
    print("หาไฟล์ไม่พบ")
