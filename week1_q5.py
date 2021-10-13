x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

print("x=",x)
print("y=",y)
#1) Check if x is subset of y.
#2) Returns a set containing the difference between sets.
#3) Remove all elements from set.
#print("union:", x|y)
#print("union on x", x.union(y))
#print("union on y", y.union(x))
print("x is subset of y:", x.issubset(y))
#print("x contains y:", x.issuperset(y))
#print("intersection:", x & y)
#print("diffrence x-y:", x-y)
#print("diffrence y-x:", y-x)
#print("diffrence x-y:", x.difference(y))
#print("diffrence y-x:", y.difference(x)) 
print("difference between sets x and y: ",x ^ y)
#print( y ^ x)
x.clear()
y.clear()
print("remove all elements from x=",x)
print("remove all elements from y=",y)