# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# 1/0
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     1/0
# ZeroDivisionError: division by zero
# s = 'sssdsd'
# s.capitalize()
# 'Sssdsd'
# s.decapitalize()
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     s.decapitalize()
# AttributeError: 'str' object has no attribute 'decapitalize'. Did you mean: 'capitalize'?
# li = [1,2,3]
# li[0.5]
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     li[0.5]
# TypeError: list indices must be integers or slices, not float
# try:
#     1/0
# except:
#     print(11)
#
#
# 11
# try:
#     li = [1,2,3]
#     li[0.5]
# except:
#     print(11)
#
#
# 11
# try:
#     1/0
# except ValueError:
#     print('ValueError')
# except:
#     print(11)
#
#
# 11
# try:
#     1/0
# except ZeroDivisionError:
#     print('x/0')
# except ValueError:
#     print('ValueError')
# except:
#     print(11)
#
#
# x/0
#
# try:
#     try:
#     1/0
# except ZeroDivisionError:
#     print('x/0')
# except ValueError:
#     print('ValueError')
# except:
#     print(11)
# except:
#     print(11)
#
# SyntaxError: expected an indented block after 'try' statement on line 2
#
# try:
#     13/0
# except ZeroDivisionError as zde:
#     print('x/0', zde.args)
# except ValueError as ve:
#     print('ValueError', ve.args)
# except:
#     print(11)
#
#
# x/0 ('division by zero',)
# try:
#     int('sdffsfe')
#
# except ZeroDivisionError as zde:
#     print('x/0', zde.args)
# except ValueError as ve:
#     print('ValueError', ve.args)
# except:
#     print(11)
#
#
# ValueError ("invalid literal for int() with base 10: 'sdffsfe'",)
#
# try:
#     raise ValueError
#
# except ZeroDivisionError as zde:
#     print('x/0', zde.args)
# except ValueError as ve:
#     print('ValueError', ve.args)
# except:
#     print(11)
#
#
# ValueError ()
#
# try:
#     raise ValueError('sdsads')
# except ZeroDivisionError as zde:
#     print('x/0', zde.args)
# except ValueError as ve:
#     print('ValueError', ve.args)
# except:
#     print(11)
#
#
# ValueError ('sdsads',)
# raise IndexError
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     raise IndexError
# IndexError
#
# try:
#     raise ValueError('sdsads')
# except ZeroDivisionError as zde:
#     print('x/0', zde.args)
# except ValueError as ve:
#     print('ValueError', ve.args)
# except:
#     print(11)
#
#
# ValueError ('sdsads',)
#
# import erfdqwed
# Traceback (most recent call last):
#   File "<pyshell#35>", line 1, in <module>
#     import erfdqwed
# ModuleNotFoundError: No module named 'erfdqwed'
# a = 6
# if a == 8:
#     try:
#         import huiiuy
#     except:
#         pass
#
#
# if a == 8:
#     try:
#         import huiiuy
#     except:
#         pass
# else:
#     print('делай')
#
#
# делай
# if a == 6:
#     try:
#         import huiiuy
#     except:
#         pass
# else:
#     print('делай')
#
#
#
#
#
# try:
#     raise ZeroDivisionError
# except:
#     print('default')
#
#
# default
# try:
#     raise ZeroDivisionError
# except ArithmeticError:
#     print('ArithmeticError')
# except ZeroDivisionErro:
#     print('ZeroDivisionError')
# except:
#     print('default')
#
#
# ArithmeticError
# try:
#     raise ZeroDivisionError
# except ZeroDivisionErro:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')
#
# except:
#     print('default')
#
#
# Traceback (most recent call last):
#   File "<pyshell#63>", line 2, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "<pyshell#63>", line 3, in <module>
#     except ZeroDivisionErro:
# NameError: name 'ZeroDivisionErro' is not defined. Did you mean: 'ZeroDivisionError'?
# try:
#     raise ZeroDivisionError
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except ArithmeticError:
#     print('ArithmeticError')
#
# except:
#     print('default')
#
#
# ZeroDivisionError
# try:
#     raise ZeroDivisionError
# except Exception as e:
#     print(e.args)
# except:
#     print('default')
#
#
# ()
# >>> def a(x):
# ...     try:
# ...         res = int(x)
# ...     except:
# ...         print(123)
# ...
# ...
# >>> a(123)
# >>> a('sd')
# 123
# >>> def a(x):
# ...     try:
# ...         res = int(x)
# ...     except:
# ...         print(123)
# ...         raise
# ...
# ...
# >>> a(123)
# >>> a('qww')
# 123
# Traceback (most recent call last):
#   File "<pyshell#80>", line 1, in <module>
#     a('qww')
#   File "<pyshell#78>", line 3, in a
#     res = int(x)
# ValueError: invalid literal for int() with base 10: 'qww'
# >>> def b(x):
# ...     try:
# ...         a(x)
# ...     except:
# ...         print('321')
# ...         raise
# ...
# ...
# >>> b('sdffds')
# 123
# 321
# Traceback (most recent call last):
#   File "<pyshell#87>", line 1, in <module>
#     b('sdffds')
#   File "<pyshell#86>", line 3, in b
#     a(x)
#   File "<pyshell#78>", line 3, in a
#     res = int(x)
# ValueError: invalid literal for int() with base 10: 'sdffds'
# >>> assert 1
# >>> assert 0
# Traceback (most recent call last):
#   File "<pyshell#89>", line 1, in <module>
#     assert 0
# AssertionError
# >>> assert ''
# Traceback (most recent call last):
#   File "<pyshell#90>", line 1, in <module>
#     assert ''
# AssertionError
# >>> assert 'l'
# >>> assert False
# Traceback (most recent call last):
#   File "<pyshell#92>", line 1, in <module>
#     assert False
# AssertionError
# >>> res = 10
# >>> assert res == 10
# >>> assert res == 11
# Traceback (most recent call last):
#   File "<pyshell#95>", line 1, in <module>
#     assert res == 11
# AssertionError
# >>> [DEBUG ON]
# >>> [DEBUG OFF]
