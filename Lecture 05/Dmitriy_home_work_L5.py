# # Homework 5.1
# # A leap year
# def is_year_leap(yr):
#     """
#     Функция вычисляет високосный год
#
#     Параметры:
#     yr: -> число, обязательно
#
#     Возвращает:
#     bool True or False
#     """
#     if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
#         return True
#     return False
#
#
# test_data = [1500, 1900, 2000, 2016, 1987]
# test_results = [False, False, True, True, False]
#
# for year , results in zip(test_data, test_results):
#     if is_year_leap(year) == results:
#         print(year, 'is leap? --> ', results)
#     else:
#         print(year, 'from your func --> ', is_year_leap(year))
#         print('but expected --> ', results)
#
#
#
#
# # Homework 5.4
# # Fibonacci numbers
# def feb(num):
#     """
#     Функция вычисляет введенное
#     пользователем число Фибоначчи
#
#     Параметры:
#     num: -> число, обязательно
#
#     Возвращает:
#     Число или ничего
#     """
#     if num < 1:
#         return None
#
#     if num < 3:
#         return 1
#
#     f1 = f2 = 1
#
#     for _ in range(2, num):
#         f1, f2 = f2, f1 + f2
#
#     return f2
#
# res = feb(int(input('Введите число Фибоначчи: ')))
# print('Результат: ', res)
#
# print('Числа, входящие в последовательность Фибоначчи:')
# for i in range(-1, 25):
#     print(feb(i))
