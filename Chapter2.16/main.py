

def my_function(str1, str2):
    print(str1)
    print(str2)
    print('tab')
    print('spaces')


my_function('hello', 1)


def my_function(name, age):
    print('my name is ' + name + ' and my age is ' + age)


my_function('hello', str(1))


def my_function(name, age):
    print('my name is', name, 'and my age is', age)


my_function('hello', 2)


def my_function(name="Someone", age="Unknown"):
    print('my name is', name, 'and my age is', age)


my_function('hello')


def my_function(name="Someone", age="Unknown"):
    print('my name is', name, 'and my age is', age)


my_function(age=36, name="Kelvin")


def print_people(*people):
    for person in people:
        print('This person is', person)


print_people('Kelvin', 'Zoe', 'Quinn', 1)


def do_math(num1, num2):
    return num1 + num2


result = do_math(1, 2)
print('result is', result)


check = 'hello'

if check == False:
    print('It is false')
elif check == 'hello':
    print('it is hello')
else:
    print('It is true')


numbers = [1, 2, 3, 4, 5]

for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1

