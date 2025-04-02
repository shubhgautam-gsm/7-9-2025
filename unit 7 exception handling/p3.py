try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print("a / b = %f"%c)
except ZeroDivisionError:
    print("Can't divide by zero")
    print(Exception)
else:
    print("Hi, I am the else block")

print("after error i am print")
