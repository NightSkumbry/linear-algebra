from .EuclidianAlgorythm import EuclidianAlgorythm
from .Deduction import Deduction
import math
from .Print import Print, CheckFlag



class DiafantExpression:
    def __init__(self, a: int, b: int, c: int, var1: str = 'x', var2: str = 'y') -> None:
        self._A = a
        self._B = b
        self._C = c
        self._VAR1 = var1
        self._VAR2 = var2
        
    def __str__(self) -> str:
        return f'{self._A}x {"-" if self._B < 0 else "+"} {abs(self._B)}y = {self._C}'
    
    
    def check_for_solutions(self, explain:int = 0) -> int:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        g = EuclidianAlgorythm(abs(self._A), abs(self._B)).get_gcd(explain_new)
        return 0 if self._C % g else g
    
    def solve(self, explain:int = 0, var:str = 't') -> tuple[Deduction, Deduction] | None:
        # flgs:
        #  8 - disable first gcd find
        
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        Print(1 +8, explain, f'Решение уравнения  {self}:\n')
        s = self.check_for_solutions(0 if CheckFlag(explain, 8) else explain_new)
        if not s:
            Print(1, explain, f'\n{self._C} не делится на {math.gcd(abs(self._A), abs(self._B))} => решений в ℤ нет.\n')
            Print(2, explain, 'Ответ: Решений в ℤ нет.')
            return
        if not s-1:
            a, b, c = self._A, self._B, self._C
            g = EuclidianAlgorythm(abs(a), abs(b))
        else:
            a, b, c = self._A//s, self._B//s, self._C//s
            g = EuclidianAlgorythm(abs(a), abs(b))
            Print(1, explain, f'\n{self._C} делится на {s} => решаем {DiafantExpression(a, b, c)}.\n')
            s = g.get_gcd(explain_new)
        Print(1, explain)
        lgf = g.get_linear_gcd_form(explain_new)
        x = Deduction(lgf[0]*c if a >= 0 else -lgf[0]*c, b, self._VAR1)
        y = Deduction(lgf[1]*c if b >= 0 else -lgf[1]*c, -a, self._VAR2)
        Print(1, explain, f"#  {self._VAR1} = x'•C + B•{var};  {self._VAR2} = y'•C - A•{var}\n")
        Print(1, explain, f'{x.express(var)};')
        Print(1, explain, f'{y.express(var)}.\n')
        Print(2, explain, f'Ответ: ({x.express(var, with_eq=False, with_z=False)}, {y.express(var, with_eq=False, with_z=False)}), {var} ∈ ℤ.')
        return x, y
            
