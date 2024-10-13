from typing import Self
from .Print import Print


class Deduction:
    def __init__(self, a: int, b: int, var: str = 'x') -> None:
        self._A = a
        self._MOD = b
        self._VAR = var
    
    def __str__(self) -> str:
        return f'{self._VAR} ≡ {self._A} (mod {self._MOD})'
    
    
    def get_MOD(self) -> int:
        return self._MOD
    
    def get_A(self) -> int:
        return self._A
    
    
    def express(self, var: str, *, with_z: bool = True, with_eq: bool = True) -> str:
        return f'{self._VAR + " = " if with_eq else ""}{self._A} {"+" if self._MOD >= 0 else "-"} {abs(self._MOD)}•{var}{", " + var + " ∈ ℤ" if with_z else ""}'
    
    def reverse(self, explain:int = 0): # -> Self | None
        from .Comparison import Comparison
        explain_new = explain - (2 if bin(explain)[2:].zfill(2)[-2] == '1' else 0)
        
        Print(1, explain, f'Найти обратный вычет для  {self}:\n')
        c = Comparison(self._A, 1, self._MOD)
        Print(1, explain, f'Для этого нужно решить  {c}.')
        d = c.to_Deduction(explain_new)
        if d is not None:
            Print(2, explain, f'\nОтвет: ', end='')
            Print(3, explain, d)
            return d
        Print(2, explain, f'Ответ: ', end='')
        Print(3, explain, f'Обратного вычета не существует')
        return
    
    def normalise(self, explain:int = 0) -> None:
        self._MOD = abs(self._MOD)
        self._A %= self._MOD
        Print(3, explain, f'{self}.')

