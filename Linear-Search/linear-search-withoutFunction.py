list = [10, 2, 1, -2, 11 , 90]
flag = 0
count = 0
searchKey = 11

while count < len(list):
    if searchKey == list[count] :
        flag = 1
        print("Item found in position ", count)
    count = count + 1

if flag == 0:
    print("Item not found")




