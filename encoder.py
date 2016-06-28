import random
s = input("Enter your message: ")
b = ''
sarr = []
sarr1 = []
seq = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'K', 'k', 'J', 'j', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
n = 0
for x in s:
    sarr.append(x)
    n += 1
n = 0
for x in sarr:
    a = random.choice(seq)
    sarr1.append(x + a)
sarr1.reverse()
print(sarr1)
for x in sarr1:
    b += x
print(b)

