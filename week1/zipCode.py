# zipCode = "12345"
# print(zipCode)

zipCode=input("Enter zipCode:\n")
#print(zipCode.isnumeric())        
if len(zipCode) != 5: 
    print("Invalid Zip: " + zipCode + "\t...expecting 5 digit zip")
    exit()
elif (zipCode.isnumeric()) == False:
    print("Invalid zip: " + zipCode + "\t...expecting numbers only") 
    exit()
else:
    print(zipCode)
    print("The Zip Code is:", zipCode)
    print("zip code: %s" %(zipCode))
    print(f"The zip code is {zipCode}")
# Adding commet to test GIT from Visual Studio    

import sys