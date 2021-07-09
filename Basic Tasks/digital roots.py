def digital_root(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n = n // 10

    if len(str(sum)) != 1:
        return digital_root(sum)
    else:
        return sum


print(digital_root(942))
