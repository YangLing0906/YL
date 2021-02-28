sum=0
sums=[0,1,2,3,4,5,6,7,8,9]
for x in sums: #x为sums中的元素值
    sum=sum+x   #循环加
print(sum)
print('-----------------分割线----------------')

array=list(range(5)) #生产List表，range(5)就是生成0到4的整数序列
print(array)
sum=0
for x in range(1001):
    sum=sum+x
print(sum)
#第二种循环，只要满足条件就可以，不断循环，当不满足条件时自动退出，100以内的奇数和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
#如果要提前结束循环，可以用break语句：
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')