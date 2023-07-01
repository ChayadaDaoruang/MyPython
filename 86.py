
import datetime
result=datetime.datetime.now()
newdate=datetime.datetime(2023,6,30,15)
print("เริ่มต้น =",result)
print(result.strftime("Xx"))
print(result.strftime("Xx"))
print(result.strftime("Xc"))

print(result.strftime("%H : %M : %S %p"))
      
print(result.strftime("%j"))

print(result.strftime("%a"))
print(result.strftime("%A"))
print(result.strftime("%w"))
print(result.strftime("%d"))
print(result.strftime("%b"))
print(result.strftime("%B"))

print(result.strftime("%d %A %B"))

print(result.strftime("%d / %M %Y"))