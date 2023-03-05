def find_perfect_numbers():
    i = 2
    while True:
        if is_perfect_number(i):
            yield i
        i += 1


def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number


for number in find_perfect_numbers():
    print(number)