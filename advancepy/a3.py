class practical:
    def findfactorial(self,num):
        f = 1
        for i in range(1,num+1):
            f*=i

        print("factorial = ",f)

obj = practical()
num = int(input("enter a number  :"))
obj.findfactorial(num)