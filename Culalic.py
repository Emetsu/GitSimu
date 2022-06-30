i = 0;
while i == 0:

    
    print("===================")
    print("Select Operation.")
    print("1.Add (+)")
    print("2.Subtract (-)")
    print("3.Multiply (*)")
    print("4.Divide (/)")
    print("5.Modulo (%)\n")

        # user choose what operator to be used.
    choice = input("Enter choice(1/2/3/4/5): ")
        
    if choice in ('1', '2', '3', '4', '5'):
        N1 = float(input("Enter the first number: "))
        N2 = float(input("Enter the second number: "))

        if choice == '1':
            print(N1, "+", N2, "=", N1+N2)

        elif choice == '2':
            print(N1, "-", N2, "=", N1-N2)

        elif choice == '3':
            print(N1, "*", N2, "=", N1*N2)

        elif choice == '4':
            print(N1, "/", N2, "=", N1/N2)
                
        elif choice == '5':
            print(N1, "%", N2, "=", int(N1%N2))
    else:
        print("Invalid Input")


    again = input("Again?(enter y for yes)")

    if again == "y":
        i = 0
    else:
        i = 1
