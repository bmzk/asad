a=0
k=0.005
g=10000*5
b=0
for i in range(30*12):
    a=a+g+b
    b=int(a*k) 
    print(str(i).center(5),str(i//12+1).center(2),'年',str(i%12+1).center(2),'月',
    'a=',str(a/100).ljust(9),'b=',str(b/100).ljust(9))
