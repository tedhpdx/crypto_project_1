from sub_key_generator import generate
from f_table import get_f_table_value

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

r_values = []
for i in range(len(word_list)):
    r_values.append((int(word_list[i], 16)) ^ (int(key_list[i], 16)))


def g_permutation(r, round_number, sub_key_list):
    hex_string = (hex(r))[2:]
    while len(hex_string) is not 4:
        hex_string = '0' + hex_string
    g1 = int(hex_string[:2], 16)
    g2 = int(hex_string[2:], 16)

    sub_key = int(sub_key_list[0], 16)
    g3 = get_f_table_value(g2 ^ sub_key) ^ g1

    sub_key = int(sub_key_list[1], 16)
    g4 = get_f_table_value(g3 ^ sub_key) ^ g2

    sub_key = int(sub_key_list[2], 16)
    g5 = get_f_table_value(g4 ^ sub_key) ^ g3

    sub_key = int(sub_key_list[3], 16)
    g6 = get_f_table_value(g5 ^ sub_key) ^ g4

    if g5 < 16:
        g5 = '0' + (hex(g5)[2:])
    else:
        g5 = hex(g5)[2:]
    if g6 < 16:
        g6 = '0' + (hex(g6)[2:])
    else:
        g6 = hex(g6)[2:]
    final_hex = g5 + g6
    return final_hex


def f_function(r_values, round_number, sub_key_list):
    t0 = g_permutation(r_values[0], round_number, sub_key_list[0:4])
    t1 = (g_permutation(r_values[1], round_number, sub_key_list[4:8]))
    t0 = int(t0,16)
    t1 = int(t1,16)
    key0 = int((sub_key_list[8] + sub_key_list[9]),16)
    key1 = int((sub_key_list[10] + sub_key_list[11]),16)
    f0 = (t0 + 2*t1 + key0) % (2**16)
    f1 = (t1 + 2*t0 + key1) % (2**16)
    return f0, f1

sub_key_collection = generate(key)
round_number = 0

def process_rounds(r_values, round_number, sub_key_collection):
    f0, f1 = f_function(r_values, round_number, sub_key_collection[round_number])
    r0_temp = r_values[0]
    r1_temp = r_values[1]
    r_values[0] = r_values[2] ^ f0
    r_values[1] = r_values[3] ^ f1
    r_values[2] = r0_temp
    r_values[3] = r1_temp
    #print(round_number)
    #print("0x" + hex(r_values[0])[2:] + hex(r_values[1])[2:] + hex(r_values[2])[2:] + hex(r_values[3])[2:])
    round_number += 1
    if round_number < 16:
        process_rounds(r_values, round_number, sub_key_collection)



def final_steps(r_values, key_list):
    y0 = r_values[2]
    y1 = r_values[3]
    y2 = r_values[0]
    y3 = r_values[1]
    c0 = y0 ^ int(key_list[0],16)
    c1 = y1 ^ int(key_list[1],16)
    c2 = y2 ^ int(key_list[2],16)
    c3 = y3 ^ int(key_list[3],16)
    print ("The ciphertext is: " + hex(c0) + hex(c1)[2:] + hex(c2)[2:] + hex(c3)[2:])


process_rounds(r_values, round_number, sub_key_collection)
final_steps(r_values, key_list)