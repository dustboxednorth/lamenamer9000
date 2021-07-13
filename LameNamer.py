#dustboxednorth's Lame Namer 9000
#2021
from datetime import date
from random_word import RandomWords

today = date.today()
r = RandomWords()

# Generate the name, in the format DAY_ADJECTIVE_NOUN
name = today.strftime("%d") + ' ' + r.get_random_word(excludePartOfSpeech = "noun") + ' ' + r.get_random_word(excludePartOfSpeech = "adjective, verb")

# Print it
print(name)
