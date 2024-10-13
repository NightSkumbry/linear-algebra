from .Deduction import Deduction
from .Comparison import Comparison
from .Print import Print, CheckFlag
import math
from functools import reduce


class DeductionSystem:
    def __init__(self, *comps:Deduction, var:str = 'x') -> None:
        self._VAR = var
        self._Deductions: list[Deduction] = sorted(comps, key=lambda x: x.get_MOD())
    
    def __str__(self) -> str:
        if (l := len(self._Deductions)) >= 3:
            s1 = '⎧ ' + ';\n⎪ '.join(map(str, self._Deductions)) + '.'
            ss = s1.split('\n')
            ss[-1] = '⎩' + ss[-1][1:]
            ss[l//2] = '⎨' + ss[l//2][1:]
            s = '\n'.join(ss)
        elif l == 2:
            s = f'⎰ {self._Deductions[0]};\n⎱ {self._Deductions[1]}.'
        else:
            s = '{' + f' {self._Deductions[0]}.'
        
        return s

    
    def is_KTO_solvable(self) -> bool:
        return math.lcm(*map(lambda t: t.get_MOD(),  self._Deductions)) == reduce(lambda x, y: x*y, map(lambda t: t.get_MOD(),  self._Deductions))
    

    def solve_KTO_1(self, explain:int = 0) -> Deduction | None:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        M = reduce(lambda x,y: x*y, map(lambda t: t.get_MOD(),  self._Deductions))
        Print(1, explain, f'Рассчитаем значение итогового модуля M, перемножив все модули.  {M=}.\n\nТеперь, для каждого сравнения ( {self._VAR} ≡ A (mod B) ) в системе вычислим:\n m = M/D;\n y как решение m•y ≡ 1 (mod B);\n c = A.\nА так же их произведение p.\n\n')
        x0 = 0
        for i, e in enumerate(self._Deductions, 1):
            m = M // e.get_MOD()
            c = e.get_A()
            Print(1, explain, f'#{i}  {e}\n')
            Print(1, explain, f'm{i} = {m};')
            Print(1, explain, f'c{i} = {c};')
            h = Comparison(m, 1, e.get_MOD(), f'y{i}')
            Print(1, explain, f'\nРешим {h}:\n')
            y: Deduction = h.to_Deduction()  # type: ignore
            y.normalise()
            Print(1, explain, y.express("t"))
            Print(1, explain, f'Отбросим часть с t.\n')
            Print(1, explain, f'y{i} = {y.get_A()};\n')
            p = m*c*y.get_A()
            Print(1, explain, f'p{i} = {p}.\n\n')
            x0 += p
        Print(1, explain, 'x0 = ∑ p{i}', f'= {x0}')
        Print(1, explain, f'x ≡ x0 ≡ {x0} (mod {M})\n')
        ans = Deduction(x0, M, self._VAR)
        ans.normalise()
        Print(2, explain, f'Ответ: ', end='')
        Print(3, explain, ans)
        return ans
    
    def solve_KTO_2(self, explain:int = 0) -> Deduction | None:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        ...
    
    def normalise(self) -> None:
        for i in self._Deductions:
            i.normalise()



