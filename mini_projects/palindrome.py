word = input("enter a word: ").lower()
reversed_word = "".join(reversed(word))
# for i in range(len(word) - 1, -1, -1):
    # reversed_word += word[i]
if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print("not a palindrome")

