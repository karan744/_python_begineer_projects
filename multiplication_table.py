print("MULTIPLICATION TABLE CREATOR!!")
num1=int(input("Enter the number of which you want the multiplication table::"))
num2=int(input("Enter the number upto which you want the table to be::"))
print(f"MULTIPLICATION TABLE OF {num1}!!")
for i in range(1,num2,1):
    print(f"{num2} x {i} = ",num1*i)

