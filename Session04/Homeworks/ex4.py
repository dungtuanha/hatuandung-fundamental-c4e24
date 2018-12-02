from random import randint

words = ["hexagon", "food", "drinks", "coffee", "girlfrend", "smart", "guitar", "piano"]

while True:
    
    j = randint(0,len(words)-1)
    word = words[j]

    characters = list(word)

    new_word = []

    while len(characters) != 0:
        n = randint(0,len(characters)-1)
        new_word.append(characters[n])
        characters.pop(n)

    print("guess the word: ", *new_word)

    your_word = str(input("your answer: "))

    word = str(word)

    while your_word != (word):
        your_word = str(input("wrong answer, try again: "))
        if your_word == (word):
            break
    words.remove(word)
    print("Bingo")
    
    try_again = str(input("Do you want to try again with an other word(Y/N)? "))
    if try_again == "Y":
        if len(words) == 0:
            print("sorry we are out of word, thanks for playing^^")
            break
        True
    elif try_again == "N":
        break
    