def summation(number):
    total,avg=0,0
    for o in number :
        total+=o
    avg=total/len(number)
    return total,avg

c=[2,4,6]
y,z=summation(c)
print(y)
print(z)