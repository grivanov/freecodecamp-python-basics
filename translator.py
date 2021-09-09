word = input("Typa a word to be translated: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
result = ""

for letter in word:
    if letter in vowels:
        letter = "g"
        result += letter
    else:
        result += letter

print(result)
