try:
 a = int(input("Enter a:"))
 b = int(input("Enter b:"))
 c = a/b
except:
  print("Can't divide with zero")
print('this non error') # try-expection not stop code
# give exception and run next lines 