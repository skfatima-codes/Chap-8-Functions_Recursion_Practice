def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(greatest(2,4,5)) 

# Celsius to Fahernhiet
def fah_cel(f):
    return 5*(f-32)/9

f=int(input("Enter a number"))
c=fah_cel(f)
print(f"{round(c,2)},C")

# Print a pattern by using recursion
def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)


pattern(3)

# Inches to cm
def inch_to_cm(inch):
    return inch*2.54
n=int(input("Enter the value in inches"))
print(f"The corresponding value of inches is {inch_to_cm(n)}")

# function to remove a given word from the list and strip it at the same time
def remove(l,word):
    n=[]

    for item in l:
      if not(item==word):
       n.append(item.strip(word))
    return n
   
l=["HArry","Rohan","Karan","an"]
print(remove(l,"an"))    
           
      
    


l=["Harry","Karan","Rohan"]
print(remove(l,"Harry"))

