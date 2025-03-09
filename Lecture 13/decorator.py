Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(a, b):
...     return a+b
... 
>>> def add(a, b):
...     print('sdad')
...     return a+b**2
... 
>>> def add(a, b):
...     return a+b
... 
>>> def decorator(func):
...     def inner(ia, ib):
...         print('sdad')
...         ib **= 2
...         func(ia, ib)
...     return inner
... 
>>> add(2,3)
5
>>> @decorator
... def add(a, b):
...     return a+b
... 
>>> add(2,3)
sdad
>>> res = add(2,3)
sdad
>>> res
>>> @decorator
... def add(a, b):
...     print(a+b)
... 
...     
>>> add(2,3)
sdad
11
>>> 
>>> 
>>> def decorator(func):
...         print('Привет из декоратора')
...         func()
... 
...         
>>> def say():
...     print('как дела')
... 
...     
>>> say()
как дела
>>> @decorator
... def say():
...     print('как дела')
... 
...     
Привет из декоратора
как дела
>>> say()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    say()
TypeError: 'NoneType' object is not callable
>>> def decorator(func):
...     def inner():
...         print('Привет из декоратора')
...         func()
...     return inner
... 
>>> @decorator
... def say():
...     print('как дела')

    
say()
Привет из декоратора
как дела
say()
Привет из декоратора
как дела
def decorator(func):
    print('Привет из декоратора')
    return func

@decorator
def say():
    print('как дела')

    
Привет из декоратора
say()
как дела
say()
как дела
def decorator(func):
    def inner():
        print('Привет из декоратора')
        func()
    return inner

@decorator
def say():
    print('как дела')

    
say()
Привет из декоратора
как дела
def say(n):
    print(f'{n} как дела?')

    
def decorator(func):
    def inner(dn):
        print('Привет из декоратора')
        func(dn)
    return inner

@decorator
def say(n):
    print(f'{n} как дела?')

    
say('Петя')
Привет из декоратора
Петя как дела?
