'''def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3

    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=max(7,9,40)
print(m)
'''
# program to convert cel to fahreheit
'''
def farh(cel):
    return(cel*(9/5))+32

c=37 
f=farh(c)
print("fahrenheit temp is"+ str(f))
'''

# program to print pattern
a=int(input("enter your no"))
for i in range(a):
    print("*"*(a-i))