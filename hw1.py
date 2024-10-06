import math
class Complex:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return f'{self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}i'
 
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a + other.a, self.b + other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a + other, self.b)
        raise NotImplementedError
 
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a - other.a, self.b - other.b)
        if isinstance(other, (int, float)):
            return Complex(self.a - other, self.b)
        raise NotImplementedError
 
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.a*other.a - self.b*other.b, self.a*other.b + self.b*other.a)
        if isinstance(other, (int, float)):
            return Complex(self.a*other, self.b*other)
        raise NotImplementedError
 
    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2), (self.b*other.a - self.a*other.b)/(other.a**2 + other.b**2))
        if isinstance(other, (int, float)):
            return Complex(self.a/other, self.b/other)
        raise NotImplementedError
 
    def toexp(self):
        if self.b != 0:
            return (str(math.sqrt(self.a**2+self.b**2))+'e^'+str(math.atan(self.b/self.a)))
        elif self.a>0:
            return (str(abs(self.a))+'e^0')
        else:
            return (str(abs(self.a))+'e^'+str(math.pi))
