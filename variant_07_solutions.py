"""
Лабораторна робота: Варіант 7
Студент: Зембович Дарина
Група: EIP 30
"""

'''
Функція розрахунку f(x) = x^3-3x-2e^(-x)
Функція приймає значення аргумента х та повертає розраховане значення f(x)
'''
def target_function(x):
    import math
    return x**3 - 3*x - 2*math.exp(-x)

'''Функція пошуку кореня рівняння f(x) = 0 методом ділення навпіл.
У випадку f(a) = 0 або f(b) = 0 призначає корінь рівняння рівним a або b відповідно та виходить з циклу
В інших випадках продовжує пошук кореня та ділить відрізок навпіл обираючи потрібний відрізок відповідно до умов:
1)f(a)*f(c) > 0 --> [c, b]
2)f(a)*f(c) < 0 --> [a, c]
Функція повертає корінь, кількість ітерацій та їх список(номер ітерації, значення a, b, c та довжину інтервала)
'''
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

