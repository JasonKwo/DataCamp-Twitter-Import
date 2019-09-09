# Now that we have the number of tweets that each candidate was mentioned in, we can plot a bar chart of this data.
# We'll use the statistical data visuallisation library SEABORN.


# Import packages
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton,trump,sanders,cruz])
ax.set(ylabel="count")
plt.show()
