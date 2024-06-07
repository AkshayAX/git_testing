import numpy as np
from typing import List

# comments added
class calculation:
    def __init__(self,input_array:List):
        self.inputs = input_array
    
    def get_sum(self):
        return np.sum(self.inputs)

calc = calculation([3,4,5])
print(calc.get_sum())