def LIterator():
    for i in range(17):
        for j in range(17):
            if i == 16 or j <= 1:
                yield 'L'
            if j == 16:
                yield '\n'

print("".join(LIterator()))