Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Dog:
    pass

class Wallet:
    pass

class Car:
    pass

class User
SyntaxError: expected ':'
class User:
    pass

d = Dog()
type(d)
<class '__main__.Dog'>
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
d = Dog()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = Dog()
TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'age'
d = Dog('bobik', 34)
class User:
    def __init__(self, name, emil):
        self.name = name
        
        self.email = email

        
dima = User('Dima', 'dima@mail.com')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dima = User('Dima', 'dima@mail.com')
  File "<pyshell#23>", line 5, in __init__
    self.email = email
NameError: name 'email' is not defined. Did you mean: 'emil'? Or did you forget to import 'email'?
class User:
    def __init__(self, name, email):
        self.name = name
        
        self.email = email

        
dima = User('Dima', 'dima@mail.com')
type(dima)
<class '__main__.User'>
type(d)
<class '__main__.Dog'>
isinstance(dima, User)
True
isinstance(dima, Dog)
False
dima.name
'Dima'
dima.email
'dima@mail.com'
d.age
34
d.name
'bobik'

vova = User('Vova', 'vova@mail.com)
            
SyntaxError: unterminated string literal (detected at line 1)
vova = User('Vova', 'vova@mail.com')
            
vava.name
            
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    vava.name
NameError: name 'vava' is not defined. Did you mean: 'vova'?
class User:
    def __init__(self, name, email):
        self.name = name
        
        self.email = email

        
vova = User('Vova', 'vova@mail.com)
            
SyntaxError: unterminated string literal (detected at line 1)
vova = User('Vova', 'vova@mail.com')
            
dima = User('Dima', 'dima@mail.com')
            
vova.name
            
'Vova'
dima.name
            
'Dima'
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
User.users_counter =6
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
User.users_counter
0
dima = User('d', 's')
User.users_counter
1
vi = User('Vi', 's')
User.users_counter
2
vi.name
'Vi'
vi.users_counter
2
dima.users_counter
2
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.users_counter = 1

        
User.users_counter
0
d = User('Di', '@')
d.users_counter
1
User.users_counter
0
class User:
    users_counter = 0
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.users_counter += 1

        
d = User('Di', '@')
vi = User('Vi', 's')
c = User('Ci', 'dffed')
User.users_counter
3
c.users_counter = 555
d.users_counter
3
c.users_counter
555
d.mobile = '332542566'
d.name
'Di'
d.mobile
'332542566'
c.mobile
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    c.mobile
AttributeError: 'User' object has no attribute 'mobile'
User.jojo = 9999
User.jojo
9999
d.jojo
9999
class Wallet:
    """представляет структуру полей для описания кошелька."""
    counter = 0
    def __init__(self, owner, currency, amount, address='', color='silver'):
        self.owner = owner
        self.currency = currency
        self.amount = amount
        self.address = address
        self.color = color
        Wallet.counter += 1
        self.wallet_id = Wallet.counter * 10

        
Wallet.counter
0
fw = Wallet('s f', 'byn', 1000)
Wallet.counter
1
fw.owner
's f'
fw.address
''
fw.wallet_id
10
fw.color
'silver'
sw = Wallet('D F', 'RUB', 10000, color='gold')
sw.color
'gold'
sw.amount
10000
sw.wallet_id
20
Wallet.__doc__
'представляет структуру полей для описания кошелька.'
Wallet.__name__
'Wallet'
Wallet.__module__
'__main__'
Wallet.__bases__
(<class 'object'>,)
fw.__dict__
{'owner': 's f', 'currency': 'byn', 'amount': 1000, 'address': '', 'color': 'silver', 'wallet_id': 10}
sw.__dict__
{'owner': 'D F', 'currency': 'RUB', 'amount': 10000, 'address': '', 'color': 'gold', 'wallet_id': 20}
for k, v in fw.__dict__.items():
    print(k, ':', v)

    
owner : s f
currency : byn
amount : 1000
address : 
color : silver
wallet_id : 10


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')

        
d1 = User('Dima', '@')
d1.name
'Dima'
d1.hello
<bound method User.hello of <__main__.User object at 0x000002543F32EAB0>>
d1.hello('hello')
Dima says hello!
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye bye!')

        
d1 = User('Dima', '@')
d1.hello('hello')
Dima says hello!
d1.bye()
Dima says bye bye!
st = 'hello'
print(st)
hello
print(d1)
<__main__.User object at 0x000002543F32EC30>
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye bye!')
    def __str__(self):
        return f'User: name-{self.name}, email-{self.email}'

    
k = User('Kate', 'k@gmail.com')
k.bye()
Kate says bye bye!
print(k)
User: name-Kate, email-k@gmail.com
dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
dir(User)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bye', 'hello']
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye bye!')
    def __str__(self):
        return f'User: name-{self.name}, email-{self.email}'

    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({counter_id:user})
    def show_all(self):
        for k, v in self.storage.items():
            print(f'User id:{k}')
            print(f'   Name:{user.name}')
            print(f'   Email:{user.email}')
            print('__str__')
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User('Dima', '@')
kate = User('Kate', 'wd')
vasia = User('Vasia', 'wdwdw')
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for k, v in self.storage.items():
            print(f'User id:{k}')
            print(f'   Name:{user.name}')
            print(f'   Email:{user.email}')
            print('__str__')
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User('Dima', '@')
kate = User('Kate', 'wd')
vasia = User('Vasia', 'wdwdw')
SyntaxError: multiple statements found while compiling a single statement
strg = Storage()
dima = User('Dima', '@')
kate = User('Kate', 'wd')
vasia = User('Vasia', 'wdwdw')
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
User id:1
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    strg.show_all()
  File "<pyshell#167>", line 11, in show_all
    print(f'   Name:{user.name}')
NameError: name 'user' is not defined. Did you mean: 'User'?
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def hello(self, message):
        print(f'{self.name} says {message}!')
    def bye(self):
        print(f'{self.name} says bye bye!')
    def __str__(self):
        return f'User: name-{self.name}, email-{self.email}'

    
class Storage:
    counter_id = 0
    def __init__(self):
        self.storage = {}
    def add_user(self, user):
        Storage.counter_id += 1
        self.storage.update({Storage.counter_id:user})
    def show_all(self):
        for k, v in self.storage.items():
            print(f'User id:{k}')
            print(f'   Name:{user.name}')
            print(f'   Email:{user.email}')
            print('__str__')
            print(user)
            print(user.bye())

            
strg = Storage()
dima = User('Dima', '@')
kate = User('Kate', 'wd')
vasia = User('Vasia', 'wdwdw')
strg.add_user(dima)
strg.add_user(kate)
strg.add_user(vasia)
strg.show_all()
User id:1
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    strg.show_all()
  File "<pyshell#181>", line 11, in show_all
    print(f'   Name:{user.name}')
NameError: name 'user' is not defined. Did you mean: 'User'?
dima.name
'Dima'
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__ (self):
        return 'Привет из род класса')
    
SyntaxError: unmatched ')'
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__ (self):
        return 'Привет из род класса'

    
class Sedan:
    pass

class Wagon:
    pass
Swdan.__bases__
SyntaxError: invalid syntax
Sedan.__bases__
(<class 'object'>,)
class Wagon(Car):
    pass

class Sedan(Car):
    pass

Sedan.__bases__
(<class '__main__.Car'>,)
s = Sedan('123244', 1.7, 'asfdas')
print(s)
Привет из род класса
isinstance(s, Sedan)
True
isinstance(s, Car)
True
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__ (self):
        return 'Привет из род класса'
    def drive(self):
        print('ппппппппп')

        
class Wagon(Car):
    pass

class Sedan(Car):
    pass

w = Wagon(123123, 1.9, '324234')
w.__dict__
{'vin': 123123, 'volume': 1.9, 'model_name': '324234'}
w.drive()
ппппппппп
class Sedan(Car):
    def drive(self):
        print('Седан')

        
s = Sedan(1235346, 2.0, 'awsdwedqwrfe')
s.drive()
Седан


class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__ (self):
        return 'Привет из род класса'
    def drive(self):
        print('ппппппппп')

        
class Wagon(Car):
    pass

class Sedan(Car):
    def drive(self):
        super().drive()
        print('Седан')

        
w = Wagon(121`32, 23, '23323')
SyntaxError: invalid syntax
w = Wagon(123123, 1.9, '324234')
s = Sedan(123123, 34, '23235')
w.drive()
ппппппппп
s.drive()
ппппппппп
Седан
class Car:
    def __init__(self, vin, volume, model_name):
        self.vin = vin
        self.volume = volume
        self.model_name = model_name
    def __str__ (self):
        return 'Привет из род класса'
    def drive(self):
        print('ппппппппп')
    def show_car(self):
        print(self.vin, self,volume, self.model_name)

        
class Sedan(Car):
    def __init__(self):
        self.body_type = 'Sedan'
        super().__init__(vin, volume, model_name)
    def drive(self):
        super().drive()
        print('RRRRRRRR')

        
s = Sedan(123123, 34, '23235')
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    s = Sedan(123123, 34, '23235')
TypeError: Sedan.__init__() takes 1 positional argument but 4 were given
class Sedan(Car):
    def __init__(self, vin, volume, model_name):
        self.body_type = 'Sedan'
        super().__init__(vin, volume, model_name)
    def drive(self):
        super().drive()
        print('RRRRRRRR')

        
s = Sedan(123123, 34, '23235')
s.vin
123123
s.show_car()
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    s.show_car()
  File "<pyshell#257>", line 11, in show_car
    print(self.vin, self,volume, self.model_name)
NameError: name 'volume' is not defined. Did you mean: 'self.volume'?
s.volume
34
print(s)
Привет из род класса
>>> class Wallet:
...     def __init__(self, money):
...         self.money = money
... 
...         
>>> w = Wallet(123456)
>>> wall.money = -12345
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    wall.money = -12345
NameError: name 'wall' is not defined. Did you mean: 'all'?
>>> w.money = -1122
>>> w.money
-1122
>>> class Wallet:
...     def __init__(self, money):
...         self.__money = money
... 
...         
>>> w = Wallet(123456)
>>> w.money
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    w.money
AttributeError: 'Wallet' object has no attribute 'money'
>>> w.money = -12122
>>> class Wallet:
...     def __init__(self, money):
...         self.__money = money
...     def read(self, secret):
...         if secret == 123:
...             return self.__money
...         return 'asdfasedfawed'
...     def add(self, amount, secret):
...         if secret != 123:
...             self.__money += amount
...         return 'unnnnnn'
... 
...     
>>> w = wallet(100)
Traceback (most recent call last):
  File "<pyshell#296>", line 1, in <module>
    w = wallet(100)
NameError: name 'wallet' is not defined. Did you mean: 'Wallet'?
>>> w = Wallet(100)
>>> w.money
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    w.money
AttributeError: 'Wallet' object has no attribute 'money'
>>> w.__money
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    w.__money
AttributeError: 'Wallet' object has no attribute '__money'
>>> w.read(321)
'asdfasedfawed'
>>> w.add(100, 123)
'unnnnnn'
>>> w.read(123)
100
>>> w.add(100, 124)
'unnnnnn'
>>> w.read(123)
200
>>> w.read(1)
'asdfasedfawed'
>>> def f():
...     pass
... 
>>> x=f()
>>> print(x)
None
