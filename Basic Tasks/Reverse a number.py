num = 12345

# Method 1
rev1 = int(str(num)[::-1])


# Method 2
rev2 = 0
while(num > 0):
    rev2 = rev2*10 + (num % 10)
    num = num//10
print(rev1)
print(rev2)
