Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class User:
    __counter = 0
    def __init__(self, name):
        self.name = naim
        User.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'

    
User.get_counter()
0
k = User('Kate')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    k = User('Kate')
  File "<pyshell#10>", line 4, in __init__
    self.name = naim
NameError: name 'naim' is not defined
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'

    
k = User('Kate')
print(k)
user name: Kate.
k.get_counter
<bound method User.get_counter of <class '__main__.User'>>
k.get_counter()
1

class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
    @classmethod
    def set_counter(cls, val):
        cls.__counter = val
        return cls.__counter
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'

    
k = User('Kate')
print(k
      )
user name: Kate.
User.set_counter(55)
55
k.se_counter()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    k.se_counter()
AttributeError: 'User' object has no attribute 'se_counter'. Did you mean: 'set_counter'?
k.set_counter()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    k.set_counter()
TypeError: User.set_counter() missing 1 required positional argument: 'val'
k.get_counter()
55
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def set_counter(cls, val):
        cls.__counter = val
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'

    
class User:
    __counter = 0
    def __init__(self, name):
        self.name = name
        User.__counter += 1
        
    @classmethod
    def set_counter(cls, val):
        cls.__counter = val
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'
    @staticmethod
    def chek(name):
        return False if len(name) < 2 else True

    
u = 'kate'
if User.chek(u):
    i = User(u)
else:
    print('имя короткое')

    
print(i)
user name: kate.
u1 = 'J'
if User.chek(u1):
    i = User(u1)
else:
    print('имя короткое')

    
имя короткое

class User:
    __counter = 0
    def __init__(self, name):
        print('__init__')
        self.name = name
        User.__counter += 1
        
    @classmethod
    def init_age(cls, name, age):
        print('alt__init__')
        user = cls(name)
        user.age = age
        return user
    def set_counter(cls, val):
        cls.__counter = val
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'
    @staticmethod
    def chek(name):
        return False if len(name) < 2 else True

    

u1 = User('Vova')
__init__
u2 = User.init_age('Vova', 19)
alt__init__
__init__
Usre.get_counter()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    Usre.get_counter()
NameError: name 'Usre' is not defined
User.get_counter()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    User.get_counter()
TypeError: User.get_counter() missing 1 required positional argument: 'cls'
u1
<__main__.User object at 0x000001593BDFE4B0>
print(u2)
user name: Vova.
u2.age
19
class User:
    __counter = 0
    def __init__(self, name):
        print('__init__')
        self.name = name
        User.__counter += 1
        
    @classmethod
    def init_age(cls, name, age):
        print('alt__init__')
        user = cls(name)
        user.age = age
        return user
    @classmethod
    def set_counter(cls, val):
        cls.__counter = val
    @classmethod    
    def get_counter(cls):
        return cls.__counter
    def __str__(self):
        return f'user name: {self.name}.'

    
u1 = User('Vova')
__init__
u2 = User.init_age('Vova', 19)
alt__init__
__init__
User.get_counter()
2


class A:
    pass

class B:
    pass

class C:
    pass

C.__mro__
(<class '__main__.C'>, <class 'object'>)
class A:
    pass

class B(A):
    pass

class C(B):
    pass

C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
class A:
    a = 10

    
class B(A):
    b = 100

    
class C(B):
    c = 1000

    
c1 = C()
c1.c
1000
c1.b
100
c1.a
10
c1.d
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    c1.d
AttributeError: 'C' object has no attribute 'd'
class A:
    a = 10
    def __init__(self):
        aaa = 11

        
class C(A):
    c = 1000
    def __init__(self):
        self.ccc = 1111
        super().__init__()

        
class A:
    a = 10
    def __init__(self):
        self.aaa = 11

        
class b(A):
    b = 100
    def __init__(self):
        self.bbb = 111

        
class B(A):
    b = 100
    def __init__(self):
        self.bbb = 111

        
class C(B):
    c = 1000
    def __init__(self):
        self.ccc = 111
        super().__init__()

        
C1.ccc
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    C1.ccc
NameError: name 'C1' is not defined. Did you mean: 'c1'?
c1.ccc
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    c1.ccc
AttributeError: 'C' object has no attribute 'ccc'
c1 = C()
c1.ccc
111
c1.bbb
111
c1.aaa
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    c1.aaa
AttributeError: 'C' object has no attribute 'aaa'

try:
    raise AttributeError
except:
    print('err')
else:
    print('ok')
finally:
    print('fin')

    
err
fin
try:
    1+1
except:
    print('err')
else:
    print('ok')
finally:
    print('fin')

    
2
ok
fin
def a(number):
    try:
        return number
    except:
        return number +1
    else:
        return number +2
    finally:
        return number ** 10

    
a(10)
10000000000
>>> def a(number):
...     try:
...         return number
...     except:
...         return number +1
...     else:
...         return number +2
... 
...     
>>> a(10)
10
>>> class User:
...     def __init__(self, name):
...         self.name = name
...         
...     
...     def __str__(self):
...         return f'user name: {self.name}.'
...     def call(self, number):
...         if len(number) < 8:
...             pass
...         return f'звоню {number}'
... 
...     
>>> class Number(Exception):
...     def __init__(self, namber, mes):
...         self.namber = namber
...         self.mes = mes
... 
...         
>>> raise Number(12311, 'uihgyuftyfrty')
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    raise Number(12311, 'uihgyuftyfrty')
Number: (12311, 'uihgyuftyfrty')
>>> class Number(Exception):
...     def __init__(self, namber, mes):
...         self.namber = namber
...         self.mes = mes
... 
...         
>>> class User:
...     def __init__(self, name):
...         self.name = name
...         
...     
...     def __str__(self):
...         return f'user name: {self.name}.'
...     def call(self, number):
...         if len(number) < 8:
...             pass
...         return f'звоню {number}'
... 
...     
>>> u = User('Vasia')
>>> u.call(1234)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    u.call(1234)
  File "<pyshell#156>", line 9, in call
    if len(number) < 8:
TypeError: object of type 'int' has no len()
>>> u.call('1234')
'звоню 1234'
>>> try:
...     u.call('1234')
... except Number as e:
...     print(e)
... except:
...     print(-1)
... 
...     
'звоню 1234'
