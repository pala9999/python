from  memoization import cached
@cached(max_size=500)

def fib(n):
   if (n == 1) or (n == 2):
      return 1
   elif (n > 2):
      return fib(n-1) + fib(n-2)
print(fib(100))

# import os
# print(os.path.isfile("python\week1\zipCode.py"))
# print(os.path.exists("C:\Python_Itmunk\python\week1\week1_q3.py"))
# print(os.walk("C:\Python_Itmunk\python\week1\week1_q3.py"))
# import math
# import pandas
# pip3 list

