def factorial(n):
    fac=1
    for i in range(1,n + 1):
       fac=fac*i
    return fac
       
while True:
    try:
        num=int(input("\nEnter a number to get the factorial: "))
        print("Your number is", num)
        
        if num < 0:
            print("Sorry, No factorial for negative number. Enter a positive number\n")
       
        elif num == 0:
            print("The factorial of ", num, " is 1")
       
        else:
            print("The factorial of", num, "is",factorial(num))
    
    except ValueError:
        print("Not a valid number. please enter a number")