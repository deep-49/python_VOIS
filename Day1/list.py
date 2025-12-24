import copy
lst = [1, 2, 3, 2, 4, 1, 5]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("List without duplicates:", unique)

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [n for n in numbers if n % 2 == 0]

print("Even numbers:", even_numbers)
#3
num=[5, 12, 7, 20, 3, 15, 3, 6]

num.sort()
print("second largest number:",num[-2])

#4
nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
for lst in nested:
    total = 0
    for num in lst:
        total += num
    print("Sum:", total)

#5
original = [1, 2, [3, 4]]

shallow = copy.copy(original)


deep = copy.deepcopy(original)

original[2][0] = 99

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)