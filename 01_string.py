a="suraj 'bhai' "
print(a)

b='pankaj "bhai" '
print(b)

c='''suraj bhai ritu bahen
pankaj bhai and...
    maa  papa'''
print(c)

#how to check type of variable..
name="suraj"
print(type(name))

#string concatination..
sp="good morning, "
jp="suraj"
print(sp+jp)

#string slicing.......
#string index accesing
namee="surajpathak"
print(namee[0:6])
print(namee[0:])
print(namee[:7])

# Negative indices
print(namee[-7:-1]) 


#string function
story= '''suraj is a amazing boy
he is going to earn his first 100 doller'''
print(story)

print(len(story))

print(story.endswith("doller"))

print(story.count("i"))

print(story.count("he"))

print(story.capitalize())

print(story.find("boy"))

print(story.replace("suraj","code with suraj"))

