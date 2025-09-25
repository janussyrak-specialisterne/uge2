from collections import defaultdict
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Read names using open to ensure correct file closing
with open(os.path.join("data", "names.txt"), "r") as f:
    data = f.read()
    names = data.split(",")

# Sort names alphabetically
names = sorted(names)

# Sort names by length
names = sorted(names, key=len)

# Create dictionary to count occurrences of letters
letters = defaultdict(int)
for name in names:
    for letter in name:
        letters[letter.lower()] += 1

# Plot the frequencies of each letter
sns.set_theme()
sns.relplot(data=letters)
plt.show()

# Print the result
for key in sorted(letters.keys()):
    print(key, letters[key])

# Count and remove duplicates
unique_names = set()
for name in names:
    unique_names.add(name)

print("Names before: ", len(names))
print("Names after: ", len(unique_names))