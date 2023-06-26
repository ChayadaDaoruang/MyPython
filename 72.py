def checkString(message):
    result ={"UPPER":0,"LOWER":0}
    for v in message:
        if v.isupper():
            result["UPPER"]+=1
        elif v.islower():
            result["LOWER"]+=1
        else:
            pass
    return result

message=input("input your message :")
x=checkString(message)
print(x)
