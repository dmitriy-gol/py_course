# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# print
# <built-in function print>
# import time
# time.sleep(0)
# import this
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
#
#
# n = 10
# users = []
# user_a_password = input('pass:')
# pass:12345
# user_a_name = input('name:')
# name:Vasia
# users.append([user_a_name, user_a_password],)
# users
# [['Vasia', '12345']]
#
# def reg():
#     user_a_name = input('name:')
#     user_a_password = input('pass:')
#     users.append([user_a_name, user_a_password],)
#     print('Done...')
#
#
# reg()
# name:kolia
# pass:321
# Done...
# users
# [['Vasia', '12345'], ['kolia', '321']]
# n = 8
# for i in range(n):
#     register()
#
#
# Traceback (most recent call last):
#   File "<pyshell#24>", line 2, in <module>
#     register()
# NameError: name 'register' is not defined
# for i in range(n):
#     reg()
#
#
# name:sdf
# pass:213
# Done...
# name:serf
# pass:234
# Done...
# name:erws
# pass:324
# Done...
# name:dsfgdrygd
# pass:345
# Done...
# name:dfgd
# pass:345
# Done...
# name:dfgdr
# pass:3453
# Done...
# name:fdyhdfty
# pass:435
# Done...
# name:drfgr
# pass:2312312
# Done...
# users
# [['Vasia', '12345'], ['kolia', '321'], ['sdf', '213'], ['serf', '234'], ['erws', '324'], ['dsfgdrygd', '345'], ['dfgd', '345'], ['dfgdr', '3453'], ['fdyhdfty', '435'], ['drfgr', '2312312']]
#
#
# def hell():
#     print('Hello')
#
#
# hell()
# Hello
#
# def hello():
#     user = input('name:')
#     print(f'Hello, {user}!')
#
#
# hello()
# name:weqreqwr
# Hello, weqreqwr!
#
#
# def hello():
#     user = input('name:')
#     print(f'Hello, {user}!')
#     for i in range(3):
#         print(i, end=' ')
#         d = 88
#         if d == 88:
#             print(11111111)
#         print(2347568)
#
#
# hello()
# name:sadiuh
# Hello, sadiuh!
# 0 11111111
# 2347568
# 1 11111111
# 2347568
# 2 11111111
# 2347568
#
#
# def hello():
#     user = input('name:')
#     print(f'Hello, {user}!')
#     for i in range(3):
#         print(i, end=' ')
#         d = 88
#         if d == 88:
#             print(11111111)
#         print(2347568)
#
#
# hello()
# name:easfasewr
# Hello, easfasewr!
# 0 11111111
# 2347568
# 1 11111111
# 2347568
# 2 11111111
# 2347568
#
#
# def hello():
#     user = input('name:')
#     print(f'Hello, {user}!')
#     for i in range(3):
#         print(i, end=' ')
#     d = 88
#     if d == 88:
#         print(11111111)
#     print(2347568)
#
#
# hello()
# name:esfrser
# Hello, esfrser!
# 0 1 2 11111111
# 2347568
# gogo()
# Traceback (most recent call last):
#   File "<pyshell#63>", line 1, in <module>
#     gogo()
# NameError: name 'gogo' is not defined
# hello = 55
# heloo()
# Traceback (most recent call last):
#   File "<pyshell#65>", line 1, in <module>
#     heloo()
# NameError: name 'heloo' is not defined. Did you mean: 'hello'?
# hello()
# Traceback (most recent call last):
#   File "<pyshell#66>", line 1, in <module>
#     hello()
# TypeError: 'int' object is not callable
# print(hello)
# 55
# def h():
#     pass
#
# h()
# h(1,2,3)
# Traceback (most recent call last):
#   File "<pyshell#72>", line 1, in <module>
#     h(1,2,3)
# TypeError: h() takes 0 positional arguments but 3 were given
#
#
# def hello(user):
#     print('hello', user)
#
#
# hello()
# Traceback (most recent call last):
#   File "<pyshell#78>", line 1, in <module>
#     hello()
# TypeError: hello() missing 1 required positional argument: 'user'
# hello(1)
# hello 1
# hello (1,2)
# Traceback (most recent call last):
#   File "<pyshell#80>", line 1, in <module>
#     hello (1,2)
# TypeError: hello() takes 1 positional argument but 2 were given
#
#
# def hello(a, b, c):
#     print('Hello,', a, b, c)
#
#
# hello(b = 44, c = 88, a = 99)
# Hello, 99 44 88
# hello(33, b = 44, c = 88)
# Hello, 33 44 88
# hello(33, c = 88, b = 44)
# Hello, 33 44 88
# hello(c = 88, b = 44, 66)
# SyntaxError: positional argument follows keyword argument
#
#
# def hello(a, b, c, d):
#     print('Hello,', a, b, c, d)
#
#
# hello(1,2,3,4)
# Hello, 1 2 3 4
# hello(1,2, c=55, d=897)
# Hello, 1 2 55 897
#
#
# def hello(name, age):
#     print('Hello,', name, age)
#
#
# hello('dddd', 28)
# Hello, dddd 28
# hello(28, 'dddd')
# Hello, 28 dddd
# hello(age=28, name='dddd')
# Hello, dddd 28
#
#
# def order(name, ph, age, msg):
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#
#
# order('dwd', 123)
# Traceback (most recent call last):
#   File "<pyshell#117>", line 1, in <module>
#     order('dwd', 123)
# TypeError: order() missing 2 required positional arguments: 'age' and 'msg'
# def order(name, ph, age='', msg=''):
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#
#
# order('gggg', 123)
# Order 344: created.
# Order details:
#   Name: gggg
#   Phone: 123
#   Age:
#   Message:
#
# order('gggg')
# Traceback (most recent call last):
#   File "<pyshell#121>", line 1, in <module>
#     order('gggg')
# TypeError: order() missing 1 required positional argument: 'ph'
# order('gggg', 123453345)
# Order 344: created.
# Order details:
#   Name: gggg
#   Phone: 123453345
#   Age:
#   Message:
#
#
#
# def a(name='John', age=123)
# SyntaxError: expected ':'
# def a(name='John', age=123):
#     print(name, age)
#
#
# a()
# John 123
# a('Natasha')
# Natasha 123
#
#
# name = input('->')
# ->1213243
# name
# '1213243'
#
#
# defh():
#
# SyntaxError: invalid syntax
# def h():
#     pass
#
# res = h()
# print(res)
# None
#
#
# def h():
#     print(1*44)
#
#
# res = h()
# 44
# print(res)
# None
#
#
# def order(name, ph, age='', msg=''):
#     if len(name) <2:
#         return False
#     if !str(ph).isalnum():
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#
# SyntaxError: invalid syntax
# def order(name, ph, age='', msg=''):
#     if len(name) <2:
#         return False
#     if str(ph).isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#
#
# res = order('', 123)
# res = order('dddd', 123)
# Order 344: created.
# Order details:
#   Name: dddd
#   Phone: 123
#   Age:
#   Message:
#
# res
#
#
# def order(name, ph, age='', msg=''):
#     if len(name) <2:
#         return False
#     if str(ph).isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#     return True
#
# res = order('', 123
#
#             )
# res
# False
# res = order('dddd', 123)
# Order 344: created.
# Order details:
#   Name: dddd
#   Phone: 123
#   Age:
#   Message:
#
# res
# True
#
#
# def order(name, ph, age='', msg=''):
#     if len(name) <2 or if str(ph).isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#     return True
# SyntaxError: invalid syntax
# def order(name, ph, age='', msg=''):
#     if len(name) <2 or ph.isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#     return True
#
#
# res = order('dddd', 123)
# Traceback (most recent call last):
#   File "<pyshell#175>", line 1, in <module>
#     res = order('dddd', 123)
#   File "<pyshell#173>", line 2, in order
#     if len(name) <2 or ph.isalnum() != True:
# AttributeError: 'int' object has no attribute 'isalnum'
#
#
# def order(name, ph, age='', msg=''):
#     if (len(name) <2) or ph.isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#     return True
#
# res = order('dddd', 123)
# Traceback (most recent call last):
#   File "<pyshell#180>", line 1, in <module>
#     res = order('dddd', 123)
#   File "<pyshell#179>", line 2, in order
#     if (len(name) <2) or ph.isalnum() != True:
# AttributeError: 'int' object has no attribute 'isalnum'
#
#
# res = order('dddd', '123')
# Order 344: created.
# Order details:
#   Name: dddd
#   Phone: 123
#   Age:
#   Message:
#
#
#
# def up(name):
#     print(name.upper())
#
#
# up('dIma')
# DIMA
#
#
# def up(name):
#     return name.upper()
#
# name = up('dimA')
# name
# 'DIMA'
# help(print)
# Help on built-in function print in module builtins:
#
# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
#
#     sep
#       string inserted between values, default a space.
#     end
#       string appended after the last value, default a newline.
#     file
#       a file-like object (stream); defaults to the current sys.stdout.
#     flush
#       whether to forcibly flush the stream.
#
#
#
# def order(name, ph, age='', msg=''):
#     """
#     Функция которая делает тото.
#
#     Параметры:
#     name -> строка, обязательно
#     ph -> строка, обязательно
#     age='' -> строка, необязательно
#     msg='' -> строка, необязательно
#
#     Ретарны:
#     bool True or False
#     """
#
#     if (len(name) <2) or ph.isalnum() != True:
#         return False
#
#     print('Order 344: created.')
#     print('Order details:')
#     print(f'  Name: {name}')
#     print(f'  Phone: {ph}')
#     print(f'  Age: {age}')
#     print(f'  Message: {msg}')
#     print()
#     return True
#
# help(order)
# Help on function order in module __main__:
#
# order(name, ph, age='', msg='')
#     Функция которая делает тото.
#
#     Параметры:
#     name -> строка, обязательно
#     ph -> строка, обязательно
#     age='' -> строка, необязательно
#     msg='' -> строка, необязательно
#
#     Ретарны:
#     bool True or False
#
# order.__doc__
# "\n    Функция которая делает тото.\n\n    Параметры:\n    name -> строка, обязательно\n    ph -> строка, обязательно\n    age='' -> строка, необязательно\n    msg='' -> строка, необязательно\n\n    Ретарны:\n    bool True or False\n    "
#
#
# def a():
#     print(1)
#
#
# def b():
#     print(2)
#
#
# def c():
#     print(3)
#
#
# c()
# 3
# del c
# c()
# Traceback (most recent call last):
#   File "<pyshell#216>", line 1, in <module>
#     c()
# NameError: name 'c' is not defined
# b()
# 2
# qwe = b
# b()
# 2
# qwe()
# 2
# del b
# b()
# Traceback (most recent call last):
#   File "<pyshell#222>", line 1, in <module>
#     b()
# NameError: name 'b' is not defined
# qwe()
# 2
# a()
# 1
# id(a)
# 2671930590208
# ss = a
# id(ss)
# 2671930590208
# del a
# ss()
# 1
#
#
# def numbers(num):
#     if num % 2 == 0:
#         return True
#     return None
# numbers(2)
# SyntaxError: invalid syntax
# numbers(2)
# Traceback (most recent call last):
#   File "<pyshell#237>", line 1, in <module>
#     numbers(2)
# NameError: name 'numbers' is not defined. Did you forget to import 'numbers'?
# def num(n):
#     if n % 2 == 0:
#         return True
#     return None
# num(2)
# SyntaxError: invalid syntax
# print(num(3))
# Traceback (most recent call last):
#   File "<pyshell#240>", line 1, in <module>
#     print(num(3))
# NameError: name 'num' is not defined. Did you mean: 'sum'?
#
#
# def numbers(num):
#     return num % 2 == 0
#
# print(numbers(2))
# True
# print(numbers(3))
# False
# a = 10
# s = 'dswe'
# a
# 10
# s
# 'dswe'
# isinstance(a, int)
# True
# isinstance(a, str)
# False
#
# if isinstance(a, int):
#     print('INT')
# elif isinstance(a, str):
#     print('STR')
#
#
# INT
# isinstance(a, (int, float, str))
# True
# a = 'ddd'
# isinstance(a, (int, float, str))
# True
#
#
# def check(a):
#     if isinstance(a, int):
#     print('INT')
# elif isinstance(a, str):
#     print('STR')
#
# SyntaxError: expected an indented block after 'if' statement on line 2
#
#
# def check(a):
#     if isinstance(a, int):
#         print('INT')
#     elif isinstance(a, str):
#         print('STR')
#
#
# check(12)
# INT
# check('dd')
# STR
#
#
# total = 0
#
#
# def add(n):
#     total = total + n
#
#
# add(5)
# Traceback (most recent call last):
#   File "<pyshell#282>", line 1, in <module>
#     add(5)
#   File "<pyshell#281>", line 2, in add
#     total = total + n
# UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
# print(total)
# 0
# x = 2183
# def add(x):
#     print('in:', x, id(x)
#     x += 888
#
# SyntaxError: '(' was never closed
# def add(x):
#     print('in:', x, id(x))
#     x += 888
#     print('in:', x, id(x))
#
#
# x
# 2183
# add(x)
# in: 2183 2671924573648
# in: 3071 2671924574032
#
# def add(num):
#     print('in:', num, id(num))
#     num += 888
#     print('in:', num, id(num))
#
#
# x
# 2183
# add(2)
# in: 2 140728132561368
# in: 890 2671924574064
# add(x)
# in: 2183 2671924573648
# in: 3071 2671924573904
# number = 2183
# number = 2183
# def add():
#     global number
#     print('in:', number, id(number))
#     number += 888
#     print('in:', number, id(number))
#
#
# add()
# in: 2183 2671924574064
# in: 3071 2671924573072
# >>> number
# 3071
# >>>
# >>>
# >>> def a():
# ...     print(1)
# ...
# ...
# ... def b():
# ...     print(2)
# ...
# ...
# ... def c():
# ...     print(3)
# ...
# SyntaxError: invalid syntax
# >>> def a():
# ...     print(1)
# ...
# ...
# >>> def b():
# ...     print(2)
# ...
# ...
# >>> def c():
# ...     print(3)
# ...
# ...
# >>> li = [a,b,c]
# >>> li
# [<function a at 0x0000026E1B7A1620>, <function b at 0x0000026E1B7A16C0>, <function c at 0x0000026E1B7A1760>]
# >>> for i in li:
# ...     i()
# ...
# ...
# 1
# 2
# 3
# >>>
# >>>
# >>> def no(num):
# ...     if num > 20:
# ...         return True
# ...     return num + no(num+4)
# ...
# >>> no(1)
# 46
# >>> no(5)
# 45
# >>> import sys
# >>> sys.getrecursionlimit()
# 1000
# >>> print(factorial(1000))
# Traceback (most recent call last):
#   File "<pyshell#330>", line 1, in <module>
#     print(factorial(1000))
# NameError: name 'factorial' is not defined
# >>> sys.setrecursionlimit(2000)
# >>> f1 = f2 = 1
# >>> f1, f2 = f2, f1+f2
# >>> f1
# 1
# >>> f2
# 2
# >>> for i in range(10):
# ...     f1, f2 = f2, f1+f2
# ...
# ...
# >>> f2
# 233
# >>> f1
# 144
