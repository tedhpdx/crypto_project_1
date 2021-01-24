from bitstring import BitArray


#https://www.geeksforgeeks.org/reverse-bits-positive-integer-number-python/
def reverseBits(num,bitSize):
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bitSize - len(reverse))*'0'
    return (int(reverse,2))


def parse_key(shifted_k):
    parsed_key = []
    i = 0
    j = 1
    while j < 16:
        parsed_key.append(shifted_k[i] + shifted_k[j])
        i += 1
        j += 1
    parsed_key.reverse()
    return parsed_key

num = int('0xabcdef0123456789',16)
print
print(num)
num1 = num >> 63
print (num1)
if num1 == 0:
    num = reverseBits(num, 64)
    num = num << 1
    num = reverseBits(num, 64)
    print (num)
if num1 == 1:
    num = reverseBits(num, 64)
    num = num >> 1
    num = reverseBits(num, 64)
    num += 1
    shifted_k = (hex(num))[2:]
    parsed_key = parse_key(shifted_k)
    x = 18
    print(parsed_key[x % 8])

    print (shifted_k)






