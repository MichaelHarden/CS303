f = open('inputs/input_10000.txt', 'r')
content = f.read()
content = content.split('\n')
content = [word + ' ' for word in content]
f.close()

f = open('inputs/input_10000.txt', 'w')

for word in content:
    f.write(word)

f.close()