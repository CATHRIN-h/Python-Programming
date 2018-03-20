t=int(input('enter the number'))
count=0
for i in range (1,t):
    if(t%i==0):
        count=count+1 
        print('yea,its a prime number')
    else:
        print('nah,its not a prime number')
