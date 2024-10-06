import math
class Complex:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __repr__(self):
        return f'{self.a}{"-" if self.b < 0 else "+"}{abs(self.b)}j'
 
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
 
 
c1 = Complex(1, 2)
c2 = Complex(7, -8)
print(c1, c2)
print(c1 + c2)


class Complex:
    
    def __init__(self,r,a):
        self.__re=r*math.cos(a)
        self.__im=r*math.sin(a)
        
    def get_re(self):
        return self.__re
    def set_re(self,v):
        raise AttributeError
    def del_re(self):
        raise AttributeError
    re=property(get_re,set_re,del_re,"Действительная часть read-only")   
    
    def get_im(self):
        return self.__im
    def set_im(self,v):
        raise AttributeError
    def del_im(self):
        raise AttributeError
    im=property(get_im,set_im,del_im,"Мнимая часть read-only")       
    
    def __str__(self):
        if abs(self.__im)>1.0e-15:
            if self.__im<0:
                sim="-"
            else:
                sim="+"
            return "("+str(self.__re)+sim+"I*"+str(abs(self.__im))+")"
        else:     
            return "("+str(self.__re)+"+I*0)"
        
    def toTrig(x,y):
        if abs(y)>1.0e-15:
            return (math.sqrt(x**2+y**2),math.atan(y/x))
        elif x>0:
            return (math.sqrt(x**2+y**2),0)
        else:
            return (math.sqrt(x**2+y**2),math.pi)
            
    def __add__(self,o):
        re_sum=self.__re+o.__re
        im_sum=self.__im+o.__im
        (r_sum,a_sum)=Complex.toTrig(re_sum,im_sum)
        return Complex(r_sum,a_sum) 
        
    def __sub__(self,o):
        re_sub=self.__re-o.__re
        im_sub=self.__im-o.__im
        (r_sub,a_sub)=Complex.toTrig(re_sub,im_sub)
        return Complex(r_sub,a_sub) 
        
    def __mul__(self,o):
        re_pro=self.__re*o.__re-self.__im*o.__im
        im_pro=self.__im*o.__re+self.__re*o.__im
        (r_pro,a_pro)=Complex.toTrig(re_pro,im_pro)
        return Complex(r_pro,a_pro) 
 
    def __truediv__(self,o):
        a=self.__re
        b=self.__im
        c=o.__re
        d=o.__im
        zz=c**2+d**2
        aa=(a*c+b*d)/zz
        bb=(b*c-a*d)/zz
        (r_div,a_div)=Complex.toTrig(aa,bb)
        return Complex(r_div,a_div)
        
    def cabs(self):
        return math.sqrt(self.__re**2+self.__im**2)
 
        
q1=Complex(1,0)
q2=Complex(1,math.pi*0.5)
q3=q2*q2
print("q3=",q3)
 
a = Complex(1, math.pi/2)
b = Complex(1, 0)
print("a=",a)
print("b=",b)
print(a-b)
