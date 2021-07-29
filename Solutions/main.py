def calculator(num1, num2):
    typeOfOperation = input("What would you like to do: ADD, SUBTRACT, MULTIPLY, DIVISION ")

    if (typeOfOperation == "ADD"):
        print(num1 + num2)
    elif (typeOfOperation == "SUBTRACT"):
        print(num1 - num2)
    elif (typeOfOperation == "MULTIPLY"):
        print(num1 * num2)
    elif (typeOfOperation == "DIVIDE"):
        print(num1 / num2)
    else:
        print("N/A")

friends = ["Jim", "Kevin", "Dwight", "Pam", "Kelly", "Oscar", "Michael"]

friends.insert(0,"Angela")


def insert(numbers):
    SortedList = []

    if(numbers[0] > numbers[1]):
        SortedList.insert(0, numbers[1])
        SortedList.insert(1, numbers[0])
        if(numbers[2] > SortedList[1]):
            SortedList.insert(2,numbers[2])
            print(SortedList)
        elif(numbers[2] > SortedList[0]):
            SortedList.insert(1,numbers[2])
            print(SortedList)
        else:
            SortedList.insert(0,numbers[2])
            print(SortedList)
    else:
        SortedList.append(numbers[0])
        SortedList.append(numbers[1])
        print(SortedList)




def printNumbers(numbers):
    start = len(numbers) - 1
    stop = 0
    for i in range(start, stop, -1):
        print(numbers[i])



def test(nums):
    start = 0
    stop = len(nums)
    # outer loop
    for i in range(start, stop):
        print("i-{}".format(i))
        upper = i
        # inner loop
        for j in range(upper, 0, -1):
            output = "i-{}, j-{}".format(i,j)
           
            print(output)

nums = [8, 2, 5, 7, 3]


def InsertionSort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j+1] = numbers[j]
            j -=1
        numbers[j+1] = key

    print(numbers)


InsertionSort([100,99,98,97,96,95])


















