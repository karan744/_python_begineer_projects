def add():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    s=a+b
    print("Sum= ",s)
    return 0

def substract():
    a=int(input("Enter 1st number to be substracted by 2nd number: "))
    b=int(input("Enter 2nd number: "))
    sub=a-b
    print("Substraction= ",sub)
    return 0

def multiply():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    m=a*b
    print("Product= ",m)
    return 0

def division():
    try:
        a=int(input("Enter 1st number to be divided by 2nd number: "))
        b=int(input("Enter 2nd number: "))
        div=a/b
        print("Division= ",div)
    except ZeroDivisonError:
        print("Enter again: ")
        return 0
        
print("Enter 1 for addition")
print("Enter 2 for substraction")
print("Enter 3 for multiplication")
print("Enter 4 for divison")
c=int(input("Enter your choice: "))
if(c==1):
    add()
elif(c==2):
    substract()
elif(c==3):
    multiply()
elif(c==4):
    division()
else: 
    c=int(input("Run the program again and rechoice !!"))
