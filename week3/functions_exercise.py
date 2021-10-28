



# def read_dict_keyword(keyword):
#     dict1={ "drum":"Music instrument",
#             "apple":"fruit",
#             "ball":"123ancd",
#             "cat":"123456"} 
#     print(dict1.get(keyword)) 
# read_dict_keyword("cat")           

# def check_val_type(value):
#     if value.isalpha() == True :
#         print("The value for Dict word",value, "is Alphabets")
#     elif value.isnumber() == True :       
#         print("The value for Dict word",value, "is Numeric")
#     else :
#         print("The value for Dict word",value, "is Alphanumeric")
# check_val_type("valujkhke123")


def check_string(str1):
    if str1.isnumeric() == True:
        return "this is number"
    elif str1.isalpha() == True:
        return "This is alpha"
    elif str1.isalnum() == True:
        return "This is alpha numeric"
print(check_string("aaA"))

# arg1="ANCdss1"
# print(arg1.isalpha())

