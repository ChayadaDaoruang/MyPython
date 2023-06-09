number = int(input("จำนวนเงิน :"))

if number>=1000:
    print("1000 Baht = ",number //1000,"ใบ")
    number%=1000
