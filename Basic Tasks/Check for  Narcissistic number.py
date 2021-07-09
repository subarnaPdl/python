# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.

def count_digits(value):
    if value == 0:
        return 0
    return 1 + count_digits(value // 10)


def narcissistic(value):
    base = count_digits(value)
    a = value; sum = 0
    while(a>0):
        sum += (a % 10) ** base
        a = a // 10
    return sum == value


print(narcissistic(123))
