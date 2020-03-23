def alphabetPosition(text):
    positions = ''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')

    for i in text:
        if i.isalpha():
            positions += str(alphabet.index(i.lower()) + 1) + ' '
            
    return positions[0:len(positions)-1]


print(alphabetPosition("The sunset sets at twelve o' clock."))
