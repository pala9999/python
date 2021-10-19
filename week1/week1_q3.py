demo_string = "This string is used for python demo purpose do not modify this string and use it as it is"
print(demo_string.upper())
print("Count occurrences of \"it\" :", demo_string.count('it'))
print("Count occurrences of \"string\" :", demo_string.count('string'))
print("Count the number of words :", len(demo_string.split()))
print("String in reverse: \n", "\"",demo_string[::-1],"\"")
print("Slice the string from index 10 to index 25:\n", demo_string[10:25])