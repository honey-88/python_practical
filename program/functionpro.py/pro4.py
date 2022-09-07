# *args

def myfun(*args):
    sum = 0
    for i in args:
        sum-=i

    print(sum)

myfun(12,345,32,78,45)