import os
try:
    if os.path.exists("Score.txt"):
        os.remove("Score.txt")
        print("ลบสำเร็จ")
    else :
        print("ไม่พบไฟล์")
except Exception as e:
    print(e)