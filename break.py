word = input("Enter a word: ")
a = input("Enter a the character needed to be found in word: ")

for character in word:
    if character == a:
        print("found")
        break
else:
    print("not found")