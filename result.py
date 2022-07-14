import base64
secret = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
text = base64.b64decode(secret).decode('utf-8') # iangnoW:NAM:ENIL:ta:su:nioJ
t_split = text.split(":") # ['iangnoW', 'NAM', 'ENIL', 'ta', 'su', 'nioJ']

# for reverse each word to ['Wongnai', 'MAN', 'LINE', 'at', 'us', 'Join']
lst_rev_each_word = []
for word in t_split:
  lst_rev_each_word.append(word[::-1])

print(' '.join(reversed(lst_rev_each_word))) # Join us at LINE MAN Wongnai