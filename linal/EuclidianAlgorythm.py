from .Print import Print, Mask, CheckFlag


class EuclidianAlgorythm:
    def __init__(self, a: int, b: int) -> None:
        self._step_nums: list[int] = []
        self._key_nums: list[int] = []
        self._swapped = False
        
        if b > a:
            a,b = b,a
            self._swapped = True
        
        self._key_nums.append(a)
        self._key_nums.append(b)
        while self._key_nums[-1] != 0:
            k, r = divmod(self._key_nums[-2], self._key_nums[-1])
            self._step_nums.append(k)
            self._key_nums.append(r)
    
    def __str__(self) -> str:
        return f'({self._key_nums[self._swapped]}, {self._key_nums[1-self._swapped]})'
    
    
    def get_gcd(self, explain:int = 0) -> int:
        Print(1, explain, ';\n'.join([f'{self._key_nums[i]} = {self._step_nums[i]}•{self._key_nums[i+1]}{" + " + str(self._key_nums[i+2]) if self._key_nums[i+2] != 0 else ""}' for i in range(len(self._step_nums))]) + '.')
        Print(3, explain, f'\n{self} = {self._key_nums[-2]}.')
        return self._key_nums[-2]
    
    def get_linear_gcd_form(self, explain:int = 0) -> tuple[int, int]:
        s = str(self.get_gcd()) if Mask(3, explain) else ""
        kp = 1
        kn = self._step_nums[-2] if len(self._step_nums) >= 2 else 0
        for i1_ind, i2_step in enumerate(range(3, len(self._key_nums)), 4):
            if Mask(1, explain): s += f' = {kp}•{self._key_nums[-i1_ind + i1_ind%2]} - {kn}•{self._key_nums[-i2_step - i1_ind%2]}'
            if i2_step <= len(self._step_nums):
                if i1_ind%2:
                    if Mask(1+4, explain): s += f' = {kp}(1•{self._key_nums[-i2_step - i1_ind%2 - 1]} - {self._step_nums[-i2_step]}•{self._key_nums[-i2_step - i1_ind%2]}) - {kn}•{self._key_nums[-i2_step - i1_ind%2]}'
                    kn += kp * self._step_nums[-i2_step]
                else:
                    if Mask(1+4, explain): s += f' = {kp}•{self._key_nums[-i1_ind + i1_ind%2]} - {kn}(1•{self._key_nums[-i1_ind + i1_ind%2 - 1]} - {self._step_nums[-i2_step]}•{self._key_nums[-i1_ind + i1_ind%2]})'
                    kp += kn * self._step_nums[-i2_step]
            else: break
        else:
            if Mask(1, explain): s += f' = {kp}•{self._key_nums[1]} - {kn}•{self._key_nums[0]}'
        if Mask(2, explain) and not CheckFlag(1, explain): s += f' = {kp}•{self._key_nums[1]} - {kn}•{self._key_nums[0]}'
        if Mask(3, explain): s += '.'
        kn = -kn
        if self._swapped ^ len(self._step_nums)%2: kn, kp = kp, kn
        
        Print(3, explain, s)
        return kp, kn
    
    