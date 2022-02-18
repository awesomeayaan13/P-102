
while True:
    print("1=Addition")
    print("2=Subtraction")
    print("3=Multiplication")
    print("4=Division")
    print("Press q to escape")


    enter = input("Enter your choice:")

    if enter == "q" or enter == "Q":
        break

    num1 = float(input("Enter Number 1:"))
    num2 = float(input("Enter Number 2:"))

    if enter == "1":
        print(num1, "+", num2, "=",(num1+num2))
    elif enter == "2":
        print(num1, "-", num2, "=",(num1-num2))
    elif enter == "3":
        print(num1, "*", num2, "=",(num1*num2))
    elif enter == "4":
        if num2 == 0.0:
            print("portal to the fifth dimension opened")
        else:
            print(num1, "/", num2, "=",(num1/num2)) 
    else:
        print("can you read?")
    print()