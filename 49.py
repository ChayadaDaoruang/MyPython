greeting=["สวัสดี","hi","hello","good bye"]
people=["มิ้น","วิว","น้ำปั่น"]
result=[]

result=[x+y for x in greeting for y in people]
print(result)