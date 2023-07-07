def checkValid(address):
    lst=address.split('.')
    numlist = []
    check1=True
    for ele in lst:
        if ele.startswith('0') and len(ele)>1:
            check1=False

    check=all(num.isdigit() for num in lst)

    if check and check1 and len(lst)==4:
        numlist=[int(i) for i in lst]
        if all(num>=0 and num<=255 for num in numlist):
            print('Valid IPv4 address ')
        else:
            print('Invalid IPv4 address')
    else:
        print('Invalid Ipv4 address')


IPv4=input('enter address:')
checkValid(IPv4)
