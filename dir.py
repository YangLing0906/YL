#pythonz自置字典，dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  #绑定值
print(d['Michael'])
d['Adam'] = 67
d['Jack'] = 90
print(d['Jack'])
print( 'Thomas' in d)  #当元素不存在list中使用False返回
print(d.get('Jack')) #使用get来获取List中元素的value
#当需要删除Key的时候，对应得value也会被删除，要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)   #Bob已经被删除，dict内部存放的顺序和key放入的顺序是没有关系的
#和list比较，dict有以下几个特点：查找和插入的速度极快，
# 不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
#而list相反：查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
s = set([1, 2, 3])#传入参数是[1,2,3],而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素
#显示的顺序也不表示set是有序的
print(s) #set和dict类似，也是一组key的集合，
#但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s =set([1,1,2,2,3,3])
print(s) #重复元素自动过滤
s.add(4) #s.add(key)，添加元素
print(s)
s.remove(4) #移除元素
print('------------------------',s)
print("------------------分割线-----------------")
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)




