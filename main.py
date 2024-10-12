from linal.DiafantExpression import DiafantExpression
from linal.Comparison import Comparison
from linal.Deduction import Deduction
from linal.EuclidianAlgorythm import EuclidianAlgorythm
from sys import argv, exit


def choise(k: list, legend: str = ""):
    if legend: print(legend)
    for i in range(len(k)):
        print(f'{i} - {Lof[k[i]]}')
    return k[int(input('--> '))]


def solve_diafant():
    print('\nВведите коэфицианты A, B и C ниже, разделяя их пробелом.')
    s = input('--> ').split()
    if len(s) == 3:
        a0, b0, c0 = map(int, s)
    else:
        raise ValueError(f'Wrong amount of arguments. {len(s)} given, but 3 expected.')
    
    DiafantExpression(a0, b0, c0).solve(explain)


def solve_comparison():
    print('\nВведите коэфицианты A, B и C ниже, разделяя их пробелом.')
    s = input('--> ').split()
    if len(s) == 3:
        a0, b0, c0 = map(int, s)
    else:
        raise ValueError(f'Wrong amount of arguments. {len(s)} given, but 3 expected.')
    
    Comparison(a0, b0, c0).solve(explain)


def find_reverse_deduction():
    print('\nВведите коэфицианты A и B ниже, разделяя их пробелом.')
    s = input('--> ').split()
    if len(s) == 2:
        a0, b0 = map(int, s)
    else:
        raise ValueError(f'Wrong amount of arguments. {len(s)} given, but 2 expected.')
    
    Deduction(a0, b0).reverse(explain)


def find_gcd():
    print('\nВведите коэфицианты A и B ниже, разделяя их пробелом.')
    s = input('--> ').split()
    if len(s) == 2:
        a0, b0 = map(int, s)
    else:
        raise ValueError(f'Wrong amount of arguments. {len(s)} given, but 2 expected.')
    
    e = EuclidianAlgorythm(a0, b0)
    e.get_gcd(explain)
    print()
    e.get_linear_gcd_form(explain)


Lof: dict = {
    solve_diafant: "Решить диафантово уравнение вида Ax + By = C",
    solve_comparison: "Решить сравнение вида Ax ≡ B (mod C)",
    exit: "Выйти",
    find_reverse_deduction: 'Найти обратный вычет для x ≡ A (mod B)',
    find_gcd: 'Найти НОД A и B и его линейное представление',
    
}

print('ЛАЖА - набор скриптов, позволяющий решать задачи из курса линейной алгебры.\n')
explain = (len(argv) == 1 or argv[1] != '-s') + 2
while True:
    a = choise([
        exit,
        find_gcd,
        solve_diafant,
        solve_comparison,
        find_reverse_deduction,
        
    ], 'Выберите тип задачи:')
    a()
    input('\nВ мнею -->')
    
