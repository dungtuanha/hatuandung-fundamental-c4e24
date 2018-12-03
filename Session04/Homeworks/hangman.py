from random import randint

print("Welcome to hangman")

#----------------------------------------------------------------------------------------------------
n = 0
erors = 0
blank_space = []

while True:
    #Draw the hangman if there is a mistake
      
    if erors > 0:
        print("---|")
    else:
        print("---")
    if erors > 1:
        print("   |")
    else:
        print()
    if erors > 2:
        print("   o")
    else:
        print()
    if erors > 3:
        print("  -", end = "")
    else:
        print()
    if erors > 4:
        print("|", end ="")
    else:
        print()
    if erors > 5:
        print("-")
    else:
        print()
    if erors > 6:
        print("  /", end = "")
    else: 
        print()
    if erors == 8:
        print(" |")
    else:
        print()
    print()
    print()
    print()
    
    #----------------------------------------------------------------------------------------------------
    #Checking if the erors over 7 times or not. 
    if erors == 8:
        print("You lose :( ")
        break
    
    #-----------------------------------------------------------------------------------------------------
    #Choose word from my list for user to guess
    if n == 0:
        words = ["hexagon", "food", "drinks", "coffee", "girlfrend", "smart", "guitar", "piano"]
        j = randint(0,len(words)-1)
        word = words[j]
        n = n + 1

    #------------------------------------------------------------------------------------------------------
    #Blank space
    if n == 1:
        for i in range(len(word)):
            blank_space.append("_")
            n = n +1             #giúp cho tránh việc chương trình tiếp tục in "_" trong lần lặp tiếp theo

    print(*blank_space)
    print()
    
    #------------------------------------------------------------------------------------------------------
    #user's guess input
    guess = str(input("Your guess? "))
    
    #-----------------------------------------------------------------------------------------------------
    #Checking user's guess and print the result
    k = 0
    characters = list(word)
    for i in range(len(characters)):
        if guess == characters[i]:
            blank_space[i] = guess
        else:
            k = k + 1               

    if k == len(characters):                   #check từ đầu đến cuối mà sai hết thì mới tính 1 lỗi.
        erors = erors + 1                      
    
    if blank_space == characters:
        print("You win^^")
        break 

    
    #------------------------------------------------------------------------------------------------------