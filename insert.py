# def InsertionPath(numbers):
# for i in range(1, len(numbers)):
#    key = numbers[i]
#    j = i - 1
#   while j >= 0 and key < numbers[j]:
#       numbers[j+1] = numbers[j]
#       j = j - 1
#   numbers[j+1] = key

# numbers = [100,98,96,94,92,90,88]
# InsertionPath(numbers)
# for i in range(len(numbers)):
#    print(numbers[i])


class Snake:
    name = "python"  # set an attribute 'name' of the class
    age = 20

    # Instance attributes & the init method
    def __init__(self, name):
        self.name = name

    # Below is a Method
    def change_name(self, new_name):  # note that the first argument is self
        self.name = new_name




#snake = Snake('python')
#print(snake)
#print(snake.name)
#print(snake.age)
#snake.change_name("anaconda")
#print(snake.name)


class Tweet:
    def __init__(self):
        self.x =

a = Tweet()

a.message = '140 characters.'

print(a.message)

b= Tweet()
b.message = "HOEOO"

print(b.message)


























