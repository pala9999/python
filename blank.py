import datetime
name=input("Enter your name:\n")
age=int(input("Enter your age in years:\n"))
age_to_hun=100-age
#print(type(age_to_hun))
curr_yr=int(datetime.datetime.now().year)
#print(today)
#d=int(today.strftime("%Y"))
#print(type(d))
#year_at_hun=age_to_hun+d
print("Hello",name,"you will trun 100 years old in year", curr_yr+age_to_hun)