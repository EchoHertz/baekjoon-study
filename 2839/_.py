# while True:
a = int(input())
result = 0

if a == 4 or a == 7:
    result = -1
elif a % 5 == 0:
    result = a // 5
elif a % 5 == 1 or a % 5 == 3:
    result = a // 5 + 1
elif a % 5 ==2 or a % 5 == 4:
    result = a // 5 + 2    

print(result)






# 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 1 -1 1