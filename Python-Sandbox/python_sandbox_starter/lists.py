# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]

# Use constructor
# numbers2 = list((1, 2, 3, 4, 5))

fruits = ['apple', 'oranges', 'grapes', 'pears']

# Get one value
print(fruits[0])

# Get length
print(len(fruits))

# Append to list
fruits.append('mangos')
print(fruits)

# Remove from list
fruits.remove('grapes')

# Insert into position
fruits.insert(2, 'strawberries')

# Remove by position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
