def reverseWords(input):
    inputWords = input.split(" ")
    output = " ".join(list(reversed(inputWords)))
    return output


print(reverseWords('Hello World Learning Python'))
