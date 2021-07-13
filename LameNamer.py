#dustboxednorth's Lame Namer 9000
#2021
from datetime import date
from random_word import RandomWords

today = date.today()
r = RandomWords()

# Generate the name
name = today.strftime("%d") + '_' + r.get_random_word(excludePartOfSpeech = "noun") + '_' + r.get_random_word(excludePartOfSpeech = "adjective, verb")

# Print it
print(name)
