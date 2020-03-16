# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Richard', 'Ariel', 'Maria', 'Wando']

# Simple for loop
for person in people:
    print(f'CUrrent person: {person}')

# Break - stops iteration
for person in people:
    if person == 'Ariel':
        break
    print(f'CUrrent person: {person}')


# Continue - skips value and continues to next
for person in people:
    if person == 'Ariel':
        continue
    print(f'CUrrent person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1
