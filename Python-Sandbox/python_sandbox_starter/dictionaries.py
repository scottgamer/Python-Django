# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Richard', last_name='Munoz')

print(person, type(person))

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-55555'
print(person)

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Length
print(len(person))

# List of dicts
people = [
    {'name': 'Richard', 'age': 26},
    {'name': 'Ariel', 'age': 6}
]

print(person)
print(people[1])
