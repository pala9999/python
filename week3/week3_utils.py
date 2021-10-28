# ## Q1. Create a function named custom_function.
# def custom_function(n):
#     for i in range(1,11):
#         print(n,"*",i,"=",n*i)
  
# custom_function(5)
#################################################################################
## Q2. Write the function call with 2 arguments fname, lname 
## that returns fname+lname, print returned value.

# def f_name (fname,lname):
#     return fname+lname
# print(f_name("Prasanth","Ala"))
#################################################################################
# # Q3a. Create a function call with arguments 
# def q3(*args):
#     a1=args[0]
#     a2=args[1]
#     return  a1+a2
# arg1=input("fname:\n")
# arg2=input("lname:\n")
# print(q3(arg1,arg2))
#################################################################################
# # Q3b. Create a function call with  keyword arguments.
# def q3(**args):
#     a1=args["fname"]
#     a2=args["lname"]
#     return a1+a2

# arg1=input("fname:\n")
# arg2=input("lname:\n")

# print(q3(fname=arg1, lname=arg2))
#################################################################################
# # Q4. Create two functions where first function accepts a dictionary 
# # as keyword argument and for each KEY in that dictionary 
# # call the second function with argument as VALUE of that KEY.
# # The second function should validate if key is Alphabets only or 
# # Alphanumeric or Numeric and print "VALUE, is of type Alphabets" 
# # or "VALUE, is of type Alphanumeric" or "VALUE, is of type Numeric" respectively.
# def check_string(str1):
#     if str1.isnumeric() == True:
#         return "Input VALUE is Numeric"
#     elif str1.isalpha() == True:
#         return "Input VALUE is Alphabets"
#     elif str1.isalnum() == True:
#         return "Input VALUE is Alphanumeric"

# def read_srt(**args):
#     d=dict()
#     a1=args["string1"]
#     a2=args["string2"]
#     a3=args["string3"]
#     d[a1]=check_string(a1) 
#     d[a2]=check_string(a2)
#     d[a3]=check_string(a3)
#     return d 

# arg1=input("Enter 1st numbers or alpha or alphanumeric string:\n")
# arg2=input("Enter 2nd numbers or alpha or alphanumeric string:\n")
# arg3=input("Enter 3nd numbers or alpha or alphanumeric string:\n")

# print(read_srt(string1=arg1,string2=arg2,string3=arg3))        

# Q5. Find the factorial of an integer through recursion.

def fact(n):
    if n == 1:
        return n
    else:   
        return  n*fact(n-1) 
print(fact(4))             