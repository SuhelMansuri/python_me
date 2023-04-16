def process(fixed ,*args, **kwargs):
    print(fixed)
    print(args)
    print(kwargs)

process(10, 20, 30, 40, 50, 'John', 100, 110, k1 = 'Suhel', k2 = 'Test1', k3 = 2000)