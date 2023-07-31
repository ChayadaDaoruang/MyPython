print ("select operation -")
print (" 1.Add")
print (" 2.subtract ")
print (" 3.multiply") 
print (" 4.divide")
select_operation = int(input("Select operations form 1, 2, 3, 4 : "))
x = int(input("enter first number : "))
y = int(input("enter second number : "))

if select_operation == 1 :
    print (x,"+",y,"=",x+y)

if select_operation == 2 :
    print (x,"-",y,"=",x-y)

if select_operation == 3 :
    print (x,"*",y,"=",x*y)

if select_operation == 4 :
    print (x,"/",y,"=",x/y)




