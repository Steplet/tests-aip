words = ('Alaska', 'auto', 'arc', 'agenda', 'arugula', 'caveman')
words_2 = set()
words_3 = []
buf = []
w = []
slo = ''
book = 'aoiuey'
wer = ''
for i in range(len(words)):
    buf = str(words[i])
    buf = buf.lower()
    if buf.count('a') > 1:
        w.append(buf.count("a") ** 2)
words_1 = tuple(w)
print(words_1)

for step in range(len(words)):
    if len(words[step]) > 3:
       words_2.add(words[step])
print(words_2)

for a in range(len(words)):
    if words[a][-1] == 'a':
        wer = str(words[a])
        wer = wer.lower()
        for l in wer:
            if l in book:
                wer = wer.replace(l, '')
        words_3.append(wer)
print(words_3)
