from c3pObject import *
import random;
class c3pRange(c3pObject):
    def __init__(self,*args,**kwargs):
        self.min = 0
        self.max = 1
    def sample(self):
        return random.uniform(self.min,self.max)
        