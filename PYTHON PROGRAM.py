#!/usr/bin/env python
# coding: utf-8

# # Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.

# In[1]:


#PRINT HELLO WORLD
    
print("Hello world")


# # how to take two input in a same line 
# 
# x, y=map(int, input().split())
# 

# # How to take output Upto 2 precision
# 
# print(format(256.2145,".2f"))
# print(round(234.4467,2))

# In[2]:


# convert integer to list

n=int(input())
a=list(map(int,str(n)))
print(a)


# In[ ]:


# ARITHMATIC OPERATION

n1=float(input("Enter first number :"))
n2=float(input("Enter second number :"))
print("Addition=",n1+n2)
print("Substraction=",n1-n2)
print("Multiplication=",n1*n2)
print("Division=",n1/n2)
print("Modulo=",n1%n2)


# In[10]:


#QUADRATIC EQUATION

import cmath
a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
d=(b*b)-(4*a*c)
x=(-b+cmath.sqrt(d))/2*a
y=(-b-cmath.sqrt(d))/2*a
print(x,y)


# In[13]:


#SWAP TWO NUMBERS

a=int(input("Enter a :"))
b=int(input("Enter b :"))
a=a+b
b=a-b
a=a-b
print(a,b)


# In[3]:


#POSITIVE OR NEGETIVE NUMBER

n=int(input("Enter any number"))
if n>=0:
    print("Positive")
else:
    print("Negetive")


# In[11]:


#Sum of first N natural number

n=int(input("Enter upto which you want sum"))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)
    


# In[23]:


#Sum of numbers in a given range

lb=int(input("Enter the lower bound:"))
ub=int(input("Enter the Upper bound:"))
sum=0
for i in range(lb,ub+1):
    sum=sum+i
print(sum)


# In[29]:


#Greatest of the Three numbers

n1=int(input("Enter First number :"))
n2=int(input("Enter Second  number :"))
n3=int(input("Enter Third number :"))
if n1>n2 and n1>n3:
    print(n1,"is greater than",n2,"and",n3)
elif n2>n1 and n2>n3:
    print(n2,"is greater",n1,"and",n3)
else:
    print(n3,"is greater",n1,"and",n2)


# In[37]:


#Leap year or not 

n=int(input("Enter any Year :"))
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


# In[49]:


# A number is prime or not

n=int(input("Entre any number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Please enter another number")


# In[63]:


# Prime number upto given Range

lb=int(input("Enter the LB:"))
ub=int(input("Enter the UB:")) 
for i in range(lb,ub+1):
    t=0
    for j in range(2,i):
        if i%j==0:
            t=1
            break
    if t==0 and i!=1:                                          1!=0 bcz 1 is not a prime number
        print(i,end=" ")
        


# In[69]:


#Sum of Two digit number   ( 23=2+3=5)

n=int(input("Enter any number"))
a=n//10
b=n%10
sum=a+b
print(sum)


# In[1]:


# Sum of any digit number

n=int(input("Enter the number :"))
sum=0
while(n!=0):
    sum=sum+n%10
    n=n//10
print(sum)


# In[12]:


#Reverse a number

n=int(input("Enter any number :"))
reverse=0
while n>0:
    reminder=n%10
    reverse=reverse*10+reminder
    n=n//10
print(reverse)


# In[25]:


#A number is Palindrome or not

n=int(input("Enter number to be check:"))
t=n                                                   t is used as a temporary variable to check
reverse=0
while n>0:
    reminder=n%10
    reverse=reverse*10+reminder
    n=n//10
if t==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# In[33]:


#Armstrong number

n=int(input("Enter a number to be check :"))
t=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
if sum==t:
    print("Armstrong number")
else:
    print("Not a armstrong number")


# In[14]:


#Fibonacci Series upto nth term 

n=int(input("Enter a number upto which fibonacci :"))
a,b=0,1
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")


# In[44]:


#Factorial of a number using recursion
def fact(n):
    if n>=0:
        if n==0 or n==1:
            return 1
        else:
            return n*fact(n-1)
    else:
        print("Enter psitive number")
n=int(input("ENter any number"))
print(fact(n))#


# In[50]:


#Factorial of a number
n=int(input("Enter any number :"))
f=1
if n>=0:
    if n==0 or n==1:
        print("1")
    else:
        for i in range(1,n+1):
            f=f*i
print(f)

            


# In[56]:


#Power of a number

a=int(input("Enter a number :"))
b=float(input("Enter the power :"))
c=a**b
print(c)


# In[ ]:


#Factor of a number

n=int(input("Enter a number :"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

    


# #Check a number is Strong number    ( 145= 1! + 4! + 5! )
# 
# n=int(input("Enter a number :"))
# sum=0
# t=n
# while n!=0:
#     r=n%10
#     f=1
#     for i in range(1,r+1):
#         f=f*i
#     sum=sum+f
#     n=n//10
# if t==sum:
#     print("This is a strong number")
# else:
#     print("Not  a strong number")

# In[9]:


#Check a number is perfect number               6= 1*2*3=1+2+3

n=int(input("Enter a number :"))
t=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if sum==t:
    print("perfect number")
else:
    print("not a perfect no")
    
    


# In[38]:


#Check a number is Automorphic or not           a square of any number end with that number   25*25= 625  end of (625) is 25

n=int(input("Enter a number :"))
a=n*n
t=0
while(n!=0):
    if(n%10!=a%10):
        print("Not Automorphic number")
        t=1
    n=n//10
    a=a//10
if(t==0):
    print("Automorphic number")


# In[9]:


#Check a number is Harshad number          a number whose some is divide the number    153 / 1+5+3 = 17

                                                        
n=int(input("Enter a number :"))    
sum=0
t=n
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
if t%sum==0:
    print("yes")
else:
    print("no")


# In[19]:


#Check a number is Abundant number or not            #sum of its proper divisors is greater than the number. 
                                                                  #  12 = 1,2,3,4,6    1+2+3+4+6 =16 >12
    
n=int(input("Enter a number :"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("Abundant Number")
else:
    print("Not a abundant number")


# In[ ]:


a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
for i in range a:
    for j in range 


# In[2]:


#Seperation keywork

print("My", "name", "is", "Monty", "Python.", sep="**")


# In[1]:


#Sleep function

import time

for i in range(1,6):
    print(i,"Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")


# In[ ]:




