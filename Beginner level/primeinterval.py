n=int(input('enter the number')
k=int(input('enter the number')
for num in range(n,k):
if(num>1):
for i in range(2,num):
if(num%i==0):
    break
else:
    print('num')
