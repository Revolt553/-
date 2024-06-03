import random

nam = random.randint(3, 20)
print(nam)

password = []

for i in range(1, nam):
    for j in range(i+1, nam):
        if nam % (i+j) == 0:
            b = i, j
            password.append(b)
for k in password:
   print(str(k[0]) + str(k[1]), end='')
