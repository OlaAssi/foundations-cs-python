def evenList(lst):
    while True:
        try:
            num = int(input('Enter an integer(to end enter 0): '))
            if num == 0:
                break
            lst1.append(num)
        except:
            continue

    newlst=[]
    for i in lst:
        if i%2 == 0:
            newlst.append(i)
    return newlst


lst1=[]
print(evenList(lst1))