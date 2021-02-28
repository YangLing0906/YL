h = 1.75
w = 80.5
t= w/h**2
if t< 18.5:
    print('Thiner')
if  18.5<t<25:
    print('Normal')
if  25<t<28:
    print('Fat')
else :
    print('So Fat')

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)