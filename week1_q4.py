my_list = ["a", "c", "d", "e", "f", "g", "h", "i"]
print("Initial List: ", my_list)
my_list.append("j")
print("\nAdd \"j\" to the end of list:")
print(my_list)
print("\nInsert \"b\" between \"a\" and \"c\":")
my_list.insert(1,"b") #Specify postion , character to add#
print(my_list)
print("\nRemove \"e\" from list:")
my_list.remove("e") #Specify exact chat to remove#
print(my_list)
print("\nReverse the list:")
my_list.reverse()
print(my_list)
print("\nreplace i with z:")
my_list[0]="z"
print(my_list)
print("\nSorted List:")
my_list.sort()
print(my_list)