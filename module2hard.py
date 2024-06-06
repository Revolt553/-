import math
import random

n = random.randint(3, 20)

print(n)

for i in range(1, math.ceil(n / 2)):
    for j in range(i+1, n):
        if (i + j) % n == 0 or n % (i + j) == 0:
            print(str(i) + str(j), end='')




'''import random

n = random.randint(3, 20)
print(n)

password = []

for i in range(1, n):
    for j in range(i+1, n):
        if n % (i+j) == 0:
            b = i, j
            password.append(b)
for k in password:
   print(str(k[0]) + str(k[1]), end='')'''
