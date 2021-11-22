e, s, m = input().split()

e = int(e)
s = int(s)
m = int(m)

year = 1

while (e != 1 or s != 1 or m != 1):
    e = e-1 if e-1 != 0 else 15
    s = s-1 if s-1 != 0 else 28
    m = m-1 if m-1 != 0 else 19
    year += 1
    
print(year)