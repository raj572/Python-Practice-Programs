'''
?@?@?
ABCD
@?@
AB
?
'''

# Print the pattern
for i in range(5, 0, -2):
    for j in range(i):
        if j % 2 == 0:
            print('?', end='')
        else:
            print('@', end='')
    print()

    if i > 1:
        for j in range(1, i):
            print(chr(64 + j), end='')
        print()