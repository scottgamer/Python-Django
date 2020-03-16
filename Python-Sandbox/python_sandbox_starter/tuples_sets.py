# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('apples', 'oranges', 'grapes')
# fruits = tuple(('apples', 'oranges', 'grapes'))

# Single value requires trailing comma
fruits2 = ('apples',)

print(fruits2, type(fruits2))

# Can't change value
# fruits[0] = 'Pears' # tupes do not support item assignment

# Delete tuple
del fruits2

# Get length
print(len(fruits))

######################################

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruits_set = {'apples', 'oranges', 'mango'}

# Check if in set
print('apples' in fruits_set)

# Add to set
fruits_set.add('grape')

# Remove from set
fruits_set.remove('grape')

# Clear set
fruits_set.clear()

print(fruits_set)
