#List - Changable
lt = [4, 3, 6, 1, 7]
print(lt)

# Sorting the list
lt.sort()
print(lt)

lt[2] = 10  # Changing the item at index 2
print(lt[2])  # Getting the element at index 2

# Appending to the list
lt.append("Append")
print(lt)

#Removing item at index 2
lt.pop(2)
print(lt)

#Removing item "Append"
lt.remove("Append")
print(lt)

#Tupple - Fixed
tup=("Tupple",1,2,3)
print(tup)