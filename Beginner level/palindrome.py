k=int(input('enter a number'))
temp=k
rev=0
while(k>0):
  m=k%10
  rev=rev**10+m
  k=k//10
if(temp==rev):
 print('palindrome')
else:
 print('not palindrome')
