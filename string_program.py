text = input("Enter a string: ")

old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", text.replace(old, new))

print("Reversed string:", text[::-1])

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

print("Character frequency:")

for char in set(text):
    print(char, ":", text.count(char))

words = text.split()
print("Number of words:", len(words))