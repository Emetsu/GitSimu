i = 0;
while i == 0:

    
    print("===================")
    print("Select operation.")
    print("1.Add (+)")
    print("2.Subtract (-)")
    print("3.Multiply (*)")
    print("4.Divide (/)")
   

        # user choose what operator to be used.
    choice = input("Enter choice(1/2/3/4: ")
        
    if choice in ('1', '2', '3', '4',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", num1+num2)

        elif choice == '2':
            print(num1, "-", num2, "=", num1-num2)

        elif choice == '3':
            print(num1, "*", num2, "=", num1*num2)

        elif choice == '4':
            print(num1, "/", num2, "=", num1/num2)
                
    else:
        print("Invalid Input")


    again = input("Again?(enter y for yes)")

    if again == "y":
        i = 0
    else:
        i = 1
