Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = []
type(li)
<class 'list'>
tp = ()
tp
()
type(tp)
<class 'tuple'>
tp2 = tuple()
type(tp2)
<class 'tuple'>
num = 2.
type(num)
<class 'float'>
num = 2,
type(num)
<class 'tuple'>
t = (1,2,3,4,'sdf')
tt = 1,2,3,4.0, 434.345, 'dfd'
tt
(1, 2, 3, 4.0, 434.345, 'dfd')
tuple(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    tuple(1)
TypeError: 'int' object is not iterable
t
(1, 2, 3, 4, 'sdf')
isinstance(t, tuple)
True
isinstance(t. list)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    isinstance(t. list)
AttributeError: 'tuple' object has no attribute 'list'
isinstance(t, list)
False
t = 1
t1 = 1.,
t2 = 1,
print(t, t1, t2)
1 (1.0,) (1,)
n = (1,2,3,4,5)
type(n)
<class 'tuple'>
n[0]
1
n[-1]
5
n[1] =99
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    n[1] =99
TypeError: 'tuple' object does not support item assignment
liN = list(n)
lin[2] = 333
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    lin[2] = 333
NameError: name 'lin' is not defined. Did you mean: 'liN'?
liN[2] = 333
liN
[1, 2, 333, 4, 5]
n = tuple(liN)
n
(1, 2, 333, 4, 5)
n = (1,2,3,[1,2,3])
n[3]
[1, 2, 3]
n[3].append(666)
n
(1, 2, 3, [1, 2, 3, 666])
t = (1,23,4)
a,b,c = t
a
1
b
23
c
4
s = 'abc'
a,b,c = s
s
'abc'
a
'a'
b
'b'
c
'c'
t = (1,2,3,4,5,6,7)
a,b,c = t
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a,b,c = t
ValueError: too many values to unpack (expected 3)
a,b,*c = t
a
1
b
2
c
[3, 4, 5, 6, 7]
type(c)
<class 'list'>
*a,c,b = t
c
6
b
7
a
[1, 2, 3, 4, 5]
st = 'sdfdsfeewfe'
a,b,*c = st
a
's'
b
'd'
c
['f', 'd', 's', 'f', 'e', 'e', 'w', 'f', 'e']


def num():
    return 1,2,3,4

num()
(1, 2, 3, 4)
def num():
    return 'error:...',1,2,3,4

num()
('error:...', 1, 2, 3, 4)
err, *tp_n = num()
err
'error:...'
tp_n
[1, 2, 3, 4]
t
(1, 2, 3, 4, 5, 6, 7)
t[:]
(1, 2, 3, 4, 5, 6, 7)
aaa = t
aaa[1] = 999
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    aaa[1] = 999
TypeError: 'tuple' object does not support item assignment
t[1:]
(2, 3, 4, 5, 6, 7)
t[1:5]
(2, 3, 4, 5)
t[1:-2]
(2, 3, 4, 5)
t[::2]
(1, 3, 5, 7)
t[::-1]
(7, 6, 5, 4, 3, 2, 1)
t += 1
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    t += 1
TypeError: can only concatenate tuple (not "int") to tuple
t += 1,
t
(1, 2, 3, 4, 5, 6, 7, 1)
t*6
(1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 6, 7, 1)
5 in t
True
9999 in t
False
a
's'
a = 1
b = 'dswds'
c
['f', 'd', 's', 'f', 'e', 'e', 'w', 'f', 'e']
c = 23
a, b, c
(1, 'dswds', 23)
t = (1,23,4, a, b, c)
t
(1, 23, 4, 1, 'dswds', 23)
oId = (1,2,3,4,5,6,7)
oId +=(len(oId)+1,)
oId
(1, 2, 3, 4, 5, 6, 7, 8)
oId += len(oId)+1
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    oId += len(oId)+1
TypeError: can only concatenate tuple (not "int") to tuple
oId
(1, 2, 3, 4, 5, 6, 7, 8)
len(oId)
8
len(li)
0
len(t)
6
t
(1, 23, 4, 1, 'dswds', 23)
t[1:3]
(23, 4)
t = 155, + t[1:3] + 144,
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    t = 155, + t[1:3] + 144,
TypeError: bad operand type for unary +: 'tuple'
t = (155,) + t[1:3] + (144,)
t
(155, 23, 4, 144)
t.count(4)
1
del t[0]
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
del t
t
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    t
NameError: name 't' is not defined. Did you mean: 'tp'?
t = (4,3,2,1)
for val in t:
    if val*2 == 4:
        continue
    print(val)

    
4
3
1
for i in range(n):
    print(i,ArithmeticError ', val:', t[i])
    
SyntaxError: invalid syntax
for i in range(n):
    print(i, ', val:', t[i])

    
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    for i in range(n):
TypeError: 'tuple' object cannot be interpreted as an integer
n = 5
for i in range(n):
    print(i, ', val:', t[i])

    
0 , val: 4
1 , val: 3
2 , val: 2
3 , val: 1
Traceback (most recent call last):
  File "<pyshell#129>", line 2, in <module>
    print(i, ', val:', t[i])
IndexError: tuple index out of range




di = {}
type(di)
<class 'dict'>
d = dict()
type(d)
<class 'dict'>
d = {1:'val', 'sd':34455}
d
{1: 'val', 'sd': 34455}
hash
<built-in function hash>
a=3
b = 4.
c = 'efds'
li = [1,2,3]
se = {3,4,5,6}
type(se)
<class 'set'>
tp = (1,2,3)
hash(a)
3
hash(b)
4
hash(c)
-8701106726336618393
hash(li)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    hash(li)
TypeError: unhashable type: 'list'
hash(tp)
529344067295497451
hash(se)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    hash(se)
TypeError: unhashable type: 'set'


def a():
    pass

a
<function a at 0x0000020BB7909080>
hash(a)
140584225032
hash(d)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    hash(d)
TypeError: unhashable type: 'dict'
dd = {1:'a', 2.:'sdaf', 's':'dds', a:'func'}
dd
{1: 'a', 2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func'}
dd[1]
'a'
dd][2.]
SyntaxError: unmatched ']'
dd[2.]
'sdaf'
dd[3]
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    dd[3]
KeyError: 3
dd[a]
'func'

for k, v in dd.values():
    print (k, v)

    
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    for k, v in dd.values():
ValueError: not enough values to unpack (expected 2, got 1)

for v in dd.values():
    print (v)

    
a
sdaf
dds
func

for v in dd.keys():
    print (v)

    
1
2.0
s
<function a at 0x0000020BB7909080>

for v in dd.items():
    print (v)

    
(1, 'a')
(2.0, 'sdaf')
('s', 'dds')
(<function a at 0x0000020BB7909080>, 'func')

dd.get(1)
'a'
dd.get(1233)
dd[-4]
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    dd[-4]
KeyError: -4
dd[-4] = 'sdaasd'
dd
{1: 'a', 2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func', -4: 'sdaasd'}
dd[0] = 0
dd
{1: 'a', 2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func', -4: 'sdaasd', 0: 0}

for v in dd.items():
    print (v)
... 
...     
(1, 'a')
(2.0, 'sdaf')
('s', 'dds')
(<function a at 0x0000020BB7909080>, 'func')
(-4, 'sdaasd')
(0, 0)
>>> dd.keys()
dict_keys([1, 2.0, 's', <function a at 0x0000020BB7909080>, -4, 0])
>>> sorted(dd.keys())
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    sorted(dd.keys())
TypeError: '<' not supported between instances of 'str' and 'float'
>>> dd.update([55, '55555555'])
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    dd.update([55, '55555555'])
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dd.update((55, '55555555'))
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    dd.update((55, '55555555'))
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dd.update(55, '55555555')
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    dd.update(55, '55555555')
TypeError: update expected at most 1 argument, got 2
>>> dd.update({55, '55555555'})
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    dd.update({55, '55555555'})
ValueError: dictionary update sequence element #0 has length 8; 2 is required
>>> dd.update([55: '55555555'])
SyntaxError: invalid syntax
>>> dd.update({55: '55555555'})
>>> dd
{1: 'a', 2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func', -4: 'sdaasd', 0: 0, 55: '55555555'}
>>> dd.update({55: '55555555'})
>>> dd
{1: 'a', 2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func', -4: 'sdaasd', 0: 0, 55: '55555555'}
>>> len(dd)
7
>>> dd.pop(1)
'a'
>>> dd.popitem()
(55, '55555555')
>>> del dd[1221]
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    del dd[1221]
KeyError: 1221
>>> dd.pop(1)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    dd.pop(1)
KeyError: 1
>>> 
>>> dd
{2.0: 'sdaf', 's': 'dds', <function a at 0x0000020BB7909080>: 'func', -4: 'sdaasd', 0: 0}
>>> dd.keys()
dict_keys([2.0, 's', <function a at 0x0000020BB7909080>, -4, 0])
>>> di = {i:i**3 for i in range(50, 60)}
>>> di
{50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379}
>>> type(di)
<class 'dict'>
