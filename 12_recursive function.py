# A Recursive function
def func(n):
    if n == 0:
        return 1
    return n*func(n-1)


n = int(input("Enter a number: "))
print(func(n))
