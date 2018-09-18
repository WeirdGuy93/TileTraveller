import string

strengur = input("Enter a sentence: ")

punctuation = string.punctuation

lower = 0
upper = 0
digit = 0
punctuations = 0

for i in range(0, len(strengur)) :
    if strengur[i].isupper() :
        upper += 1
    elif strengur[i].islower() :
        lower += 1
    elif strengur[i].isdigit() :
        digit += 1
    elif strengur[i] in punctuation :
        punctuations += 1

print("{:>15} {:5}".format("Upper case", upper))
print("{:>15} {:5}".format("Lower case", lower))
print("{:>15} {:5}".format("Digits", digit))
print("{:>15} {:5}".format("Punctuation", punctuations))