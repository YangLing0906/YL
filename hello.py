for i in range(6):
    print(i)

    print(list(range(6))) 
#name =input("please enter you name: ")
#print(name)

print(100*100)



print(r'\\\\')#表示" "内默认不进行转义
#表示多行
print('''line1
line2
line3''')
print(r'''hello\n \# 未进行转义
world''')#r" 内部未进行转义，表示\以后的转义无效

#bool运算符
age =19
if age >= 18:
    print('adult')
else:
    print('teenager')

Answer=True #bool类型
# /浮点数除法 
# //地板除，整数的除法
# %取余数 10%3
print(10/3,10//3,10%3)
ord('A') #ord函数
print(ord("A"))
print(chr(65)) #chr函数
#
# 日期2021.1.23
x=b'ABC'
print(x)
print(len('中文'))#len 函数的使用

#数组
classmates=['Micheal','Bob','Tony']  #数组元素已经固定 0,1,2，list是一种有序集合，可以随意添加或者删除其中的元素
print(classmates)
print(len(classmates))
for i in range(3): # for循环
    print(classmates[i])
#用索引来访问list中的元素的位置，索引从0开始，但是得确保索引不要越界，不然会报错
print(classmates[-1])  #-1直接访问数组的最后位置，以此类推，可以获取倒数第2个、倒数第3个：
classmates.append('Adma') #可以在list中追加元素在末尾
print(classmates)
print('####123')
print(classmates[3])

classmates.insert(1,'Jack')#也可以在list表中其他位置插入元素
print(classmates[1])
print('#####')
for j in range(5):
    print(classmates[j],j)

classmates.pop() #在数组中删除元素，末尾的元素 ,Adma
classmates.pop(3)# 删除制定位置的元素，i为索引位置，Tony

print(classmates)

#2021.1.24
print('--------2021.1.24-------')

classmates[0]='YL'
print(classmates)

array=['YL',123,True] #list表中的数据类型也可以不同
array1=['a',['a','b'],'c'] #list表元素也可以是另外一个数组
print(len(array1))

print('----------------------')
p=['a','b']
g=['a','c',p,'d']

print(g[2][1])#获取p中的元素b，g可以看做是一个二维数组

L=[]
print(len(L)) #list表中没有元素的话，她的长度也为0，空的list

print('--------')

classmates=('Michael','Bob','YL') #另外的一种表，tuple(),一旦初始化就不能改变，不能修改，可以使用classmates(0),classmates(-1),但是不能修改值
print('tuple使代码更安全')
t=(1,2) #在定义tuple的时候就要把元素定下来
u=()# 定义空的tuple
v=(1,)  #当定义一个元素的时候,加上一个',',消除歧义

t = ('a', 'b', ['A', 'B'])#tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

print('---------分隔线---------')
#循环和判断，计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
age=20
if age>18: #就把缩进的两行print语句执行了，否则，什么也不做
    print('you age is',age)
    print('adult')
else:
    print('you age is',age)
    print('teenager')

#age = 3 #当然上面的判断是很粗略的，完全可以用elif做更细致的判断,elif 是else if 的缩写
age = input()
age =int(age) #将输入的字符型转化为整型
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

names = ['Michael', 'Bob', 'Tracy']
for name in names: #name为在names中元素的名字
    print(name)
print('---------------------分割线--------------------------')
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


