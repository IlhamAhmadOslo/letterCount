# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 19:36:41 2021

@author: Eier
"""
class Animal:
    def __init__(self, age):
        
        if age == 0:
            self.a = 0
        else:
            self.a = age
        self.a += 10
    def paytho_kalb(self):
        
        return self.a
       
        
        
    
class Animal2: 
    def __init__(self, age=None):
        self.a = 0 if age is None else age
        #return self.a
        self.spicies= 'Human'
        self.t= 100
        
    def fitness(self):
        fitness=0
        if self.a >= 10:
            fitness+=5
        self.phi= fitness
        return self.phi        
        

import random
c = random.gauss(1.5, 8)


kanskje={'l':1,'g':5, 'w':3, 'la la ':9}
class prove:
    default_params={'ø':1,'g':5, 'w':3, 'Mmm':5 }
    @classmethod
    def set_params(cls, new_params):
        for key in new_params:
            if key not in cls.default_params.keys():
                raise KeyError('Invalid parameter name: ' + key)
            else:
                raise  'Det er ok din idiot'
    def __init__(self):
        pass
    def f(self):
        self.t= self.l + self.g
   # @classmethod           
    #def get_params(cls):

        #return cls.default_params
        
        
        
        
def g(a):
    a += 2
    return random.random() < a
            
        

def mo(t, b):
    birth = 0
    if t<= 2 or \
            b <= 2:
        birth= 15
    else:
        birth= 0
    return birth
    
res=[]    
for _ in range(10):
    mom=mo(1,3)
    res.append(mom)
    
    
    
t= [v for v in range(0,10)]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
