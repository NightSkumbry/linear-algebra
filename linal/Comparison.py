from .Deduction import Deduction
from .DiafantExpression import DiafantExpression
from .EuclidianAlgorythm import EuclidianAlgorythm
from typing import Self
from .Print import Print, CheckFlag


class Comparison:
    def __init__(self, a: int, b: int, c: int, var: str = 'x') -> None:
        self._A = a
        self._B = b
        self._MOD = c
        self._VAR = var
    
    def __str__(self) -> str:
        return f'{self._A if self._A != 1 else ""}{self._VAR} ≡ {self._B} (mod {self._MOD})'
    
    
    def to_Deduction(self, explain:int = 0, var:str = 't') -> Deduction | None:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        s = self.solve(explain_new +16, var)
        return None if s is None else s[0]
        
    def to_DiafantExpression(self) -> DiafantExpression:
        return DiafantExpression(self._A, -self._MOD, self._B, var1=self._VAR)
        
    def solve(self, explain:int = 0, var:str= 't') -> tuple[Deduction, int] | None:
        # flgs:
        #  16 - disable modular answer
        
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        Print(1 +16, explain, f'Решение сравнения  {self}:')
        if self._A >= self._MOD or self._A < 0 or self._B >= self._MOD or self._B < 0:
            Print(1, explain, '\nНормализуем сравнение, т. е. сделаем A, B ∈ [0, C);')
            self.normalise(explain_new)
        Print(1, explain)
        solution_count = EuclidianAlgorythm(self._A, self._MOD).get_gcd(explain_new)
        
        D = self.to_DiafantExpression()
        Print(1, explain, f'Получается, у сравнения будет {solution_count} решений. Найдём их, решив уравнение {D}.')
        sol = D.solve(explain_new +8, var)
        if sol is None:
            Print(2, explain, 'Ответ: Решений в ℤ нет.')
            return
        x = sol[0]
        Print(1, explain, f'Нас интересует только {self._VAR}. Запишем его в виде x = A + B•{var}, {var} ∈ ℤ, где 0 <= A < B .\n')
        x.normalise()
        Print(2, explain, f'Ответ: ', end='')
        Print(3, explain, f'{x.express(var, with_z=False)}' + (f' (mod {self._MOD})' if not CheckFlag(16, explain) else '') + f', {var} ∈ ℤ')
        return x, self._MOD
        
    def normalise(self, explain:int = 0) -> None:
        self._MOD = abs(self._MOD)
        self._A %= self._MOD
        self._B %= self._MOD
        Print(3, explain, f'{self}.')
        
        
