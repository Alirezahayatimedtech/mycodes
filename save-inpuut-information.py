import re

text = input()
words = re.findall(r'[A-Z][a-z]*', text)
index = 1
found = False

for i, word in enumerate(words):
    if i == 0:
        continue
    if word[-1] in ['.', ',']:
        word = word[:-1]
    if word.isnumeric():
        continue
    if word[0].isupper():
        found = True
        print(f"{index}:{word}")
        index += 1

if not found:
    print("None")