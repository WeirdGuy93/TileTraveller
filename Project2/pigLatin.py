word = ""

while word != "." :
    word = input("Enter a word: ")
    vowels = "aeiou"

    if word == "." :
        break

    for i in range(0, len(word)) :
        if word[i] in vowels :
            if i == 0 :  #if the first letter is a vowel
                word = word + "yay"
                break
            else :
                word = word[i:] + word[:i] + "ay"
                break
    else :
        word = word  + "ay"

    print(word)


