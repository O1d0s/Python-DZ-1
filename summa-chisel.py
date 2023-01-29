n = int(input())
pos=0
s=0
while n>0:
    pos = n % 10
    s += pos
    n //= 10
print(s)