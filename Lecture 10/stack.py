Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
stack = []
def push(val):
    stack.append(val)

    

def pop():
    stack.pop()

    

stack.push(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    stack.push(1)
AttributeError: 'list' object has no attribute 'push'
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
    pass

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()

        
s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.stack
[1, 2, 3]
s2 = Stack()
s2.stack
[]
s1.pop()
s1.stack
[1, 2]
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, val):
        self.__stack.append(val)
    def pop(self):
        try:
            self.__stack.pop()
         except:
             
SyntaxError: unindent does not match any outer indentation level
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self, val):
        self.__stack.append(val)
    def pop(self):
...         try:
...             self.__stack.pop()
...         except:
...             return 'ne ok'
...         return 'ok'
...     def show(self):
...         return self.__stack
... 
...     
>>> s = Stack()
>>> s.pop()
'ne ok'
>>> s.push(123)
>>> s.push(1)
>>> s.push(3)
>>> s.push(2)
>>> s.show()
[123, 1, 3, 2]
>>> s.pop()
'ok'
>>> s.show()
[123, 1, 3]
>>> s.pop()
'ok'
>>> s.show()
[123, 1]
>>> 
>>> 
>>> class CountingStack(Stack):
...     def __init__(self):
...         super().__init__()
...         self.counter = 0
...         self.summa = 0
...     def push(self, val):
...         self.counter += 1
...         self.summa += val
...         super().push(val)
... 
...         
>>> s = CountingStack()
>>> s.show()
[]
>>> s.pop()
'ne ok'
>>> s.counter
0
>>> s.summa
0
>>> s.push(1)
>>> s.push(2)
>>> s.push(3)
>>> s.push(4)
>>> s.push(999)
>>> s.show()
[1, 2, 3, 4, 999]
>>> s.counter
5
>>> s.summa
1009
>>> s.pop()
'ok'
>>> s.pop()
'ok'
>>> s.pop()
'ok'
>>> s.pop()
'ok'
>>> s.pop()
'ok'
>>> s.pop()
'ne ok'
>>> s.show()
[]
