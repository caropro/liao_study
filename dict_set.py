#coding=utf-8
dic={"a":1,"b":2,"c":3}
print(dic)

dic["d"]=4
print(dic["d"],dic)
#可以添加元素

print("e" in dic)
#判断字典内有无元素

print(dic.get("e",0))
#判断字典内有无元素，没有则返回0

print(dic.pop("a"))
print(dic)
#还是可以用pop来移除元素

s={1,2,3}
print(s)

s.add(4)
s.add(4)
print(s)
#add添加元素到集,但不会出现重复元素

s1={1,2,3}
s2={2,3,4}
print(s1&s2)
print(s1|s2)
#集合间的交集，和并集

a=['c','a','b']
a.sort()
print(a)

a='abc'
print(a.replace('a','A'))
b=a.replace('a','A')
print(b)
print(a)

a={1,2,3}
a=(1,2,3)
print(a)
print(a[1])
#set不支持索引,元组可以

a=set("deoxyribonucleicacid")
print(a)
a=tuple("deoxyribonucleicacid")
print(a)
#元组不会消除重复元素，但集会