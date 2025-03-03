Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print()

print(1,2,3)
1 2 3
def pront(val):
    for v in val:
        print(v, end=' ')
    print()

    
pront([1,2,3,4])
1 2 3 4 
pront(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pront(1,2,3,4,5)
TypeError: pront() takes 1 positional argument but 5 were given
def pront(*val):
    for v in val:
        print(v, end=' ')
    print()

    
pront([1,2,3,4])
[1, 2, 3, 4] 
pront(1,2,3,4,5)
1 2 3 4 5 
def pront(*val):
    print(type(val))
    for v in val:
        print(v, end=' ')
    print()

    
pront(1,2,3,4,5)
<class 'tuple'>
1 2 3 4 5 
pront(1,2,3,4,5, [1,2,34,], 'ssdwer')
<class 'tuple'>
1 2 3 4 5 [1, 2, 34] ssdwer 
def pront(*args):
    print(type(args))
    for v in args:
        print(v, end=' ')
    print()

    
pront(1,2,3,4,5, [1,2,34,], 'ssdwer')
<class 'tuple'>
1 2 3 4 5 [1, 2, 34] ssdwer 
def pront(*args):
    print(type(args))
    print(args)
    for v in args:
        print(v, end=' ')
    print()

    
pront(1,2,3,4,5, [1,2,34,], 'ssdwer')
<class 'tuple'>
(1, 2, 3, 4, 5, [1, 2, 34], 'ssdwer')
1 2 3 4 5 [1, 2, 34] ssdwer 
def pront(*args, sep1=' ', end1='\n'):
    for v in args:
        print(v, end=sep1)
    print(end=end1)

    
pront(1,2,3,4,5, [1,2,34,], 'ssdwer')
1 2 3 4 5 [1, 2, 34] ssdwer 


def bal(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in bal.items():
        print('\t', k, ':', v)

        
bal(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bal(1,2,3,4)
TypeError: bal() takes 0 positional arguments but 4 were given
bal(name='Vasia', cash=1200)
{'name': 'Vasia', 'cash': 1200}
<class 'dict'>
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    bal(name='Vasia', cash=1200)
  File "<pyshell#33>", line 4, in bal
    for k, v in bal.items():
AttributeError: 'function' object has no attribute 'items'
def bal(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print('\t', k, ':', v)

        
bal(name='Vasia', cash=1200)
{'name': 'Vasia', 'cash': 1200}
<class 'dict'>
	 name : Vasia
	 cash : 1200


def num(name='Joe', *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
num()
Joe
()
{}
def num(name='Joe', *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

    
num('Vasia', 1,2,3,4,54,'dssdwe', age=100, apples=99)
Vasia
(1, 2, 3, 4, 54, 'dssdwe')
{'age': 100, 'apples': 99}


def nums(*args):
    s = 0
    for i in args:
        s += i
    print(s)

    
def num(*args, **kwargs):
    print(args)
    print(kwargs)
    nums(args)

    
num(1,2,3,4,5)
(1, 2, 3, 4, 5)
{}
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    num(1,2,3,4,5)
  File "<pyshell#60>", line 4, in num
    nums(args)
  File "<pyshell#57>", line 4, in nums
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def nums(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)

    
def num(*args, **kwargs):
    print(args)
    print(kwargs)
    nums(args)

    
num(1,2,3,4,5)
(1, 2, 3, 4, 5)
{}
((1, 2, 3, 4, 5),)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    num(1,2,3,4,5)
  File "<pyshell#65>", line 4, in num
    nums(args)
  File "<pyshell#63>", line 5, in nums
    s += i
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
def num(*args, **kwargs):
    print(args)
    print(kwargs)
    nums(*args)

    
num(1,2,3,4,5)
(1, 2, 3, 4, 5)
{}
(1, 2, 3, 4, 5)
15
li1 = li2 = [1,2,3], [4,5,6]
li1
([1, 2, 3], [4, 5, 6])
li2
([1, 2, 3], [4, 5, 6])
li3= li1+li2
li3
([1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6])
st = 'dsswdwewewe'
li = [st]
li
['dsswdwewewe']
li = [*st]
li
['d', 's', 's', 'w', 'd', 'w', 'e', 'w', 'e', 'w', 'e']
d = {'1':2, '2':3}
d1 = {'11':22, '22':33}
di = {**d, **d1}
di
{'1': 2, '2': 3, '11': 22, '22': 33}
*t, = 'okhui'
t
['o', 'k', 'h', 'u', 'i']
*t = 'wewrwer'
SyntaxError: starred assignment target must be in a list or tuple
a, *t = 'kljhiughyuig'
a
'k'
t
['l', 'j', 'h', 'i', 'u', 'g', 'h', 'y', 'u', 'i', 'g']
*t, = 'klhiugyuyu'
t
['k', 'l', 'h', 'i', 'u', 'g', 'y', 'u', 'y', 'u']
# b**2 - 4*a*c
lambda: 2
<function <lambda> at 0x000001D3E01EAA20>
(lambda: 2)()
2
lambda a,b,c: a*b-c
<function <lambda> at 0x000001D3E01EA840>
(lambda a,b,c: a*b-c)
<function <lambda> at 0x000001D3E01E9940>
(lambda a,b,c: a*b-c)()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    (lambda a,b,c: a*b-c)()
TypeError: <lambda>() missing 3 required positional arguments: 'a', 'b', and 'c'
(lambda a,b,c: a*b-c)(2,3,4)
2
def c(z,x,y,b,a,c):
    return z+x+y + (lambda b, a, c: b**2 - 4*a*c)(b,a,c)

c(1,2,3,4,5,6)
-98


l = [2,3,4,6]
for i in l:
    print(i)

    
2
3
4
6
l_iter = iter(l)
l_iter
<list_iterator object at 0x000001D3E01DF310>
next(l_iter)
2
next(l_iter)
3
next(l_iter)
4
next(l_iter)
6
next(l_iter)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    next(l_iter)
StopIteration
st = 'sdadasd'
s_i = iter(st)
next(s_i)
's'
next(s_i)
'd'
next(s_i)
'a'
next(s_i)
'd'
next(s_i)
'a'
next(s_i)
's'
next(s_i)
'd'
next(s_i)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    next(s_i)
StopIteration
class Pow:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count <= self.n:
            res = 5 ** self.count
            self.count += 1
            return res
        raise StopIteration

    
p = Pw(15)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    p = Pw(15)
NameError: name 'Pw' is not defined. Did you mean: 'Pow'?
p
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    p
NameError: name 'p' is not defined
p = Pow(15)
p
<__main__.Pow object at 0x000001D3E01DDB20>
p_i = iter(p)
next(p_i)
1
next(p_i)
5
next(p_i)
25
next(p_i)
125
p = Pw(4)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    p = Pw(4)
NameError: name 'Pw' is not defined. Did you mean: 'Pow'?
class Pow:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.count = 0
        return self
    def __next__(self):
        if self.count <= self.n:
            res = 5 ** self.count
            self.count += 1
            return res
        raise StopIteration

    
p = Pow(4)
p_i = iter(p)
next(p_i)
1
next(p_i)
5
next(p_i)
25
next(p_i)
125
next(p_i)
625
next(p_i)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    next(p_i)
  File "<pyshell#150>", line 12, in __next__
    raise StopIteration
StopIteration
li = [i**2 for i in range(10)]
li
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
gen = (i**2 for i in range(10))
gen
<generator object <genexpr> at 0x000001D3E01B9080>
for v in gen:
    print(v)

    
0
1
4
9
16
25
36
49
64
81
for v in gen:
    print(v
          )

    
def ret(n):
    for i in range(n):
        return i

    
ret(5)
0
ret(5)
0
def ret(n):
    for i in range(n):
        yield i**2

        
r = ret(5)
r
<generator object ret at 0x000001D3E01B9CB0>
next(r)
0
next(r)
1
next(r)
4
next(r)
9
next(r)
16
next(r)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    next(r)
StopIteration
for i in ret(10):
    print(i)

    
0
1
4
9
16
25
36
49
64
81


def mul(n):
    return n * 5

li= [1,2,3,4]
res_li = map(mul, li)
res_li
<map object at 0x000001D3E01DFAC0>
li
[1, 2, 3, 4]


def a():
    x=10
    def i(n):
        return n**x
    return i

res = a()
res
<function a.<locals>.i at 0x000001D3E01E9300>
res(6)
60466176
def num():
    n = 0
    def inner():
        nonlocal n
        n **= 2
        return n
    return inner

res = num()
res
<function num.<locals>.inner at 0x000001D3E01E9A80>
res()
0
def num():
    n = 2
    def inner():
        nonlocal n
        n **= 2
        return n
    return inner

res = num()
res()
4
res()
16
res()
256
res()
65536
res()
4294967296
res()
18446744073709551616
res()
340282366920938463463374607431768211456
res()
115792089237316195423570985008687907853269984665640564039457584007913129639936
res()
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096
res()
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
res()
32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389437335543602135433229604645318478604952148193555853611059596230656
>>> class Dog:
...     pass
... d = Dog()
SyntaxError: invalid syntax
>>> d = Dog()
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    d = Dog()
NameError: name 'Dog' is not defined
>>> class Dog:
...     pass
... 
>>> d = Dog()
>>> type(d)
<class '__main__.Dog'>
>>> isinstance(d, Dog)
True
>>> list.__bases__
(<class 'object'>,)
>>> isinstance(list, type)
True
>>> d = Dog()
>>> isinstance(type, type)
True
>>> 
>>> class Number:
...     Num = 99
...     def get_number(self):
...         return 55
... 
...     
>>> n = Number()
>>> n.Num
99
>>> n.get_number()
55
>>> 
>>> def get_number(self):
...         return 55
... 
...     
>>> NumberFromType = type('NumberFromType', (object,), {'get_number':get_number, 'Num':99, 'name':'JOJO'})
>>> NumberFromType
<class '__main__.NumberFromType'>
>>> nn = NumberFromType()
>>> type(nn)
<class '__main__.NumberFromType'>
>>> nn.name
'JOJO'
>>> nn.get_number()
55
>>> 
>>> name = input()
Car
>>> name
'Car'
>>> di = {'VIN':12345, 'Model':'Sedan'}
>>> new_type = type(name, (object,), di)
>>> new_type
<class '__main__.Car'>
>>> my-car = new_type()
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> my_car = new_type()
>>> my_car.Model
'Sedan'
>>> my_car.VIN
12345
