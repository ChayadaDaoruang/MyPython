def add(*number):
    sum=0
    for e in range(len(number)):
        sum+=number[e]
    print(sum)

def displayData(**item):
    print(item)

displayData(fname="meaw",Iname="chayada",age=14,city="ปทุมธานี")
