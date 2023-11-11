def fizzBuzz(input):
    if input%3 == 0 and input%5 == 0:
        return 'fizzBuzz'
    if input%3 == 0:
        return 'fizz'
    if input%5 == 0:
        return 'Buzz'
    return input


print(fizzBuzz(1))