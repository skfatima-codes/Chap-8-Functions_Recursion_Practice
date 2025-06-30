# def show(n):
#     if n==-1:
#         return
#     print(n)
#     show(n-1)
#     print("End")
# show(6) 
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
     
print(fact(5))

# First ten nantural no sum
def nat_num(n):
    if(n==0):
        return 0
    print(n)
    return nat_num(n-1)+n
sum=nat_num
print(sum)   

# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["Apple","Mango","Banana"]
# print_list(fruits)

# write a recursive function to reverse a string
 

      




    

    
 
 


    