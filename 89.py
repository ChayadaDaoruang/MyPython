import random

ATM_PASSWORD="MOMOMU"
result=""

while result!=ATM_PASSWORD :
    result=""
    for letter in range(len(ATM_PASSWORD)):
        list_number=random.choice("678huup")
        result=''.join(list_number)+str(result)
        print("SEARCH=",result)
print("CRACK PASSWORD IS",result)