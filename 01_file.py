# read function in file .....
'''f=open('sample.txt','r')
data=f.read()
# data=f.read(5)  #it wil print 5 character
print(data)
f.close()
'''

# readline() function in file...
# f=open('sample.txt','r')
# data=f.readline()
# print(data)
# f.close()

# write () function in file...
# f=open('another.txt','w')
# f.write("hello i am the owner of this file pl z write it on file")
# f.write("this is suraj pathak from khatima")
# f.close()

# append function in file...
f = open('another.txt','a')
f.write("this is appended text")
f.close()

#with open as f function...(using this function now we dont need to add f.close() in the last)
with open('another.txt','r') as f:
    a = f.read()

with open('another.txt','w') as f:
    a = f.write(" i me and mai")

