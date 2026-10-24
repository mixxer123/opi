import re

text = input()
sentences = re.split(r'(?<=[.?!])\s+', text.strip())
sentences = [s for s in sentences if s]

for s in sentences:
    print(s)
print('Предложений в тексте:', len(sentences))
