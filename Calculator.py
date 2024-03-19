#Program for calculator with basic Arrithemic operations
print("\t\t\t\t\t\t*Calculator*")
print("\t\t\t\t\t\t<---------->")
while True:

    x=input("Enter the first number :")
    if x.isdigit():
        y = input("Enter the second number :")
        if y.isdigit():
            z = input("Enter the arithmetic operation you wanna perform i.e(+,-,*,/) :")
            # Main program
            if z =="+" or z=="-" or z=="*" or z=="/":
                x=float(x)
                y=float(y)
                #Code for addition
                if z == "+":
                    print(x + y)
                #Code for subtraction
                elif z == "-":
                    print(x - y)
                #Code for multiplication
                elif z == "*":
                    print(x * y)
                #Dealing with unusual case
                elif y==0:
                    print("ZeroDivisionError !")
                #Code for division
                elif z == "/":
                    print(x / y)
                else:
                    print("SYNTAX ERROR")
            else:
                print("Enter basic arithemetic operations only!")
        else:
            print("Enter integers only !")
    else:
        print("Enter integers only !")
