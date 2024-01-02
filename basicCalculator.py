num1,num2 = [int(x) for x in input("Enter the two numbers separated by space :").split()]
list_operators = ['+','-','/','*']
choice = int(input("Type 0 for addition\n1 for subtraction\n2 for division\n3 for multiplication\nEnter the choice : "))
result = 0
if choice == 0:
    result = num1  + num2
    print(f"The result for {num1} {list_operators[0]} {num2} is {result}")
elif choice == 1:
    result = num1 - num2
    print(f"The result for {num1} {list_operators[1]} {num2} is {result}")
elif choice == 2:
    result = num1/num2
    print(f"The result for {num1} {list_operators[2]} {num2} is {result}")
elif choice == 3:
    result = num1*num2
    print(f"The result for {num1} {list_operators[3]} {num2} is {result}")
else:
    print("Invalid opeartion")

