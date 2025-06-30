# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# c=int(input("Enter a number"))
# average=(a+b+c)/3
# print(average)
# Function Definition
def avg():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    c=int(input("Enter a number"))
    average=(a+b+c)/3
    print(average)
    # return if i return the function it will throw an error
    
a=avg() #Funtion Call
print("Thanks for solving") # when we want to repaet the logic multiple times (Reuse of logic)
b=avg() 
print("Thanks for solving")   
c=avg()   
print("Thanks for solving") 

