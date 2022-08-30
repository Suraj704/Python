# 4!= 1*2*3*4 = 24

# n=int(input("enter the number:"))
# product=1
# for i in range(n):
#     product=product * (i+1)
# print("factorial of given no is:",product)

# factorial function
def factorial_itr(n):
    product=1
    for i in range(n):
        product=product * (i+1)
        return product
f = factorial_itr(6)
print("factoral of no is: ",f)
