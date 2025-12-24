t = (10, 5, 25, 3, 18)

max_val = t[0]
min_val = t[0]

for i in t:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)

#2
data = [("a", 1), ("b", 2), ("c", 3)]
d = {}

for item in data:
    key = item[0]
    value = item[1]
    d[key] = value

print(d)
#3
a = (1, 2, 3, 2, 4, 2, 5)
x=2
count = 0
for i in a:
    if i == x:
        count += 1

print(f"Count of {x} in tuple: {count}")

#4
c = (1, 2, [10, 20, 30])

c[2][1] = 99  

print(c)

#5
p = (5, 10, 15, 20, 25)
q =(30, 35, 40)
p, q = q, p
print("p:", p)
print("q:", q)
