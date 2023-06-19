message=["aa","aab","acb","cca"]
result=[]

for item in message:
    result.append(item.count("a"))
print(result)