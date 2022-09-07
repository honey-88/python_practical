# *args

def myfun(*args):
    sum = 0 
    for i in args:
        sum+=i

    print(sum)

myfun(12,23,45,778,44,32)
