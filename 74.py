def hanoi(m,p,r,l):
    if(m==0):
        return
    hanoi(m-1,p,r,l)
    print("จานที่  = ",p,"จาก = ",r,"ไป = ",l)
    hanoi(m-1,l,p,r)

hanoi(4,"A","B","C")