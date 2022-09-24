# # 1.Проверить является ли число квадартом второго.

# a = int(input('Enter a:'))
# b = int(input('Enter b:'))

# if a**2 == b or b**2 == a:
#     print('yes')
# else:
#     print('no')


# # 2.Найти максимальныое число.

# some_list = []
# for i in 1, 2, 3, 4, 5:
#     some_list.append(int(input()))
# print(some_list)
# max = some_list[0]
# for i in some_list:
#     if max < i:
#         max = i
# print (max)

# 3.Написать программу, принимающую на вход число N. И выводить числа от -N до N

# N = int(input('Enter N:'))
# for i in range(-N, N+1):
#     print(f'{i}')

# 4.Написать программу, принимающую на вход дробь и показывать первую цифру дробной части числа.

# N = float(input('Enter N:'))
# print(int(N*10) % 10)

# 5. Проверить делиться ли число без остатка на 5, на 10, на 15, но не на 30.

N = int(input('Enter N:'))
def function(N):
    return (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0
print(function(N))
