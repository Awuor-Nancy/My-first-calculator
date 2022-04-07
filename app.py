#1.ADD
#2.SUBTRACT
#3.MULTIPLY
#4.DIVIDE
#5.QUOTIENT

print("select an operation to perform")
print("1.ADD")
print("2.SUBTRACT")
print("3.MUTIPLY")
print("4.DIVIDE")
print("5.MODULUS")

operation = input()

if operation == "1":
    num1=input("the first number:")
    num2=input("the second number:")
    print("the sum is" + str(int(num1) + int(num2)))
   # code for ADD

elif operation == "2":
    num1 =input("the first number:")
    num2 =input("the second number:")
    print("the difference is" + str(int(num1) - int(num2)))

    #code for SUBTRACT
elif operation == "3":
    num1= input("the first number:")
    num2 = input("the second number:")
    print("the product is" + str(int(num1) * int(num2)))

    #code for MULTIPLY
elif operation == "4":
    num1= input("the first number:")
    num2=("the second number:")
    print("the result is" + str(int(num1) / int(num2)))
    #code for DIVIDE
elif operation == "5":
    num1=input("te first number:")
    num2=input("the second number:")
    print(" the modulus is" + str(int(num1) % int(num2)))
    #code for QUOTIENT 

else :
    print("invalid entry")
