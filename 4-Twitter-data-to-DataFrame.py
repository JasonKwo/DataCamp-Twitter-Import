# Now we have the Twitter data in a list of dictionaries, tweets_data, where each dictionary corresponds to a single tweet.
# Next we're going to extract the text and language of each tweets.  The text in a tweet, t1, is stored as the value
# t1['text'] and the language is stored in t1['lang'].

# Our task is to build a DataFrame in which each row is a tweet and the columns are 'text' and 'lang'



# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang'])

# Print head of DataFrame
print(df.head())
