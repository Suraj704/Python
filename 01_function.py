def percent(marks):
    return ((marks1[0]+marks1[1]+marks1[2]+marks1[3]+marks1[4]+marks1[5])/400)*100

marks1=[4,78,70,60,8,5]
percent1=percent(marks1)
print("percentage is:",percent1)

marks2=[1,5,8,3,7,9]
percent2=percent(marks2)
print("percentage is:",percent2)

marks3=[10,50,80,30,70,9]
percent3=percent(marks3)
print("percentage is",percent3)

#greeting function
def greet(name):
    print("good day "+name)

greet("suraj")
greet("pathak")

# greeting function through return
def greeting(name="unknown person"):
    gr="hello dosto "+ name
    return gr
mess=greeting("this is suraj the great")
print(mess)

mess2=greeting()
print(mess2)

# sum function
def mysum(num1,num2):
    return num1+num2

s=mysum(10,10)
print("sum of given no is:",s)

s1=mysum(5,10)
print("sum of given no is:",s1)

# strip function.............
i="       suraj is a full stack devloper"
print(i)
print(i.strip())