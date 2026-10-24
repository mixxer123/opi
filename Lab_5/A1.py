def shorten(text):
    while True:
        left = text.rfind('(')
        if left == -1:
            break
        right = text.find(')', left)
        if right == -1:
            break
        text = text.replace(text[left:right + 1], '')
    text = ' '.join(text.split())
    text = text.replace(' .', '.')
    return text


text = input()
print(shorten(text))
