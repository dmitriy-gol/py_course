Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Number(Exception):
...      def __init__(self, namber, mes):
...          self.namber = namber
...          self.mes = mes
... 
...          
>>> class User:
...      def __init__(self, name):
...          self.name = name
...           
...      def __str__(self):
...          return f'user name: {self.name}.'
...      def call(self, number):
...          if len(number) < 8:
...              raise Number(number, 'короткий номер!')
...          return f'звоню {number}'
... 
...         
>>> u = User('Vasia')
>>> try:
...     u.call('1234')
... except Number as e:
...     print(e)
... except:
...     print(-1)
... 
...     
('1234', 'короткий номер!')
>>> try:
...     u.call('126546545645634')
... except Number as e:
...     print(e)
... except:
...     print(-1)
... 
...     
'звоню 126546545645634'
