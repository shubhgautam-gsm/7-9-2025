# By using args* the variable-length arguments, we can pass any number of arguments.
def printme(*names):
 print("type of passed argument is ",type(names))
 print("printing the passed arguments...")
 for name in names:
  print(name)

printme("john","David","smith","nick")

