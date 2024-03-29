# Special methods -Dumders
# difference between repr and str

class Complex:
    
    def __init__(self, real=1, img=1):
        self.real = real
        self.img = img
        
    def __str__(self):
        return f'{self.real} +i {self.img}'
    
    def __repr__(self):
        return f'Complex({self.real}, {self.img})'
    
    def __add__(self, other):
        r = self.real + other.real
        i = self.img + other.img
        z = Complex(r, i)
        return z
    def __sub__(self, other):
        r = self.real - other.real
        i = self.img - other.img
        z = Complex(r, i)
        return z
        
print(int.__add__(5, 15))

print(str.__add__('Hello, ', 'World!'))        
z1 = Complex(5, 6)
z2 = Complex(7, 8)

z3 = z1 - z2
print(z3)
# print(z1.__str__())
# print(z1.__str__())
# print(z1.__repr__())
# print(help(Complex))