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
 
    def __toTrig__(a,b):
        if abs(b)>1.0e-15:
            return (math.sqrt(a**2+b**2),math.atan(y/x))
        elif a>0:
            return (math.sqrt(x**2+y**2),0)
        else:
            return (math.sqrt(x**2+y**2),math.pi)
