n1 = {5, 8, 4, 10}
n2 = {4, 1, 5}
n3 = {18, 21, 7}

union = n1 | n2 | n3
print(union)

for pares in union:
    if pares %2 == 0 :
        print(pares)