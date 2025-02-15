# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# li = []
# li
# []
# a = [1, 2, 3, True]
# a
# [1, 2, 3, True]
# a[3]
# True
# a['1']
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     a['1']
# TypeError: list indices must be integers or slices, not str
# a[6]
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     a[6]
# IndexError: list index out of range
# type[a]
# type[[1, 2, 3, True]]
# type(a)
# <class 'list'>
# type(a[0])
# <class 'int'>
# st = "Hello"
# st.upper()
# 'HELLO'
# st
# 'Hello'
# q = 100
# q.upper()
# Traceback (most recent call last):
#   File "<pyshell#14>", line 1, in <module>
#     q.upper()
# AttributeError: 'int' object has no attribute 'upper'
# 'sdawsd'.upper()
# 'SDAWSD'
# a = [4, 5, 45, 6, 7, 8, 23]
# a.append(777)
# a
# [4, 5, 45, 6, 7, 8, 23, 777]
# a.insert(2, 9)
# a
# [4, 5, 9, 45, 6, 7, 8, 23, 777]
# len(a)
# 9
# a.reverse()
# a
# [777, 23, 8, 7, 6, 45, 9, 5, 4]
# a.reverse()
# a
# [4, 5, 9, 45, 6, 7, 8, 23, 777]
# a.pop()
# 777
# a
# [4, 5, 9, 45, 6, 7, 8, 23]
# res = a.pop(3)
# res
# 45
# a
# [4, 5, 9, 6, 7, 8, 23]
# del a[0]
# a
# [5, 9, 6, 7, 8, 23]
# del li
# li
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     li
# NameError: name 'li' is not defined
# a.remove(1)
# Traceback (most recent call last):
#   File "<pyshell#35>", line 1, in <module>
#     a.remove(1)
# ValueError: list.remove(x): x not in list
# a.remove(8)
# a
# [5, 9, 6, 7, 23]
# todel = 555
# if todel in a:
#     a.remove(todel)
#
#
# a
# [5, 9, 6, 7, 23]
# a.count(6)
# 1
# a.append(6)
# a.count(a)
# 0
# a.count(6)
# 2
# a.clear()
# a
# []
# a = [4, 5, 45, 6, 7, 8, 23]
# a.index(6)
# 3
# li = [7, 7, 7]
# a += li
# a
# [4, 5, 45, 6, 7, 8, 23, 7, 7, 7]
# a *= 2
# a
# [4, 5, 45, 6, 7, 8, 23, 7, 7, 7, 4, 5, 45, 6, 7, 8, 23, 7, 7, 7]
# q = [1, 2, 5, 7 , 2, 4, 6]
# q[-2]
# 4
# q[6]
# 6
# hat_list = [1, 2, 3, 4, 5]
# print(len(hat_list)
#
#       )
# 5
# hat_list[2] = int(input('введи число:'))
# введи число:9
# hat_list.pop()
# 5
# print(len(hat_list))
# 4
# hat_list
# [1, 2, 9, 4]
# q
# [1, 2, 5, 7, 2, 4, 6]
# for i in q:
#     print(i)
#
#
# 1
# 2
# 5
# 7
# 2
# 4
# 6
# li = []
# for i in range(int(input('n->'):
#     li.append(int(input('v->')))
#
# SyntaxError: invalid syntax
# for i in range(int(input('n->'))):
#     li.append(int(input('v->')))
#
#
# n->4
# v->44
# v->34
# v->23
# v->41
# li
#
# [44, 34, 23, 41]
# for i in range(len(li)):
#     print(li[i])
#
#
# 44
# 34
# 23
# 41
# li
#
# [44, 34, 23, 41]
# li.reverse()
#
# li.append(100)
#
# li
#
# [41, 23, 34, 44, 100]
# sorted(li)
#
# [23, 34, 41, 44, 100]
# li
#
# [41, 23, 34, 44, 100]
# for i in sorted(li):
#                    print(i, end=' ')
#
#
# 23 34 41 44 100
# sorted(li, reverse=True)
#
# [100, 44, 41, 34, 23]
# li = [3, 5, 0, -10, 4]
#
# a, b = 66, 77
#
# a, b = b, a
#
# a
#
# 77
# b
#
# 66
# li[1], li[2] = li[2], li[1]
#
# li
#
# [3, 0, 5, -10, 4]
# li[2], li[3] = li[3], li[2]
#
# li
#
# [3, 0, -10, 5, 4]
# li[0], li[1] = li[1], li[0]
#
# li
#
# [0, 3, -10, 5, 4]
# max(li)
#
# 5
# sum(li)
#
# 2
# sum(li)/len(li)
#
# 0.4
# built-in functions python
#
# SyntaxError: invalid syntax
# li = [1, 2, 3, 4]
#
# a = li
#
# ad(li)
#
# Traceback (most recent call last):
#   File "<pyshell#109>", line 1, in <module>
#     ad(li)
# NameError: name 'ad' is not defined. Did you mean: 'a'?
# id(li)
#
# 2058415902144
# is(a)
#
# SyntaxError: invalid syntax
# id(li)
#
# 2058415902144
# a
#
# [1, 2, 3, 4]
# li
#
# [1, 2, 3, 4]
# a = li.copy()
#
# id(a)
#
# 2058416271424
# id(li)
#
# 2058415902144
# li[:]
#
# [1, 2, 3, 4]
# li[:3]
#
# [1, 2, 3]
# li[1:]
#
# [2, 3, 4]
# li += li
#
# li
#
# [1, 2, 3, 4, 1, 2, 3, 4]
# k = li[::2]
#
# k
#
# [1, 3, 1, 3]
# li[::-1]
#
# [4, 3, 2, 1, 4, 3, 2, 1]
# 77 in li
#
# False
# 4 in li
#
# True
# s = {}
#
# type(s)
#
# <class 'dict'>
# s = set()
#
# type(s)
#
# <class 'set'>
# s = {"df", 1, 2, 3, 1, 1, 2, 3}
#
# s
#
# {3, 1, 2, 'df'}
# s.add(1)
#
# s
#
# {3, 1, 2, 'df'}
# for v in s:
#                    print(v, end=' ')
#
#
# 3 1 2 df
# 99 in s
#
# False
# 1 in s
#
# True
# s.update({1, 2, 3, 4, 666})
#
# s
#
# {1, 2, 3, 'df', 4, 666}
# s.remove(555)
#
# Traceback (most recent call last):
#   File "<pyshell#143>", line 1, in <module>
#     s.remove(555)
# KeyError: 555
# s.remove(4)
#
# s
#
# {1, 2, 3, 'df', 666}
# s.discard(444)
#
# s.discard(1)
#
# s
#
# {2, 3, 'df', 666}
# s.len()
#
# Traceback (most recent call last):
#   File "<pyshell#149>", line 1, in <module>
#     s.len()
# AttributeError: 'set' object has no attribute 'len'
# len(s)
#
# 4
# li
#
# [1, 2, 3, 4, 1, 2, 3, 4]
# li = list(set(li))
#
# li
#
# [1, 2, 3, 4]
# st
#
# 'Hello'
# list(st)
#
# ['H', 'e', 'l', 'l', 'o']
# list
#
# <class 'list'>
# st
#
# 'Hello'
# set(st)
#
# {'o', 'H', 'e', 'l'}
# st
#
# 'Hello'
# str(li)
#
# '[1, 2, 3, 4]'
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# my_list = list(set(li))
#
# my_list
#
# [1, 2, 3, 4]
# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# my_list = [::1]
#
# SyntaxError: invalid syntax
# my_list[::-1]
#
# [9, 2, 6, 2, 4, 1, 4, 4, 2, 1]
# li = [1, 2, 3, 4, 5]
#
# resliast = []
#
# resliast = []
#
# reslist = []
#
# for i in li:
#                    reslist.append(i**2)
#
#
# li
#
# [1, 2, 3, 4, 5]
# reslist
#
# [1, 4, 9, 16, 25]
# reslist = []
#
# reslist = [v**2 for v in li]
#
# reslist
#
# [1, 4, 9, 16, 25]
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# reslist = [v**2 for v in li if v%2==0]
#
# reslist
#
# [4, 16, 36, 64, 100]
# li
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> number = [int(input("-->")) for i in range(int(input("n-->)))]
# ...
# SyntaxError: unterminated string literal (detected at line 1)
# >>> number = [int(input("-->")) for i in range(int(input("n-->")))]
# ...
# n-->5
# -->44
# -->55
# -->66
# -->7
# -->9
# >>> numbers
# ...
# Traceback (most recent call last):
#   File "<pyshell#185>", line 1, in <module>
#     numbers
# NameError: name 'numbers' is not defined. Did you mean: 'number'? Or did you forget to import 'numbers'?
# >>> number
# ...
# [44, 55, 66, 7, 9]
# >>> li
# ...
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> li = [[1,2,3], [11,22,33], [0,5,8]]
# ...
# >>> li
# ...
# [[1, 2, 3], [11, 22, 33], [0, 5, 8]]
# >>> li[0][2]
# ...
# 3
# >>> li[1][1]
# ...
# 22
# >>> li[2][0]
# ...
# 0
# >>> li[0].append(333)
# ...
# >>> li
# ...
# [[1, 2, 3, 333], [11, 22, 33], [0, 5, 8]]
# >>> li[0][2] = 222
# ...
# >>> li
# ...
# [[1, 2, 222, 333], [11, 22, 33], [0, 5, 8]]
# >>> li = [[1,2,3], [1,2,3]]
# ...
# >>> li
# ...
# [[1, 2, 3], [1, 2, 3]]
# >>> li[0][0][1]
# ...
# Traceback (most recent call last):
#   File "<pyshell#199>", line 1, in <module>
#     li[0][0][1]
# TypeError: 'int' object is not subscriptable
# >>> li = [[[1,2,3], [1,2,3]]]
# ...
# >>> li[0][0][1
# ...          ]
# ...
# 2
# >>> li[0][0]
# ...
# [1, 2, 3]
# >>> li[0][0].clear()
# ...
# >>> li
# ...
# [[[], [1, 2, 3]]]
