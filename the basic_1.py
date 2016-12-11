print ("hello,world")

s1=float(input("去年成绩"))
s2=float(input("今年成绩"))

r=abs((s1-s2)/s1*100)
if s1>s2:
    print("成绩下降了 %.1f %%" % r)
elif s1 == s2:
    print("成绩没变化")
else:
    print("成绩提升了了 %.1f %%" % r)
