index = -1

def search (list, searchKey):
    count = 0
    while count < len(list):
        if searchKey == list[count]:
            globals() ['index'] = count
            return True
        count += 1
    return False


list = [10, 2, 1, -2, 11 , 90]
searchKey = 11

if search(list, searchKey):
    print("Item found in position", index)
else:
    print("Item not found")