top_number = 20

for number in range(1,top_number):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizzbuzz!')
    elif number % 3 == 0:
        print('Fizz!')
    elif number % 5 == 0:
        print('Buzz!')
    else:
        print(number)
