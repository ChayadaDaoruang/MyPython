#calculate wages 

pay_rate = int(input("pay rate : "))
hours_work = int(input("hours work : "))

if hours_work > 40 : 
    wages = (pay_rate*40)+((hours_work-40)*(1.5*pay_rate))

else :
    wages = (pay_rate)*(hours_work)

print("total pay",wages)