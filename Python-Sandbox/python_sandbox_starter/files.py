# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('Python')
myFile.write(' and Javascript\n')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write('I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
myFile.close()
print(text)
