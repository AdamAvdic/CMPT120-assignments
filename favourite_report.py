file = open("favourites-survey_2021Fallm.csv")
header = file.readline()

favorites = file.readline().strip().split(",")

for line in file:
  their_favourites = line.strip().split(",")
  their_name = their_favourites[1]
  vowel_counter = 0 

def countVowels(name):
    if len(name) == 0:
        return 0
    else:
       if name[0] in ["a","e","i","o","u"]:
         return 1 + vowel_counter([1:])
         else:
          return vowel_counter([1:])


print(vowel_counter)
