list = [-3, 3, 5, 10, 11, 20, 22, 51, 76, 101] #Sorted List
searchKey = 101
flag = 0

lowerBoundary = 0
upperBoundary = len(list) - 1


while upperBoundary >= lowerBoundary & flag == 0:
    midInedx = ( lowerBoundary + upperBoundary ) // 2
    if list[midInedx] == searchKey:
        print("Item found in index", midInedx)
        globals() ['flag'] == 1
        break

    elif searchKey > list[midInedx]:
        lowerBoundary = midInedx + 1

    elif searchKey < list[midInedx]:
        upperBoundary = midInedx - 1

if flag == 1:
    print("Item not found")
