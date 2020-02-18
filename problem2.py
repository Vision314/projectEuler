max = 4_000_000
sum = 0
f0 = 0
f1 = 1
f2 = 0

while(f2 < max):
    f2 = f0 + f1
    sum += f2 if f2 % 2 == 0 else 0
    f0 = f1
    f1 = f2
print(sum)
