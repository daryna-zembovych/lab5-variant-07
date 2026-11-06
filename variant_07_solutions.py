"""
Лабораторна робота: Варіант 7
Студент: Зембович Дарина
Група: EIP 30
"""

#Функція розрахунку f(x) = x^3-3x-2e^(-x)
def target_function(x):
    import math
    return x**3 - 3*x - 2*math.exp(-x)

#Функція пошуку кореня рівняння f(x) = 0 методом ділення навпіл
#Приймає функцію, межі відрізка та точність
def solve_bisection(target_function, a, b, E):
    res = 0
    iter_num = 0
    iter_list = []
    while (b - a)/(2) >= E:
        iter_num += 1
        c = (a + b) / 2
        iter_list.append(
            {
                "iter": iter_num,
                "a": a,
                "b": b,
                "c": c,
                "interval_len": b - a,
            })
        if target_function(a) == 0:
            res = a
            break
        elif target_function(b) == 0:
            res = b
            break
        else:
            if target_function(a)*target_function(c) > 0:
                a = c
            elif target_function(a)*target_function(c) < 0:
                b = c
            res = (a + b) / 2

    return res, iter_list, iter_num
