import random

word = str(input("enter a word: "))

charlst = list(word)
random.shuffle(charlst)
new_word = ''.join(charlst)

print("guess what word is this: ", end ="")
print(new_word)

your_word = str(input("your answer: "))

while your_word != (word):
    your_word = str(input("wrong answer, try again: "))
    if your_word == (word):
        print("Bingo")
        break
