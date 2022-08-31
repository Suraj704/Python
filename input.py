a=int(input("enter the number of which you need table: "))
for i in range(1,11):
    print(str(a) + "*" + str(i) + "=" + str(a*i))
    #shortcut of above print line using f string
    # print(f"{a}*{i}={a*i}")