def checkPassword(str):
    if len(str)>=8:
        checkup = 0
        checklow = 0
        checkcharacter = 0
        checkdigit = 0
        for i in str:
            if i.upper():
                checkup +=1
            if i.lower():
                checklow +=1
            if i.isdigit():
                checkdigit +=1
            if i == '#' or i == '?' or i == '!' or i == '$':
                checkcharacter +=1
        if checkup != 0 and checklow != 0 and checkcharacter != 0 and checkdigit != 0:
            print('Strong password')
        else:
            print('Weak password')
    else:
        print('Weak password')


password = input('Enter password: ')
checkPassword(password)