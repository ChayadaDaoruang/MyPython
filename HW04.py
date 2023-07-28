#program to calculate total legs of animal in the farm

chicken = int(input("How many chicken : "))
cow = int(input("How many cow : "))
pig = int(input("How many pig : "))
total_legs = (chicken*2)+(cow*4)+(pig*4)
print(" This farm have : ",total_legs,"legs")