Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
input('пароль:')
пароль:qwer123
'qwer123'
pass = input('пароль:')
SyntaxError: invalid syntax
password = input('пароль:')
пароль:qwer12
print(password)
qwer12
msg = """asdfasf
asefsef
asdfsaf

-->"""
a = input(msg)
asdfasf
asefsef
asdfsaf

-->sda
print(a)
sda
type(a)
<class 'str'>
a = input(msg)
asdfasf
asefsef
asdfsaf

-->12345
type(a)
<class 'str'>
a*2
'1234512345'
num = input('дай мне число:')
дай мне число:123
res = num ** 2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    res = num ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
a = '123'
b = '3.5'
c = 12
type(a)
<class 'str'>
type(c)
<class 'int'>
d = 5.5
type(c)
<class 'int'>
type(d)
<class 'float'>
int
<class 'int'>

int()
0
str()
''
>>> int(d)
5
>>> str(d)
'5.5'
>>> int('123 g')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int('123 g')
ValueError: invalid literal for int() with base 10: '123 g'
>>> d = str(d)
>>> type(d)
<class 'str'>
>>> d
'5.5'
>>> a = .77
>>> print(a)
0.77
>>> print(2 ** 3.)
8.0
>>> 2 ** 3 ** 4
2417851639229258349412352
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
>>> 0 / 5
0.0
>>> s, ss = 'hello', 'lol'
>>> s + ss
'hellolol'
>>> res = s + s + s + ss
>>> print(res)
hellohellohellolol
>>> len(res)
18
>>> len(s)
5
>>> a = 'sddsd' 'sadsad' 'ewrwer'
>>> a
'sddsdsadsadewrwer'
>>> a = '*' * 20
>>> a
'********************'
>>> a, b = 1, 2
>>> print(a,'+',b,'=', a+b)
1 + 2 = 3
>>> print(f'{a}+{b}={a+b}')
1+2=3
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a = int(input('-->'))
-->123
>>> type(a)
<class 'int'>
>>> a**2
15129
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
