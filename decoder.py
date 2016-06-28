s = input('Enter encoded message: ')
print(s)
g = ''
garr = []
for x in s:
    garr.append(x)
garr.reverse()
print(garr)
n = 0
for x in garr:
    if n == 1:
        g += x
    elif n % 2 == 1:
        g += x
    n += 1
print(g)
