mydisct= {
    "first":"quick value",
    "suraj":"A fullstact web devloper",
    "marks" : [1,54,87,57],
    "nesting":{"surya":"hello this is nesting 1st",
    "ramu":"2nd ex of nesting"}

}

print(mydisct)
print(mydisct['first'])
print(mydisct['marks'])
print(mydisct['nesting']['surya'])

#changing the value
mydisct["marks"]=[46,55,77]
print(mydisct["marks"])