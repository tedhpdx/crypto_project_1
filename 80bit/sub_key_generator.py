

sub_key_collection = []

#https://www.geeksforgeeks.org/reverse-bits-positive-integer-number-python/
def reverseBits(int_key,bitSize):
    binary = bin(int_key)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'
    return (int(reverse,2))


def parse_key(shifted_k):
    parsed_key = []
    i = 0
    j = 1
    while len(shifted_k) < 20:
        shifted_k = '0' + shifted_k
    while j < 20:
        parsed_key.append(shifted_k[i] + shifted_k[j])
        i += 2
        j += 2
    parsed_key.reverse()
    return parsed_key

def key_schedule(x, key, sub_key_list):
    parsed_key = []
    shifted_key = []
    int_key = int(key,16)
    high_order_bit = int_key >> 79
    if high_order_bit == 0:
        int_key = reverseBits(int_key, 80)
        int_key = int_key >> 1
        int_key = reverseBits(int_key, 80)
        shifted_key = (hex(int_key))[2:]
        parsed_key = parse_key(shifted_key)
    if high_order_bit == 1:
        int_key = reverseBits(int_key, 80)
        int_key = int_key >> 1
        int_key = reverseBits(int_key, 80)
        int_key += 1
        shifted_key = (hex(int_key))[2:]
        parsed_key = parse_key(shifted_key)
    index = x % 8
    sub_key_list.append(parsed_key[x % 10])
    return shifted_key , sub_key_list

def k(round, sub_key_list, key):
    key_prime, sub_key_list = key_schedule(4*round, key, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+1, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+2, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+3, key_prime, sub_key_list)

    key_prime, sub_key_list = key_schedule(4*round, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+1, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+2, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+3, key_prime, sub_key_list)

    key_prime, sub_key_list = key_schedule(4*round, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+1, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+2, key_prime, sub_key_list)
    key_prime, sub_key_list = key_schedule(4*round+3, key_prime, sub_key_list)

    sub_key_collection.append(sub_key_list)

    return key_prime, sub_key_list

def generate(key):
    key_prime = key
    for i in range(20):
        sub_key_list = []
        key_prime, sub_key_list = k(i, sub_key_list, key_prime)
    return sub_key_collection






