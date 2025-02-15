# Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# a = [1,2,3,4]
# id(a)
# 2543176812608
# aa = a
# id(aa)
# 2543176812608
# aa[1] = 999
# a
# [1, 999, 3, 4]
# k = a[:]
# id(k)
# 2543176863872
# k[1] = 888
# r
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     r
# NameError: name 'r' is not defined
# k
# [1, 888, 3, 4]
# a
# [1, 999, 3, 4]
# g = copy()
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     g = copy()
# NameError: name 'copy' is not defined. Did you forget to import 'copy'?
# q = a.copy()
# q
# [1, 999, 3, 4]
# id(q)
# 2543176864320
#
#
#
# li = [1,2,3]
# a = [22, li, 33, 44]
# a
# [22, [1, 2, 3], 33, 44]
# li[2] = 999
# li
# [1, 2, 999]
# a
# [22, [1, 2, 999], 33, 44]
# import copy
# d = copy.deepcopy(a)
# d
# [22, [1, 2, 999], 33, 44]
# li[1] = 333
# a
# [22, [1, 333, 999], 33, 44]
# d
# [22, [1, 2, 999], 33, 44]
# имя = "Джонни"
# print(имя)
# Джонни
# li = [1,2,3]
# li[1] = 88
# li
# [1, 88, 3]
# st = '12345'
# st
# '12345'
# st[0]
# '1'
# st[0] = 'dfdedf'
# Traceback (most recent call last):
#   File "<pyshell#39>", line 1, in <module>
#     st[0] = 'dfdedf'
# TypeError: 'str' object does not support item assignment
# len(st)
# 5
# st23 = '12345'
# id(st)
# 2543176898656
# id(st23)
# 2543176898656
# jj = [1,2,3]
# ff = [1,2,3]
# id(jj)
# 2543133069696
# id(ff)
# 2543176705472
# "sdff'sadf'sdfsd'asdf"
# "sdff'sadf'sdfsd'asdf"
# st * 99
# '123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
# res = st * 88
# st
# '12345'
# res
# '12345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
# st+res
# '1234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345123451234512345'
# ch = 'f'
# ch1 = 'v'
# ord(ch)
# 102
# ord(ch1)
# 118
# codeF = 102
# codeV = ord(ch1)
# chr(codeF)
# 'f'
# li = []
# for i in range(250, 275):
#     li.append(chr(i))
#
#
# li
# ['ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē']
# for i in range(1250, 1275):
#     li.append(chr(i))
#
#
# li
# ['ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē', 'Ӣ', 'ӣ', 'Ӥ', 'ӥ', 'Ӧ', 'ӧ', 'Ө', 'ө', 'Ӫ', 'ӫ', 'Ӭ', 'ӭ', 'Ӯ', 'ӯ', 'Ӱ', 'ӱ', 'Ӳ', 'ӳ', 'Ӵ', 'ӵ', 'Ӷ', 'ӷ', 'Ӹ', 'ӹ', 'Ӻ']
# for char in li:
#     print(ord(char), end=' ')
#
#
# 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 1250 1251 1252 1253 1254 1255 1256 1257 1258 1259 1260 1261 1262 1263 1264 1265 1266 1267 1268 1269 1270 1271 1272 1273 1274
# for v in st:
#     print(v)
#
#
# 1
# 2
# 3
# 4
# 5
# excl = '25'
# for v in st:
#     if v in excl:
#         continue
#     print(v)
#
#
# 1
# 3
# 4
# for i in range(len(st)):
#     print('index:', i, '| value:', st[i])
#
#
# index: 0 | value: 1
# index: 1 | value: 2
# index: 2 | value: 3
# index: 3 | value: 4
# index: 4 | value: 5
# st = 'helloddee'
# for i in range(len(st)):
#     print('index:', i, '| value:', st[i])
#
#
# index: 0 | value: h
# index: 1 | value: e
# index: 2 | value: l
# index: 3 | value: l
# index: 4 | value: o
# index: 5 | value: d
# index: 6 | value: d
# index: 7 | value: e
# index: 8 | value: e
# msg = 'rome: grog, shakira.'
# secret = 8
# secretMessage = ''
# for c in msg:
#     secretMessage += chr(ord(c)+secret)
#
#
# secretMessage
# 'zwumB(ozwo4({pisqzi6'
# res = ''
# for c in secretMessage:
#     res += chr(ord(c)-secret)
#
#
# res
# 'rome: grog, shakira.'
# res1 = ''
# for c in secretMessage:
#     res1 += chr(ord(c)-3)
#
#
# res1
# 'wtrj?%lwtl1%xmfpnwf3'
# st
# 'helloddee'
# st[::-1]
# 'eeddolleh'
# st = '[fix] sadasdasd.'
# st1 = '[bug] ssdsdasd.'
# st2 = '[hlp] 342ssdssd.'
# st[1:4]
# 'fix'
# li = [st, st1, st2]
# for s in li:
#     res = s[1:4]
#     if res == 'bug':
#         print('1111')
#     elif res == 'fix':
#         print('fix')
#     else:
#         print('help')
#
#
# fix
# 1111
# help
# st[2:]
# 'ix] sadasdasd.'
# st[::3]
# '[xsaa.'
# st.upper()
# '[FIX] SADASDASD.'
# st.lower()
# '[fix] sadasdasd.'
# name = input('->').upper()
# ->awdwwqaer
#
# name
# 'AWDWWQAER'
# st.index('d')
# 8
# st.index('`')
# Traceback (most recent call last):
#   File "<pyshell#126>", line 1, in <module>
#     st.index('`')
# ValueError: substring not found
# name = 'John'
# name[:2]+'k'+name[3:]
# 'Jokn'
# name = 'dwswqdwedqwewqeeeee'
# name.count('e')
# 7
# name.count('!')
# 0
# >>> name.isalpha()
# True
# >>> name = 'dwswqdwedqwewqeeeee*'
# >>> name.isalpha()
# False
# >>> nums = '12345'
# >>> nums.isdigit()
# True
# >>> nums.isalfa()
# Traceback (most recent call last):
#   File "<pyshell#137>", line 1, in <module>
#     nums.isalfa()
# AttributeError: 'str' object has no attribute 'isalfa'. Did you mean: 'isalpha'?
# >>> nums.isalpha()
# False
# >>> name.islower()
# True
# >>> ' fff'.isspace()
# False
# >>> ' '.isspace()
# True
# >>> li
# ['[fix] sadasdasd.', '[bug] ssdsdasd.', '[hlp] 342ssdssd.']
# >>> res = '|'.join(li)
# >>> res
# '[fix] sadasdasd.|[bug] ssdsdasd.|[hlp] 342ssdssd.'
# >>> res.replace('bug', 'lol')
# '[fix] sadasdasd.|[lol] ssdsdasd.|[hlp] 342ssdssd.'
# >>> res
# '[fix] sadasdasd.|[bug] ssdsdasd.|[hlp] 342ssdssd.'
# >>> res.endswith('.')
# True
# >>> res.endswith('!')
# False
# >>> res.endswith('[')
# False
# >>> res.endswith('[fix')
# False
# >>> res.startswith('[fix')
# True
# >>> res.startswith('fix')
# False
# >>> st = '      edfdsrf      '
# >>> st
# '      edfdsrf      '
# >>> st.strip{}
# SyntaxError: invalid syntax
# >>> st.strip()
# 'edfdsrf'
# >>> st
# '      edfdsrf      '
# >>> st.lstrip()
# 'edfdsrf      '
# >>> st.rstrip()
# '      edfdsrf'
# >>> st.title()
# '      Edfdsrf      '
# >>> st += st
# >>> st
# '      edfdsrf            edfdsrf      '
# >>> st.title()
# '      Edfdsrf            Edfdsrf      '
# >>> st.swapcase()
# '      EDFDSRF            EDFDSRF      '
# >>> st.capitalize()
# '      edfdsrf            edfdsrf      '
# >>> st.split()
# ['edfdsrf', 'edfdsrf']
# >>> st = '*kojoj*okjoi*lkjokj*gggg*4444'
# >>> st.split('*')
# ['', 'kojoj', 'okjoi', 'lkjokj', 'gggg', '4444']
