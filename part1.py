def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

N = input('Enter positive integer n:')
if N.isdigit() and int(N) > 0:
    N = int(N)
    print('n! =', factorial(N))
