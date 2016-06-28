import random
def encoder(s):
    b = ''
    sarr = []
    sarr1 = []
    seq = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'K', 'k', 'J', 'j', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    for x in s:
        sarr.append(x)
    for x in sarr:
        a = random.choice(seq)
        sarr1.append(x + a)
    sarr1.reverse()
    for x in sarr1:
        b += x
    return b
def decoder(es):
    g = ''
    garr = []
    for x in es:
        garr.append(x)
    garr.reverse()
    n = 0
    for x in garr:
        if n == 1:
            g += x
        elif n % 2 == 1:
            g += x
        n += 1
    return g
while True:
    w = input('What do you want?')
    if w == 'encode':
        s = input('Enter your message: ')
        es = encoder(s)
        print(es)
    if w == 'decode':
        es = input('Enter encoded message: ')
        s = decoder(es)
        print(s)