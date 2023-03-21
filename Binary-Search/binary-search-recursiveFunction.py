list = [2, 3, 9, 10, 18, 34, 41, 49, 50, 80, 100, 120]
searchKey = 3

lowerB = 0
upperB = len(list) - 1

def recursiveSearch(list, searchKey):
    if len(list) == 0:
        return False
    else:
        mid = (len(list)) // 2

        if list[mid] == searchKey:
            return True

        else: 
            if list[mid] > searchKey:
                return recursiveSearch(list[: mid], searchKey)
            else:
                return recursiveSearch(list[mid + 1 :], searchKey)
        
result = recursiveSearch(list, searchKey)

if result is not False:
    print("Item found")
else: 
    print("Item not found")