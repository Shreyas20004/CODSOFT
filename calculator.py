cont = True

while cont == True :
    num1 =int( input("Enter the first number:"))
    num2 =int(input("Enter the Second number:"))
    
    print("*****Menu*****")
    print("Choose:1.Add,2.Multiply,3.Subtract,4.Divide")
    
    ch = int(input("Enter choice:"))
    if int(ch) < int(5) and int(ch)>int(0) :
        
        if ch == int(1):
            c = num1 + num2
            print(c)
        if ch == int(2):
            c = num1*num2
            print(c)
        if ch == int(3):
            c = num1-num2
            print(c)
        if ch == int(4):
            c = num1/num2
            print(c)
    else:
        print("Invalid Choice!")

    
    if not input("do you want to continue?(y/n):").lower() =="y":
        cont=False
    
print("thankyou")