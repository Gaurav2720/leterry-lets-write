word = "donkey"

# Read the file with UTF-8 encoding
with open("donk.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the word
contentnew = content.replace(word, "######")

# Write back to file with UTF-8 encoding
with open("donk.txt", "w", encoding="utf-8") as f:
    f.write(contentnew)
