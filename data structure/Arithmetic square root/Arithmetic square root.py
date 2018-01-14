#求平方根程序：y = (y+x/y)/2（）该牛顿迭代公式是怎么来的？？？
def square_root(x):
    y = 1.0
    while abs(y*y-x)>1e-6:
        y = (y+x/y)/2
    return y
s = square_root(8)
print(s)