# 0802 lesson prac : added name: 謝安
# kenny到此一遊111
"""
以下的部分，都要用2個以上的while
"""
"""
1.)  
透過2個while  
印出 3*3 乘法表
"""
print("1")
x=1
while x<=3:
    y=1
    while y<=3:
        print(x,"*",y,"=",x*y)
        y=y+1
    x=x+1
"""透過2個while  
印出乘法表 如下
3*3=9
3*2=6
3*1=1
2*3=5
2*2=4
2*1=2
1*3=3
1*2=2
1*1=1
"""
print("2")
x=3
while x>=1:
    y=3
    while y>=1:
        print(x,"*",y,"=",x*y)
        y=y-1
    x=x-1
"""
3.)  
透過2個while  
印出乘法表 如下
3*1=3
3*2=6
3*3=9
2*1=2
2*2=4
2*3=6
1*1=1
1*2=2
1*3=3
"""
print("3")
x=3
while x>=1:
    y=1
    while y<=3:
        print(x,"*",y,"=",x*y)
        y=y+1
    x=x-1
"""
4.)  
透過2個while  
印出乘法表 如下
1*3=3
1*2=2
1*1=1
2*3=6
2*2=4
2*1=2
3*3=9
3*2=6
3*1=3
"""
print("4")
x=1
while x<=3:
    y=3
    while y>=1:
        print(x,"*",y,"=",x*y)
        y=y-1
    x=x+1
"""
5.)  
透過2個while  
印出乘法表 如下
1*1=1
2*1=2
2*2=4
3*1=3
3*2=6
3*3=9
"""
print("5.)=========")

x=1
while x<=3:
    y=1
    while y<=x:
        print(x,"*",y,"=",x*y)
        y=y+1
    x=x+1
"""
6.)  
透過2個while  
印出乘法表 如下
1*1=1
1*2=2
1*3=3 
2*1=2
2*2=4
3*1=3
"""
print("6")
x=1
while x<=3:
    y=1
    while y<=3-(x-1):
        print(x,"*",y,"=",x*y)
        y=y+1
    x=x+1
"""
7.)  
透過2個while  
印出 3*3 乘法表
但是數字的輸出 請用國字
例如
壹 乘上 壹 等於 壹
壹 乘上 貳 等於 貳
……
參 乘上 參 等於 玖
提示 
請參考之前的數字轉國字的範例，並翻寫成 def 函數
"""
"""
印出 3*3 乘法表
但是數字的輸出 請用國字
"""
print("7")
list1=["零","壹","貳","參","肆","伍","陸","柒","捌","玖"]
x=1
while x<=3:
    y=1
    while y<=3:
        print(list1[x],"*",list1[y],"=",list1[x*y])
        y=y+1
    x=x+1
#######
