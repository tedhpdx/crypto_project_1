from sub_key_generator import generate

eight_byte_block = 'security'
key = 'abcdef0123456789'

block_list = []

for letter in eight_byte_block:
    stripped = hex(ord(letter))[2:]
    block_list.append(stripped)


word_list = []
i = 0
j = 1
while j < 8:
    word_list.append(block_list[i] + block_list[j])
    i += 2
    j += 2
print(word_list)

key_list = []
i = 0
j = 4
while j <= 16:
    temp_string = ''
    for index in range(i,j):
        temp_string += key[index]
    i += 4
    j += 4
    key_list.append(temp_string)
print (key_list)

r_values = []
for i in range(len(word_list)):
    r_values.append((int(word_list[i], 16)) ^ (int(key_list[i], 16)))

print (r_values)
print (generate(key))