import numpy
def function():
  x = input("Enter number x: ")
  y = input("Enter number y: ")
  x = int(x)
  y = int(y)
  exp = x**y
  print("x**y = " + str(exp))
  log = numpy.log2(x)
  print("log2(x) = " + str(log))
  my_id = 79957
  print("My student ID is " + str(my_id))

function()