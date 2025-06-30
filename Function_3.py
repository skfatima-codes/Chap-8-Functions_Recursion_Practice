# Default Parameter Values
def goodday(name,ending="Thanks"):# it means agr hm ending ko koi value na dain to by default it will print "Thnaks"
# def goodday(name,ending): it will that we missed one argumnet
    print(f"Good day! {name}")
    print(ending)


goodday("Fatima") 

# Multiplication of two numbers
# def cal_product(a,b):
    # a=2
    # b=3
#     product=a*b
#     print(product)
#     return product
# cal_product(24,5)
def calc_product(a,b=3):
    print(a*b)
    return a*b
calc_product(2)


