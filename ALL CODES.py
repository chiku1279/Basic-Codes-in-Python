#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('hello world')


# In[ ]:


a=5
b=10
c=a+b
print(c)


# In[ ]:


n=int(input("Enter any number"))
r=n**0.5
print("the square root of",n,"=",r)


# In[ ]:


a=int(input("enter side a:\n"))
b=int(input("enter side b:\n"))
c=int(input("enter side c:\n"))
p=(a+b+c)
s=p/2
area=(s*(s-a)*(s-b)*(s-c))**(0.5)
print("the area of triange=",area)


# In[ ]:


a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("entere c")) 
d=(b*b)-4*(a*c) 
x=(-b+d**0.5)/2*a 
y=(-b-d**0.5)/2*a
print(x)
print(y)


# In[ ]:


a=int(input("enter a :"))
b=int(input("enter b :"))
t=a                                  #swap with using third variable
a=b
b=t
print("after swapped a is equal to",a,"and b is equal to",b)


# In[ ]:


a=int(input("enter a :"))
b=int(input("enetr b :"))
a=a+b                             #swap without using third variable
b=a-b
a=a-b
print("after swap a is equal to",a,"and b is equal to",b)


# In[ ]:


import random
n=random.randint(10,20)
print(n)


# In[ ]:


n=float(input("Enter in kilmeter:"))
r=n*0.621371
print(n,"kilometer =",r,"miles")


# In[ ]:


c=float(input("Enter temp in celcius"))
f=(1.8*c)+32
print("Temperature in celcius =",f,"fahreheit")


# In[ ]:


n=int(input("enter any number:"))
if(n>0):
  print("Positive  +\n")
elif(n<0):
  print("Negetive  -\n")
else:
  print("Zero  0\n")


# In[ ]:


n=int(input("Enter any number"))
r=n%2
if(r==0):
  print("Even")
else:
  print("Odd")


# In[ ]:


n=int(input("Enter a year:"))
if(n%4==0):
  if(n%100==0):
    if(n%400==0):
      print("Leap year")
    else:
      print(" not a Leap year")
  else:
    print(" leap year")
else:
  print(" not a Leap year")


# In[ ]:


a=int(input("enter A:\n"))
b=int(input("enter B:\n"))
c=int(input("enter C:\n"))
if(a>b):
  if(a>c):
    print("A is greatest")
  else:
    print("C is greatest")
elif(b>c):
  print("B is greatest")
else:
  print("C is greatest")


# In[ ]:


n=int(input("Enter any number:"))
if n>1:
  for i in range(2,n):
      if n%i==0:
        print("Not a prime")
        break
  else:
    print("Prime")
else:
  print("not a prime")



# In[ ]:


n=int(input("Enter any number"))
c=1
for i in range(1,n+1):
  c=c*i
print(c)


# In[ ]:


n=int(input("Entre any number"))
c=1
for i in range(1,11):
  c=n*i
  print(n,"*",i,"=",c)


# In[ ]:


n=int(input("ENter any number"))
a=0
b=1
if(n<=0):
  print("PLese enter valid number")
elif(n==1):
  print(a,end="  ")
elif(n>=2):
  print(a)
  print(b)
  for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c


# In[ ]:


n= int(input("Enter a number: "))
sum = 0
t = num
while t> 0:
   d = t % 10
   sum += d ** 3
   t //= 10
if n == sum:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")


# In[ ]:


n=int(input("Enter number upto which sum is reqired"))
sum=0
for i in range(1,n+1):
  sum=sum+i
print(sum)


# In[ ]:


n = int(input("Enter number of terms "))
s = list(map(lambda x: 2 ** x, range(n)))
for i in range(n):
   print("2 raised to power",i,"is",s[i])


# In[ ]:


n=int(input("enter any number"))
for  i in range(1,n):
  if(i%2==0):
    print(i)


# In[ ]:


n=int(input("ENter any number :"))
print("The decimal value of", n, "is:")
print(bin(n), "binary.")
print(oct(n), " octal.")
print(hex(n), " hexadecimal.")


# In[ ]:


n=input("Enter any character")
print("The ascii value of",n,"=",ord(n))


# In[ ]:


a=int(input("enter a"))
b=int(input("enter b"))
if a>b:
  s=b
else:
  s=a
for i in range(1,s+1):
  if((a%i==0)and(b%i==0)):
    gcd=i
print("gcd/hcf=",i)


# In[2]:


a=int(input("enter a"))
b=int(input("enter b"))
if(a>b):
  m=a
else:
  m=b
while(1):
  if((m%a==0)and(m%b==0)):
    print("LCM=",m)
    break;
  m=m+1


# In[ ]:


n=int(input("enetr any number"))
for i in range(1,n+1):
  if(n%i==0):
    print(i)
  


# In[ ]:


n=int(input("Enter your choise 1-Adittion , 2-Substration , 3-Multiplication ,4-Division"))
a=int(input("Enter a"))
b=int(input("Enter b"))
if(n==1):
  print("Addition")
  r=a+b
  print(r)
elif(n==2):
  print("Substraction")
  r=a-b
  print(r)
elif(n==3):
  print("Multiplication")
  r=a*b
  print(r)
elif(n==4):
  print("Division")
  r=a/b
  print(r)
else:
  print("Wrong choise")




# In[1]:


import calendar
y=int(input("Enter a year"))
m=int(input("Enter  a month"))
print(calendar.month(y,m))


# In[ ]:


def Fab(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fab(n-1) + Fab(n-2))  
n = int(input("Enter the terms? "))   
if n <= 0:  
   print(" enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(Fab(i))


# In[ ]:



def ns(n):
   if n==1:
       return n
   else:
       return (n + ns(n-1))
num = int(input("Enter a number: ")) 
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",ns(num))


# In[ ]:


def facto(n):  
   if n == 1:  
       return n  
   else:  
       return (n*facto(n-1))   
n = int(input("Enter a number: "))  
if n < 0:  
   print("enter positive no")  
elif n== 0:  
   print("The factorial of 0 is 1")  
else:  
   print(facto(num)) 


# In[ ]:


def binary(n):
  if(n==0):
    return 0
  else:
    binary(int(n/2))
    print(n%2,end="")
n=int(input("Enter no"))
binary(n)


# In[ ]:


n=input("Enter a string")
s=n[::-1]
if(n==s):
  print("Palindrome")
else:
  print("not palindrome")


# In[ ]:


a = {0, 2, 4, 6, 8};
b = {1, 2, 3, 4, 5};
print("Union of a and b is",a | b)
print("Intersection of a and b is",a & b)
print("Difference of a and b is",a - b)
print("Symmetric difference of a and b is",a ^ b)


# In[ ]:


for i in range(4):
  for j in range(i+1):
    print("*",end=" ")
  print("\n")
    
    


# In[ ]:


a={1,2,3,4}
b={5,6,7,8}
print(a|b)


# In[ ]:





# In[ ]:


a = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(a[1]['name'])
print(a[1]['age'])
print(a[1]['sex'])


# In[ ]:


s=['a','b','c','d']
for i in range(len(s)):
  print("at index",i,s[i])


# In[ ]:


a=[[1,2,3],[4,5,6],[7,8,9]]
fl = [num for sublist in a for num in sublist]
print(fl)


# In[ ]:


a=[1,2,3,4,5,6,7]
print(a[2::])


# In[ ]:


a=[1,2,3,4,5,6,7]
print(a[:4:])


# In[ ]:


a=[1,2,3,4,5,6,7]
print(a[::-1])


# In[ ]:


a={'name-':'chiku','branch-':'cs','age-':'21'}
for key in a:
  print(key,a[key])


# In[ ]:


age={'ram':55,'shyam':20,'chiku':36}
for i in sorted(age,key=age.get):
  print(i,age[i])


# In[ ]:


a=[2,3,4,5]
if not  a:
  print("List is empty")
else:
  print("LIst is not empty")


# In[ ]:


try:
  a=100
  b=0
  q=a/b
  print(q)
except division_error:
  print("divison is not perfrmed")iku


# In[ ]:



a=['chiku','ram']
b=[2,4]
c=a+b
print(c)


# In[ ]:


a={'name':'chiku','class':'cs1','age':'21'}
n=input("ENter any key")
if n in a:
  print("key is present")
else:
  print("Key is Not present")


# In[ ]:


n=int(input("ENter in  how many chunk divided"))
l = [1,2,4,5,6,9,0,34,56,89,31,42]
[l[i:i + n] for i in range(0, len(l), n)]


# In[ ]:


a=293.344
print(float(a),type(a))
print(int(a),type(a))


# In[ ]:


a=[2,3,4,1]
for i in a[3:4:]:
  print(i)


# In[ ]:


n=input("ENter a string :")
for i in range(len(n)):
  for j in range(i+1,len(n)+1):
    print(n[i:j])


# In[ ]:


s=input("Enter a string")
for i in s:
  print(i,end="")


# In[ ]:


l=[2,4,3,1,5]
import random
n=random.randint(0,len(l))
print(l[n])


# In[ ]:


numbers = [2,3,3,5,1,2,5]
n=int(input("ENter a no"))
count = numbers.count(n)


print('Count of ',n, count)


# In[ ]:


a={ 'name':'chiku','branch':'cs','college':'siet','age':'21'}
a.pop("age")
print(a)


# In[ ]:


a=''' My name is sudhnshu singh 
     i am from kanpur
     how are you'''
print(a)


# In[ ]:


import time
s = time.time()
print("chiku")
e = time.time()
print(e - s)


# In[ ]:


l1 = ["chiku", "singh", "moh"]
l2 = [20, 12, 50]
print("List 1 : ", l1)
print("list 2 : ", l2)
d= {l1[i]: l2[i] for i in range(len(l1))}
print("list to dict    ",d)


# In[ ]:


n="  sudhanshu singh  "
print(n.strip())


# In[10]:


print(int(3/4))


# In[ ]:




