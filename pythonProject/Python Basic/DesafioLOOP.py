"""
usar for ou while
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
"""
aux = 10
for cont in range(0,9):
    for aux1 in range(1):
        print(f'{cont}  {aux}')
        if aux == 1:
            break
        aux -= 1

#ou posso usar
print()
print('---------------------------------')
print()

for p,r in enumerate(range(10,1,-1)):
    print(p,r)