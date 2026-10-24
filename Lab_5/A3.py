text = input()
result = ''
for word in text.split():
    if len(word) >= 3:
        result += word[0].upper()
print(result)
