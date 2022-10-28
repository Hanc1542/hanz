with open('draft.txt') as fi:
    data = fi.readlines()
idx = 0
size = len(data)
new_word = ''
while idx < size:
    list = data[idx].split()
    i = 0
    length_list = len(list)
    while i < length_list:
        if list[i] == 'Kteam':
            list[i-1] = 'How'
        i = i+1
    new_word += ' '.join(list) + '\n'
    idx += 1
with open("kteam.txt",'w') as f:
    f.write(new_word)