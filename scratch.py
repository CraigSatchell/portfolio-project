# Python scratch code file

text = 'This method returns a string, which is the concatenation of the strings in the sequence seq. The separator between elements is the string providing this method.'

print(text + '\n')

words = text.split()
cnt = len(words)
print('word count: ' + str(cnt))
i = 0
ntext = ''
print(cnt)
print(words[i])
if cnt >= 50:
    while i < 50:
        ntext = ntext + words[i] + ' '
        i = i + 1
    ntext = ntext + '...'
else:
    ntext = text

print('text:', ntext)
