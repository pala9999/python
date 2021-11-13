### Binary Search

listA = [3,8,5,7,4]
def binarySearch(ListofElements, searchElement):
    ListofElements = sorted(ListofElements)
    print(ListofElements)
    low = 0
    mid = 0
    upper = len(ListofElements) - 1

    while(low <= upper):
        mid = ( low +upper)// 2
        if ListofElements[mid] == searchElement:
            return ("Element found",ListofElements[mid], "Index of", mid)
        else:
            if ListofElements[mid] < searchElement:
                low = mid + 1
            else:
                upper = mid - 1
    return("Element not found")

print(binarySearch(listA,4))
    

