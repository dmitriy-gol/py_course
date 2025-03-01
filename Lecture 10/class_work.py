Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.vol = vol
    def __str__(self):
        return f'{self.brand}: {self.vol}'

    
my_new_car = Car('zaz', 0.9)
print(my_new_car)
zaz: 0.9
my_new_car
<__main__.Car object at 0x000001394D0ECAD0>
class Car:
    def __init__(self, brand, vol):
        self.brand = brand
        self.vol = vol
    def __str__(self):
        return f'str - {self.brand}: {self.vol}'
    def __repr__(self):
        return f'repr - {self.brand}: {self.vol}'

    
new = Car('zaz', 0.9)
print(new)
str - zaz: 0.9
new
repr - zaz: 0.9
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.vol = vol
        Car.counter += 1
    def __str__(self):
        return f'str - {self.brand}: {self.vol}'
    def __repr__(self):
        return f'repr - {self.brand}: {self.vol}'

    

new = Car('zaz', 0.9)
Car.counter
1
new = Car('zaz', 0.9)
Car.counter
2
new.counter
2
Car.__doc__
Car.__bases__
(<class 'object'>,)
class Empty:
    pass

e = Empty()
e
<__main__.Empty object at 0x000001394D0ED760>
Empty.__bases__
(<class 'object'>,)
new.__dict__
{'brand': 'zaz', 'vol': 0.9}
Car.__dict__
mappingproxy({'__module__': '__main__', 'counter': 2, '__init__': <function Car.__init__ at 0x000001394D0F8040>, '__str__': <function Car.__str__ at 0x000001394D0F80E0>, '__repr__': <function Car.__repr__ at 0x000001394D0F8180>, '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__name__
'Car'
class Car:
    counter = 0
    def __init__(self, brand, vol):
        self.brand = brand
        self.vol = vol
        Car.counter += 1
    def drive(self, dist):
        print(f'проехал {dist} км')
    def __str__(self):
        return f'str - {self.brand}: {self.vol}'
    def __repr__(self):
        return f'repr - {self.brand}: {self.vol}'

    
new = Car('zaz', 0.9)
new.drive(123)
проехал 123 км
hasattr
<built-in function hasattr>
setattr
<built-in function setattr>
fetattr
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    fetattr
NameError: name 'fetattr' is not defined. Did you mean: 'getattr'?
getattr
<built-in function getattr>
new
repr - zaz: 0.9
new.brand
'zaz'
getattr(new, 'brand')
'zaz'
getattr(new, 'bra')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    getattr(new, 'bra')
AttributeError: 'Car' object has no attribute 'bra'
getattr(new, 'brand', False)
'zaz'
res = getattr(new, 'brand', False)
res
'zaz'
if getattr(new, 'brand') != False:
    print(new.brand)

    
zaz
hasattr(new, 'brand')
True
hasattr(new, 'band')
False
if hasattr(new, 'brand') != False:
    print(new.brand)

    
zaz
if hasattr(new, 'brand') != False:
    print(new.brand)
else:
    print('False')

    
zaz
if hasattr(new, 'band') != False:
    print(new.brand)
else:
    print('False')

    
False
setattr(new, 'bnd', 1234)
new.__dict__
{'brand': 'zaz', 'vol': 0.9, 'bnd': 1234}
new.hello = 999
new.__dict__
{'brand': 'zaz', 'vol': 0.9, 'bnd': 1234, 'hello': 999}


class Animal:
    def __init__(self, color, age):
        self.color = color
        self. age = age
    def eat(self):
        print(f'животное {self.color} цвета кушает')
    def go(self):
        print('Животное двигается')
    def sleep(self):
        print('zzzz...')

        
class DomCat(Animal):
    def __init__(self, name,Animal color, age):
        
SyntaxError: invalid syntax
class DomCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)

        
cat = DomCat('Dima', 'black', 0)
cat.color
'black'
cat.name
'Dima'
cat.eat()
животное black цвета кушает
cat.sleep()
zzzz...
cat.go()
Животное двигается
class Animal:
    def __init__(self, color, age):
        self.color = color
        self. age = age
    def eat(self):
        print(f'животное {self.color} цвета кушает')
    def go(self):
        print('Животное двигается')
    def sleep(self):
        print('zzzz...')

        
class DomCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f'Name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}
    
SyntaxError: unterminated f-string literal (detected at line 6)
class DomCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f'Name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}'

    
cat = DomCat('Dima', 'black', 0)
cat
Name: Dima
	Age: 0
	Color: black
class DomCat(Animal):
    def __init__(self, name, color, age):
        self.name = name
        super().__init__(color, age)
    def __repr__(self):
        return f'Cat name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}'

    
cat = DomCat('Dima', 'black', 0)
cat
Cat name: Dima
	Age: 0
	Color: black

class DomCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id = DomCat.counter
        DomCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f'Name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}'

    
cat = DomCat('Dima', 'black', 0)
cat.__dict__
{'name': 'Dima', 'id': 123, 'color': 'black', 'age': 0}
cat._id = 9987897
cat._id
9987897
class DomCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.id_ = DomCat.counter
        DomCat.counter += 1
        super().__init__(color, age)
    def __repr__(self):
        return f'Name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}'

    
cat = DomCat('Dima', 'black', 0)
cat.id_ = 2345235
cat.id_
2345235

class DomCat(Animal):
    counter = 123
    def __init__(self, name, color, age):
        self.name = name
        self.__id = DomCat.counter
        DomCat.counter += 1
        super().__init__(color, age)
    def get_id(self):
        print(f'cat id: {self.__id}')
    def __repr__(self):
        return f'Name: {self.name}\n\tAge: {self.age}\n\tColor: {self.color}'

    
cat = DomCat('Dima', 'black', 0)
cat.__id
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    cat.__id
AttributeError: 'DomCat' object has no attribute '__id'
cat.__dict__
{'name': 'Dima', '_DomCat__id': 123, 'color': 'black', 'age': 0}
cat
Name: Dima
	Age: 0
	Color: black
cat.get_id
<bound method DomCat.get_id of Name: Dima
	Age: 0
	Color: black>
cat.get_id()
cat id: 123
cat.__init__()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    cat.__init__()
TypeError: DomCat.__init__() missing 3 required positional arguments: 'name', 'color', and 'age'



stack = []
def push(value):
    stack.append(value)

    
def pop():
    stack.pop()

    
push(1)
push(2)
push(3)
push(4)
stack
[1, 2, 3, 4]
pop()
stack
[1, 2, 3]
pop()
stack
[1, 2]
pop()
stack
[1]



class Stack:
    def __init__(self):
        self.stack = []
    def pus(self, val):
        self.stack.append(val)
    def pop():
        stack.pop()

        
s1 - Stack()
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    s1 - Stack()
NameError: name 's1' is not defined
s1 = Stack()
s1.push(1)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    s1.push(1)
AttributeError: 'Stack' object has no attribute 'push'. Did you mean: 'pus'?
s1.pus(1)
s1.pus(2)
s1.pus(3)
s1.pus(4)
s1.stack
[1, 2, 3, 4]
s1.pop()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    s1.pop()
TypeError: Stack.pop() takes 0 positional arguments but 1 was given
s2 = Stack()
s2.stack
[]
class Stack:
    def __init__(self):
        self.stack = []
    def pus(self, val):
        self.stack.append(val)
    def pop():
        stack.pop()

        
class Stack:
    def __init__(self):
        self.stack = []
    def pus(self, val):
        self.stack.append(val)
    def pop():
        stack.pop(self)

        
s1.stack
[1, 2, 3, 4]
s1.pop()
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    s1.pop()
TypeError: Stack.pop() takes 0 positional arguments but 1 was given
class Stack:
    def __init__(self):
        self.stack = []
    def pus(self, val):
        self.stack.append(val)
    def pop(self):
        stack.pop()

        
s1.pop()
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    s1.pop()
TypeError: Stack.pop() takes 0 positional arguments but 1 was given
class Stack:
    def __init__(self):
        self.stack = []
    def pus(self, val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()

        
s1.pop()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    s1.pop()
TypeError: Stack.pop() takes 0 positional arguments but 1 was given
a = 10
b = 11
a + b
21
a.__add__(b)
21
a.__sub__(b)
-1
help(int)
Help on class int in module builtins:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating-point
 |  numbers, this truncates towards zero.
 |
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |
 |  Built-in subclasses:
 |      bool
 |
 |  Methods defined here:
 |
 |  __abs__(self, /)
 |      abs(self)
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __and__(self, value, /)
 |      Return self&value.
 |
 |  __bool__(self, /)
 |      True if self else False
 |
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __float__(self, /)
 |      float(self)
 |
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |
 |  __format__(self, format_spec, /)
 |      Convert to a string according to format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |
 |  __int__(self, /)
 |      int(self)
 |
 |  __invert__(self, /)
 |      ~self
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __neg__(self, /)
 |      -self
 |
 |  __or__(self, value, /)
 |      Return self|value.
 |
 |  __pos__(self, /)
 |      +self
 |
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |
 |  __radd__(self, value, /)
 |      Return value+self.
 |
 |  __rand__(self, value, /)
 |      Return value&self.
 |
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __ror__(self, value, /)
 |      Return value|self.
 |
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |
 |      Rounding with an ndigits argument also returns an integer.
 |
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |
 |  __rsub__(self, value, /)
 |      Return value-self.
 |
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |
 |  __rxor__(self, value, /)
 |      Return value^self.
 |
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |
 |  __sub__(self, value, /)
 |      Return self-value.
 |
 |  __truediv__(self, value, /)
 |      Return self/value.
 |
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |
 |  __xor__(self, value, /)
 |      Return self^value.
 |
 |  as_integer_ratio(self, /)
 |      Return a pair of integers, whose ratio is equal to the original int.
 |
 |      The ratio is in lowest terms and has a positive denominator.
 |
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |
 |  bit_count(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |
 |      Also known as the population count.
 |
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |
 |  is_integer(self, /)
 |      Returns True. Exists for duck type compatibility with float.is_integer.
 |
 |  to_bytes(self, /, length=1, byteorder='big', *, signed=False)
 |      Return an array of bytes representing an integer.
 |
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.  Default
 |        is length 1.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  from_bytes(bytes, byteorder='big', *, signed=False)
 |      Return the integer represented by the given array of bytes.
 |
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.  Default is to use 'big'.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  denominator
 |      the denominator of a rational number in lowest terms
 |
 |  imag
 |      the imaginary part of a complex number
 |
 |  numerator
 |      the numerator of a rational number in lowest terms
 |
 |  real
 |      the real part of a complex number

a.__truediv__(b)
0.9090909090909091
a / b
0.9090909090909091
s = 'sdadawsd'
s1 = 'asdasdawsed'
s + s1
'sdadawsdasdasdawsed'
s.__add__(s1)
'sdadawsdasdasdawsed'
's' in s
True
s.__contains__('s')
True
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nexctcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
c = Cat('Cat', 5)
c1 = Cat('San', 6)
c + c1
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    c + c1
  File "<pyshell#206>", line 6, in __add__
    return self.age + nexctcat.age
NameError: name 'nexctcat' is not defined. Did you mean: 'nextcat'?
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
s + s1
'sdadawsdasdasdawsed'
c + c1
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    c + c1
  File "<pyshell#206>", line 6, in __add__
    return self.age + nexctcat.age
NameError: name 'nexctcat' is not defined. Did you mean: 'nextcat'?
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __add__(self, nextcat):
        return self.age + nextcat.age
    def __contains__(self, key):
        return key in self.name
    def __len__(self):
        return self.age
    def __lt__(self, nextcat):
        return self.age < nextcat.age

    
c = Cat('Cat', 5
c1 = Cat('San', 6)
        
SyntaxError: '(' was never closed
c = Cat('Cat', 5)
        
c1 = Cat('San', 6)
        
c + c1
        
11
len(c)
        
5
c < c2
        
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    c < c2
NameError: name 'c2' is not defined. Did you mean: 's2'?
c < c1
        
True
c1 < c
        
False
c
        
<__main__.Cat object at 0x000001394D112B40>

>>> 
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount = amount
...     def __add__(self, int_value):
...         return self.amount += int_value
...     def __sub__(self, int_value):
...         return self.amount -= int_value
...     
SyntaxError: invalid syntax
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount = amount
...     def __add__(self, int_value):
...         self.amount += int_value
...         return self.amount
...     def __sub__(self, int_value):
...         self.amount -= int_value
...         return self.amount
...     def __len__(self, int_value):
...         return self.amount
... 
...     
>>> w = Wallet(1000)
>>> w + 100
1100
>>> len(w)
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    len(w)
TypeError: Wallet.__len__() missing 1 required positional argument: 'int_value'
>>> W - 50
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    W - 50
NameError: name 'W' is not defined. Did you mean: 'w'?
>>> W -50
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    W -50
NameError: name 'W' is not defined. Did you mean: 'w'?
>>> w - 50
1050
>>> add(w)
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    add(w)
NameError: name 'add' is not defined
>>> w
<__main__.Wallet object at 0x000001394D1130B0>
>>> class Wallet:
...     def __init__(self, amount):
...         self.amount = amount
...     def __add__(self, int_value):
...         self.amount += int_value
...         return self.amount
...     def __sub__(self, int_value):
...         self.amount -= int_value
...         return self.amount
...     def __len__(self):
...         return self.amount
... 
...     
>>> w = Wallet(1000)
>>> w + 100
1100
>>> len(w)
1100
>>> w - 50
1050
>>> len(w)
1050
