import math

print("Select operation to perform: ")
print("1. PERFORM ADDITION")
print("2. PERFORM SUBTRACTION")
print("3. PERFORM MULTIPLICATION")
print("4. PERFORM DIVISION")
print("5. PERFORM SQUARE ROOT")
print("6. PERFORM EXPONENT")

operation = input()

if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The result is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The result is " + str(int(num1) - int(num2)))
elif operation== "3":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The result is " + str(int(num1) * int(num2)))
elif operation== "4":
    num1 = input("Enter first number: ")
    num2 = input ("Enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5":
    num = int(input("Enter number: "))
    print("The result is %f " %(math.sqrt(num)) )
elif operation == "6":
    num = int(input("Enter number: "))
    print("The result is %d " %(math.pow(num, 2)) )
else:
    print("Invalid Input")