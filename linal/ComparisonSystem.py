from .Comparison import Comparison
from .Deduction import Deduction
from .Print import Print, CheckFlag
from .DeductionSystem import DeductionSystem

 
class ComparisonSystem:
    def __init__(self, *comps:Comparison, var:str = 'x') -> None:
        self._VAR = var
        [i.set_VAR(var) for i in comps if i.get_VAR() != var]
        self._Comparisons: list[Comparison] = sorted(comps, key=lambda x: x.get_MOD())
    
    def __str__(self) -> str:
        if (l := len(self._Comparisons)) >= 3:
            s1 = '⎧ ' + ';\n⎪ '.join(map(str, self._Comparisons)) + '.'
            ss = s1.split('\n')
            ss[-1] = '⎩' + ss[-1][1:]
            ss[l//2] = '⎨' + ss[l//2][1:]
            s = '\n'.join(ss)
        elif l == 2:
            s = f'⎰ {self._Comparisons[0]};\n⎱ {self._Comparisons[1]}.'
        else:
            s = '{' + f' {self._Comparisons[0]}.'
        
        return s
    
    
    def is_normalised(self):
        return all([i.is_normalised() for i in self._Comparisons])
    
    
    def to_deduction_system(self, explain:int = 0) -> DeductionSystem | None:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        if not self.is_normalised():
            Print(1, explain, '\nНормализуем сравнения, где это нужно:\n')
            self.normalise()
            Print(1, explain, self, '\n')
        if any([i.get_A() != 1 for i in self._Comparisons]):
            Print(1, explain, f'Разрешим сравнения с коэфициентами перед {self._VAR}:')
        
        ds: list[Deduction] = []
        for i in self._Comparisons:
            if i.get_A() != 1:
                Print(1, explain, '#', i)
                d = i.to_Deduction(explain_new)
                if d is None:
                    return
                ds.append(d)
                Print(1, explain, f'\n{d}\n')
            else:
                d = Deduction(i.get_B(), i.get_MOD(), var=self._VAR)
                ds.append(d)
        return DeductionSystem(*ds, var=self._VAR)
    
    def normalise(self) -> None:
        for i in self._Comparisons:
            i.normalise()
    
    def solve_KTO(self, explain:int = 0) -> Deduction | None:
        explain_new = explain - (2 if CheckFlag(2, explain) else 0)
        
        if CheckFlag(1, explain):
            print('Каким алгоритмом желаете воспользоваться?\n1 или 2')
            alg = int(input('--> '))
            if alg not in [1,2]:
                raise ValueError(f'Wrong algorythm.')
        
        Print(1, explain, f'\nРешить систему сравнений:\n\n{self}')
        wdn = self.is_normalised()
        ds = self.to_deduction_system(explain_new)
        if any([i.get_A() != 1 for i in self._Comparisons]) or not wdn:
            Print(1, explain, 'Промежуточный итог:\n\n', ds, '\n', sep='')
        del wdn
        if ds is None:
            Print(2, explain, 'Ответ: ', end='')
            Print(3, explain, f'Данную систему не решить с помощью КТО. Невозможно привести все сравнения в вид без коэфициентов перед {self._VAR}.')
            return
        if not ds.is_KTO_solvable():
            Print(2, explain, 'Ответ: ', end='')
            Print(3, explain, f'Данную систему не решить с помощью КТО. Не все модули взаимнопросты.')
        
        if alg == 1:
            ds.solve_KTO_1(explain_new +2)
        elif alg == 2:
            ds.solve_KTO_2(explain_new)
        





