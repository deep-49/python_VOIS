#sets
set1= {1, 2, 3, 4, 5}
set2= {4, 5, 6, 7, 8}

union_set= set1|set2
print("Union of set1 and set2:", union_set)
intersection_set= set1 & set2
print("Intersection of set1 and set2:", intersection_set)
difference_set= set1 - set2
print("Difference of set1 and set2:", difference_set)
symmetric_difference_set= set1 ^ set2
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)

is_subset = True

for element in set1:
    if element not in set2:
        is_subset = False
        break

if is_subset:
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")

i=int(input("Enter a number: "))
for element in set2:
    if element >i:
        print(element)


numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_set = set(numbers)
unique_list = list(unique_set)
print("unique set:", unique_set)
print("List with Unique Elements:", unique_list)
