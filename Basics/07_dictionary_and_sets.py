# Dictionary
dict = {
    "name": "Subarna Poudel",
    "class": 13,
    "address": "Mars"
}
print(dict)  # Prints the dictionary

print(dict.keys())  # Get Keys
print(list(dict.values()))  # Get Values and shows in a list

# Getting values from dict
print(dict["name"])
print(dict.get("class"))

# Sets
# Sets are fixed like tuples
# Sets cannot contain same value twice
# Sets can contain tuples but not list because tuples are fixed but lists are not.
se = {1, "Subarna", 3, (1, 2), 1}
se.add(10)  # Adds 10 to the set
print(se)
