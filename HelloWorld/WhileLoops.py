c = 0

while c < 5:
    print(c)
    c += 1

c = 0

while c < 10:
    print(c)

    if c == 4:
        break
    c += 1

c = 0

while c < 10:
    c += 1
    if c == 3:
        continue
    print(c)

c = 0

while c < 10:
    c += 1
    if c == 3:
        pass
    print(c)