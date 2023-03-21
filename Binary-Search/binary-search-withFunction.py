list = [2, 3, 9, 10, 18, 34, 41, 49, 50, 80, 100, 120]
searchKey = 80


def search(list: int, searchKey) -> int :
    lowerB = 0
    upperB = len(list) - 1

    while upperB >= lowerB :

        midIndex = (lowerB + upperB) // 2

        if searchKey == list[midIndex]:
            return midIndex
        if searchKey > list[midIndex]:
            lowerB = midIndex + 1
        if searchKey < list[midIndex]:
            upperB = midIndex - 1

    return None


def validate (midIndex):
    if midIndex is not None:
        print("Item found in", midIndex)
    if midIndex is None:
        print("Item not found")

returnValue = search(list, searchKey)
validate(returnValue)