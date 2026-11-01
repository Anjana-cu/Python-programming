numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

# Search
search = int(input("Enter a number to search: "))

if search in numbers:
    print(search, "is present in the list")
else:
    print(search, "is not present in the list")


# Update
old = int(input("Enter the number to update: "))

if old in numbers:
    new = int(input("Enter the new value: "))
    index = numbers.index(old)
    numbers[index] = new
    print("Updated list:", numbers)
else:
    print(old, "is not present in the list")


# Even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)


# Add
element = int(input("Enter an element to add: "))
numbers.append(element)
print("After adding:", numbers)


# Remove
element = int(input("Enter an element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("After removing:", numbers)
else:
    print(element, "is not present in the list")


# Sort
numbers.sort()
print("Sorted list:", numbers)


# Reverse
numbers.reverse()
print("Reversed list:", numbers)