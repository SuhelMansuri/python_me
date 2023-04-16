from read_valid_integer import read_valid_integer
def factorial(n):
    if n < 0:
        ve = ValueError('Unable to calculate factorial of nagative number')
        raise ve
    p = 1
    for i in range(1, n+1):
         p *= i
         print('i-----',i)
         print('p-----',p)
    return p
     
def main():
    valid = False
    while not valid:
        valid = True
        try:
            n = read_valid_integer('Input an integer to get the factorial: ')
            f = factorial(n)
            print(f)
        except ValueError as v:
            print(v.args)
            valid = False

if __name__ == '__main__':
    main()