for row in range(1,6):
    for col in range(1,row+1):
        if row%2==0:
            print("0",end="")
        else:
            print("1",end="")
    print()