w = int(2)
x = int(5)
y = int(7)

a = w + y
b = y - w
c = y % x
d = y // w
e = y ** w
f = w * x
g = y / x

print("a = w + y")
print("a =", w , "+" , y , "=" , a)

print("b = y - w") 
print("b =", y , "-" , w , "=" , b)

print("c = y % x")
print("c =", y , "%" , x , "=" , c)

print("d = y // w")
print("d =", y , "//" , w , "=" , d)

print("e = y ** w")
print("e =", y , "**" , w , "=" , e)

print("f = w * x")
print("f =", w , "*" , x , "=" , f)

print("g = y / x")
print("g =", y , "/" , x , "=" , g) 

print(a, ',', b ,',', c ,',', d,',', e,',', f,',', g)