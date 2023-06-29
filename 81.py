try:
    fr=open("STUDENT.txt","r",encoding="utf-8")
    print(fr.read())
except FileNotFoundError :
    print("หาไฟล์ไม่พบ")