"""
Лабораторна робота: Варіант 7
Студент: Зембович Дарина
Група: EIP 30
"""

#Функція розрахунку f(x) = x^3-3x-2e^(-x)
def target_function(x):
    import math
    return x**3 - 3*x - 2*math.exp(-x)