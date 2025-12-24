s = "Hello123@#"

vowels = consonants = digits = special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)


#palindrome
a= "madam"

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

#frequency of characters
freq={}
for ch in a:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character Frequency:", freq)

#reverse
r = "Python is easy"
result = ""
word = ""

for ch in r:
    if ch != " ":
        word = ch + word      # reverse current word
    else:
        result = result + word + " "
        word = ""

# add last word
result = result + word

print(result)

#5th
b = "Python"

try:
    b[0] = "J"   
except TypeError as e:
    print("Error:", e)

print("String after attempt:", b)