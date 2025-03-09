Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Dog:
...     inst_cont = False
...     def __init__(self, name):
...         if Dog.inst_cont == False:
...             self.name = name
...             Dog.inst_cont == True
...         else:
...             raise Exception('собака это синглтон')
... 
...         
>>> Dog.inst_cont
False
>>> d1 = Dog('Bobik')
>>> Dog.inst_cont
False
>>> class Dog:
...     inst_cont = False
...     def __init__(self, name):
...         if Dog.inst_cont == False:
...             self.name = name
...             Dog.inst_cont = True
...         else:
...             raise Exception('собака это синглтон')
... 
...         
>>> Dog.inst_cont
False
>>> d1 = Dog('Bobik')
>>> Dog.inst_cont
True
>>> d2 = Dog('Vasia')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d2 = Dog('Vasia')
  File "<pyshell#13>", line 8, in __init__
    raise Exception('собака это синглтон')
Exception: собака это синглтон
