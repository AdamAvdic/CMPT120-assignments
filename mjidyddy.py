
def numvowels(mystring):
    vowels = ["a","e","i","o","u"]
    num_vowels = 0
    for i in mystring.lower():
        if i in vowels:
            num_vowels += 1

    print(num_vowels)


numvowels("hello")
numvowels("eEe")
numvowels("tsktsk")
