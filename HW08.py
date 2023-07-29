test_1 = int(input("Enter score for test 1 :"))
test_2 = int(input("Enter score for test 2 :"))
test_3 = int(input("Enter score for test 3 :"))

average = (test_1+test_2+test_3)/3
print("the average score is",average)

if average > 95 :
    print("congratulations!")
    print("that is the great average!")
