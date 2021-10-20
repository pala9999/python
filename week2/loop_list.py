
#Loop through the items in the fruits list.fruits = ["apple", "banana", "cherry"]
print("\n**** while loop through the items in the fruits list *****")
listf = ["apple", "banana", "cherry"]
i = 0
while i < len(listf):
    print("Element",i,"=",listf[i])
    i +=1

print("\n**** for loop through the items in the fruits list *****")
listf = ["apple", "banana", "cherry"]
num = len(listf)
for num in range(0,num):    ### Range max should be 1 more than neede , so num instead on num-1
    print("Element",num,":",listf[num])

#Print First 5 natural numbers using while loop
print("\n***  Print First 5 natural numbers using while loop ***")
i = 1
while i <= 5:
    print("Element",i,"=", i)
    i +=1    

#Print First 5 natural numbers using for loop
print("\n*****  Print First 5 natural numbers using for loop *****")
for num in range(1,6):
    print(num)


#Using while loop calculate the sum of all numbers from 1 to 10
print("\n*****  Using while loop calculate the sum of all numbers from 1 to 10 ****")
i=1
sum=0
while i <= 10:
    sum += i
    i +=1 ### increment i by 1 to end the while loop
print(sum) 

print("\n*****  Using for loop calculate the sum of all numbers from 1 to 10 ****")
sum=0
for i in range(1,11):
    sum = sum + i
print(sum)


#Write while loop program to print a multiplication table of 3 from 1 to 10 -> (3,6,9.....,30)
print("\n***  while loop to print a multiplication table of 3 ****")

i=1
while i < 11:
    print("3 *",i,"=",i*3)
#    i == i + 1
    i +=1

# #Write for loop program to print a multiplication table of 3 from 1 to 10 -> (3,6,9.....,30)
print("\n***   for loop to print a multiplication table of 3 ****")
for i in range(1,11):
    print("3 * ",i,"=",3*i)


#Write a program to display only those numbers which are divisible by five from a list
print("\n****   while loop to display only those numbers which are divisible by five ***")
list1 = [1,3,5,8,20]
i=0
while i < len(list1):
    if list1[i] % 5 == 0:
        print(list1[i])
    i +=1

print("\n**** for loop to display only those numbers which are divisible by five ***")
list1 = [1,3,5,8,20]
for i in range(0,len(list1)):
    if list1[i] % 5 == 0:
        print(list1[i])
        
#Given a list, replace the smallest value with the largest one.
#Input: 
#ListA = [4,5,6,2,9]
#Output should be
#ListA = [4,5,6,9,9]
#2 is the smallest number and it should be replace by 9.
print("\n****  without loop replace the smallest value with the largest one *****")
listA = [4,5,6,2,9]
print("Original List =",listA)
list_len=len(listA)-1
list_sort = listA[:]
list_sort.sort()
sml_num=list_sort[0]
lrg_num=list_sort[list_len]
print("Smallest num =",sml_num)
print("largest num =",lrg_num)
sml_num_indx = int(listA.index(sml_num))
print("Index of smallest num",sml_num,"=",sml_num_indx)
listA[sml_num_indx]=lrg_num
print("Final List =",listA)

# *********** with for loop  ***********************
print("\n****  for loop replace the smallest value with the largest one *****")
listA = [4,5,6,2,9]
print("Before:",listA)
max_num=max(listA)
list_len=len(listA)
for i in range (0,list_len) :
    if listA[i] < max_num :
            small_num=listA[i]
listA[(listA.index(small_num))]=max_num
print("After:",listA)

# *************** with while loop ****************

print("\n****  while loop replace the smallest value with the largest one *****")
listA = [4,5,6,2,9]
print("Before:",listA)
i=0
max_num=max(listA)
while i < len(listA):
    if listA[i] < max_num :
        small_num=listA[i]
    i = i + 1
listA[(listA.index(small_num))]=max_num
print("After:",listA)    
