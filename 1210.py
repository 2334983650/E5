
from time import clock
def Fib1(n):
    if n==0 or n==1:
        return n
    else:
        f1,f2=0,1
        for i in range(2,n+1):
            f1,f2=f2,f1+f2
        return f2
     
def Fib2(x):
    if x==0 or x==1:
        return x
    else:
        return Fib2(x-1)+Fib2(x-2)
 
n=eval(input("please input a number:"))
start=clock()
f1 = Fib1(n)
runtime=clock()-start
print("使用循环递推的方法求第%d项斐波那契数为:%d"%(n,f1))
print("使用了%d秒"%(runtime))
start=clock()
f1 = Fib2(n)
runtime=clock()-start
print("使用递归的方法求第%d项斐波那契数为:%d"%(n,Fib2(n)))
print("使用了%d秒"%(runtime))
#def Fib3(n):
#    fibb=[0,1]
#    for i in range(2,n+1):
#        fibb.append(fibb[i-1]+fibb[i-2])
#    return fibb[n]
#start=clock()
#f1 = Fib3(n)
#runtime=clock()-start
#print("使用递推列表的方法求第%d项斐波那契数为:%d"%(n,Fib3(n)))
#print("使用了%d秒"%(runtime))
#def fibb3(n,f1=0,f2=1):
#    if n==0:
#        print(n,f1,f2)
#        return f1
#    print(n,f1,f2)
#    return fibb3(n-1,f2,f1+f2)
#start=clock()
#f3=fibb3(n)
#runtime=clock()-start
#print("使用尾循环递推的方法求第%d项斐波那契数为:%d"%(n,f3))
#print("使用了%d秒"%(runtime))
