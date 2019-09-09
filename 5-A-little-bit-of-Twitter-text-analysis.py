# We now have a DataFrame of tweets set up.  We can analyse how many tweets contain the words 'clinton', 'trump', 'sanders'
# and 'cruz'.

# In pre-exercise code, we have defined the following function 'word_in_text()', which will tell you whether the first arguement
# (a word), occurs within the second argument (a tweet).

import re

def word_in_text(word, text):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False
    
    
# We can iterate over the rows of the DataFrame and calculate how many tweets contain each of our keywords.


# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df (previously defined DataFrame), counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])
