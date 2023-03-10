x = 6

def example():
    global x
    print(x)
    print(x+5)
   # x +=6
example()
def example1():
    globx = x
    print('globx',globx)
    globx+=5
    print('globx',globx)
    return globx
x = example1()
print('after return',x)