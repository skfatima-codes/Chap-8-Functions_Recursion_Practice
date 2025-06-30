# def calc_sq(a):
#     square=a*a
#     print(square)
#     return square
# calc_sq(4)
# calc_sq(5)
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(fact(3))

# Check whether te no is prime or not
def check_prime(n):
    for i in range(2,n):
        if n<2:
            return False
        if n%i==0:
            return False
    return True
print(check_prime(4))    
print(check_prime(3))    
    
# def prime(n):
#     for i in range(2,n):
#         if n<2:
#             print("We can check it without any restriction")
#     if n%i==0:
#         print("The no is not a prime no")
#     else:
#         print("The no is prime no")
# prime(4)   

# Sum of even no in aa list     
def even_sum(nums):
    sum=0
    for n in nums:
        if n%2==0:
            sum=sum+n
        # print(sum)
    return sum
# even_sum([2,3,4,6,7])       
print(even_sum([2,3,4,6,7]))  

#  Function with default parameter
def def_para(naming,ending="Shutup"):
    print("Hello")
    print(naming)
    print(ending)

def_para("HI") 

# USD to INR
def converter(usd_value):
    inr_value=usd_value*83
    print(inr_value)
converter(3)

# even or odd
def check(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
check(5)        
  

    



  
    
    
    




