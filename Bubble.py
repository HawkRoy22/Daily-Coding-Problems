numbers = [10,9,8,7]

index = 0
swapCtr = 0
temp = 0
i = 0

while(True):
    print(numbers)
    print("swapCtr {x}".format(x=swapCtr))
    print("i {x}".format(x=i))
    if numbers[i] >  numbers[i+1]:
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp
        swapCtr+=1

    if(swapCtr > 0 and i == (len(numbers) - 2)):
        i = 0
        swapCtr = 0
        continue
    elif (swapCtr == 0 and i == (len(numbers) - 2)):
        break

    i += 1

for i in range(0,5):
    print(i)

