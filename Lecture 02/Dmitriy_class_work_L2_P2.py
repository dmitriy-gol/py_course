# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# a, b = 1, 2
# a
# 1
# a == b
# False
# a != b
# True
# a, b = 9, 9
# a == b
# True
# a >= b
# True
# password = input('login')
# login12345
# if password == '12345':
#     print('ok')
#
#
# ok
# if password == 12
# SyntaxError: expected ':'
# if password == 12:
#     print('ok')
# else:
#     print('no')
#
#
# no
# secret = 12
# secret1 = 5
# if password == secret:
#     print('ok')
# elif:
#
# SyntaxError: invalid syntax
# if password == secret:
#     print('ok')
# elif password == secret1:
#     print('spy ok')
# else:
#     print('no')
#
#
# no
# a = 123
# if a == 123:
#     res = True
# else:
#     res = False
#
#
# res
# True
# res = True if a == 123 else False
# res
# True
# res = a == 123
# res
# True
# password = '123'
# match password:
#     case '1235':
#         print('ok')
#     case '123':
#         print('---')
#     case _:
#         print('no')
#
#
# ---
# counter = 1
# while counter < 10:
#     print(counter)
#     counter += 3
#
#
# 1
# 4
# 7
# for i in range(5):
#     print(i)
#
#
# 0
# 1
# 2
# 3
# 4
# import time
# for i in range(5):
#     print('sleep', i)
#     time.sleep(1)
#
#
# sleep 0
# sleep 1
# sleep 2
# sleep 3
# sleep 4
# st = 'hello 1234'
# find = '2'
# find in st
# True
# if find in st:
#     print('yes')
# else:
#     print('no')
#
#
# yes
# no_print = 'вапвапцузэ'
# w = input('слово:')
# слово:sdfaf3245ыва
# w
# 'sdfaf3245ыва'
# for char in w:
#     print(char)
#
#
# s
# d
# f
# a
# f
# 3
# 2
# 4
# 5
# ы
# в
# а
# for char in w:
#     if char in no_print:
#         continue
#     print('char')
#
#
# char
# char
# char
# char
# char
# char
# char
# char
# char
# char
# for char in w:
#     if char in no_print:
#         continue
#     print(char)
# ...
# ...
# s
# d
# f
# a
# f
# 3
# 2
# 4
# 5
# ы
# >>> for char in w:
# ...     if char not in no_print:
# ...         continue
# ...     print(char)
# ...
# ...
# в
# а
# >>> for char in w:
# ...     if char not in no_print:
# ...         continue
# ...     print(char)
# ... else:
# ...     print('успешно...')
# ...
# ...
# в
# а
# успешно...
# >>> for char in w:
# ...     if char not in no_print:
# ...         break
# ...     print(char)
# ... else:
# ...     print('успешно...')
# ...
# ...
# >>> age = 21
# >>> money = 1000
# >>> if age > 18 and money > 900:
# ...     print('ok')
# ...
# ...
# ok
# >>> age = 16
# >>> if age > 18 and money > 900:
# ...     print('ok')
# ...
# ...
# >>> True and True and False
# False
# >>> age = 21
# >>> if age > 18 or money > 900:
# ...     print('ok')
# ...
# ...
# ok
# >>> age = 17
# >>> if age > 18 or money > 900:
# ...     print('ok')
# ...
# ...
# ok
# >>> money = -1
# >>> if age > 18 or money > 900:
# ...     print('ok')
# ...
# ...
# >>> False or False or True
# True
# >>> not True
# False
# >>> age
# 17
# >>> age > 10
# True
# >>> not age > 10
# False
# >>> not not False
# False
