#dustboxednorth's Lame Namer 9000
#2021
from datetime import date
from random_word import RandomWords

today = date.today()
r = RandomWords()
spc = ' '

# Generate the name, in the format DAY_ADJECTIVE_NOUN
name = today.strftime("%d") + spc + r.get_random_word(excludePartOfSpeech = "noun") + spc + r.get_random_word(excludePartOfSpeech = "adjective, verb")

# Print it
print(name)
