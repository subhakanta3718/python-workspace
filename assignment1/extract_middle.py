# Get user input
text = input("Enter a string: ")

# Find the length of the string
length = len(text)

# Determine and print the middle character(s)
if length % 2 == 0:
    # Even length: print two middle characters
    mid1 = length // 2 - 1
    mid2 = length // 2
    print("Middle characters:", text[mid1:mid2 + 1])
else:
    # Odd length: print the single middle character
    mid = length // 2
    print("Middle character:", text[mid])
