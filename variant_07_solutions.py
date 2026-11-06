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


'''
Функція пошуку кореня рівняння f(x) = 0 методом ділення навпіл.
У випадку f(a) = 0 або f(b) = 0 призначає корінь рівняння рівним a або b відповідно та виходить з циклу.
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
                {"iter": iter_num,
                "a": a,
                "b": b,
                "c": c,
                "interval_len": b - a})
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

    return res, iter_num, iter_list


'''
Функція запису результатів знаходження кореня та протоколу ітерацій у файл
'''
def save_results_to_file(res, iter_num, iter_list,):
    with open("results_variant_07.txt", "w", encoding="utf-8") as file:
        file.write("=" * 75 + "\n")
        file.write("Пошук кореня рівняння методом ділення навпіл\n")
        file.write("=" * 75 + "\n")
        file.write(f"Знайдений корінь: {res:.6f}\n")
        file.write(f"Кількість ітерацій: {iter_num}\n")
        file.write("Протокол ітерацій:\n")
        file.write(f"{'Iter':<6} | {'a':<10} | {'b':<10} | {'c (x)':<10} | {'b - a':<10}\n")
        file.write("-" * 75 + "\n")
        for row in iter_list:
            file.write(
                f"{row['iter']:<6} | {row['a']:<10.6f} | {row['b']:<10.6f} | {row['c']:<10.6f} | {row['interval_len']:<10.6f}\n")


