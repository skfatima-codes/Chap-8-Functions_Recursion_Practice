# WAF to find length of a list(List is the pARAMETER)
cities=["Khi","LHR","ISB"]
movies=["Curuela","Kota Factory","IT"]
print(cities[2],end=" ")# WAF to print elemnts of the list in a single line
print(cities[1])
def print_len(list):
    print(len(list))
print_len(cities)    
print_len(movies)  


# WAF to print elemnts of the list in a single line
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)        