# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:53:03 2021

@author: lefev
"""

import time

class G:
     def __init__(self, age):
          self._age = age
       
     # using property decorator
     # a getter function
     @property
     def age(self):
         print("getter method called")
         return self._age
     
     @property
     def t(self):
         try:
             return self._t
         except:
             time.sleep(2)
             self._t = self.age + 1
             return self._t
       
     # a setter function
     @age.setter
     def age(self, a):             
         if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
         print("setter method called")
         del self._t
         self._age = a



class A:
    
    @property
    def _test(self):
        if "_test" in a.__dict__:
            return self._test
        else:
            setattr(self, "_test", 0)
            return self._test
        
# =============================================================================
#         try:
#             return self.test_
#         except AttributeError:
#             self.test_ = 0
#             return self.test_
# =============================================================================

         
   
         
         
         
import numpy as np

np.random.seed(1)
np.random.uniform(size=5)


rng = np.random.default_rng(2)
rng.uniform(size=2)

#

#

from scipy.optimize import minimize

l = []

def f(x):
    l.append(x.item())
    return x**2

def track(x):
    l.append(x.item())

minimize(f, 10)

#

def f(*args, **kwargs):
    return (args, kwargs)

args = ()
d = {}

for key, value in zip(d.keys(), args):
    print(key, value)

if args:
    print("ok")
    
# 

lamb = 5
size = 100
x = np.random.poisson(lamb, size=size)

def score(x, lamb):
    return x/lamb - 1

def fisher(x, lamb):
    return score(x, lamb)**2

lamb = x.mean()

print(score(x, lamb).sum(), x.sum()/lamb - size)
print(fisher(x, lamb).mean(), 1/lamb)

print(fisher(x, lamb).sum(), x.sum()/lamb**2, size**2/x.sum(), (x/lamb**2).sum())
print(1/fisher(x, lamb).sum(), 1/(x.sum()/lamb**2), x.sum()/size**2)

a = fisher(x, lamb)
b = x/lamb**2



import time
def f():
    time.sleep(.1)
def g():
    time.sleep(5)
x = None
y = f() if x is None else g()

x = False
1 if x is False else 1/0

# Bisection

from mathematics import bisection

def f(x, c = 0):
    return x**2 + c

lower=0
upper = [5, 4]
bisection(f, [0], [[5, 4], [3,3]], kwargs={"c": [[-4, -9], [-1, -2]]}, tol=0)


t0 = time.time_ns()
a=np.empty((10000000, 1000000, 555), dtype=[])
t1 = time.time_ns()
print(t1-t0)




class Test:
    def __init__(self, x):
        self.x = x
        

        
    def memorize(func):
        def wrapper(self):   
            name = "_" + func.__name__
            try:
                return getattr(self, name) # self._prop
            except AttributeError:
                setattr(self, name, func(self)) #self._prop = func(self)
                return getattr(self, name) # self._prop
            
        return wrapper
    
    @property
    @memorize
    def prop(self):
        print("...")
        return self.x + 1
    
    @property
    @memorize
    def prop2(self):
        print("...2")
        return self.x - 1
    
    def __str__(self):
        return "de"
    
t = Test(5)
t.prop


def test(*args):
    print(not args)
    
    
    
    
    
    
    
    
    
from superclasses import Base, Shock

class S1(Base, Shock):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self._y = 0
        
    @property
    def x(self):
        return 0
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    def m(self):
        return 0
        
class S2(Base, Shock):
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

shift = lambda value: value + 10

u = S2(1,2,3)
s = S1(0, u)
s.shock(v1=5, v2={"v3":99}, y=10)


import numpy as np
import mathematics as math
from scipy import optimize


c = 5#np.array([2,3,4,5]).reshape(2,2)
f = lambda x: np.exp(x) - c
df = lambda x: np.exp(x)
root = np.log(c)
tol=1e-14

math.bisection(f, -5, 5, tol=2e-12)
math.newton_raphson(f, df, 0, tol=tol)
optimize.bisect(f, -5, 5, full_output=True)
optimize.newton(f, c, df, tol=tol, full_output=True)


from superclasses import Base, Mixture

class Test(Base, Mixture):
    
    @Mixture.components.setter
    def components(self, value):
        self.a = 99
        self._components = value

m = Mixture("de", "eee", "2de", weights = [10,20,30])

for w, c in m:
    print(w+1, c)
    
    
    
    
    
    
    
import time
x = np.arange(int(1e6)).reshape(100,100,100) 
t0 = time.time_ns()
for i in range(100000):
    if x.ndim == 0:
        y = x[()]
t1 = time.time_ns()
print((t1-t0)*1e-9)



import numpy as np
import time
import util

def sum(x, axis = None, dtype = None, keepdims = False, skipna = False):
    
    if skipna:
        out = np.nansum(x, axis = axis, dtype = dtype, keepdims = keepdims)
    else:
        out = np.sum(x, axis = axis, dtype = dtype, keepdims = keepdims)
        
    if isinstance(out, np.ma.core.MaskedArray):
        return out.data
    else:
        return out  
    
def mean1(x, axis = None, dtype = None, keepdims = False, skipna = False):
    
    return sum(x, axis=axis, keepdims=keepdims, skipna=skipna) / util.count_nan(x, axis=axis, keepdims=keepdims, invert=True)

def mean2(x, axis = None, dtype = None, keepdims = False, skipna = False):
    
    if skipna:
        mean = np.nanmean(x, axis = axis, dtype = dtype, keepdims = keepdims)
    else:
        mean = np.mean(x, axis = axis, dtype = dtype, keepdims = keepdims)
        
    if isinstance(mean, np.ma.core.MaskedArray):
        return mean.data
    else:
        return mean  
    
rng = np.random.default_rng(0)
x = rng.uniform(0,100,1000000)
x[0:1000] = np.nan
x = x.reshape(1000,1000)
x = np.ma.masked_array(x, mask = (x > 70))
x.mask[-1,] = True
axis = 1
keepdims = True
skipna = False

t0 = time.time_ns()
for i in range(100):
    m1 = mean1(x, axis=axis, keepdims=keepdims, skipna=skipna)
t1 = time.time_ns()
for i in range(100):
    m2 = mean2(x, axis=axis, keepdims=keepdims, skipna=skipna)
t2 = time.time_ns()

print((t1-t0)*1e-9, (t2-t1)*1e-9)


with np.errstate(divide = "ignore", invalid = "ignore"):
    a=np.array(0)/np.array(0)



from superclasses import TermStructure, Base

class A(Base, TermStructure):
    x = 99
    
    @TermStructure.maturities.setter
    def maturities(self, value):
        self.x = 0
        TermStructure.maturities.fset(self, value) 

a = A([1,2,3], [[9,8,7]])


from abc import ABC, ABCMeta, abstractmethod

class Super(metaclass = ABCMeta):
    @abstractmethod
    def x(self, a):
        pass
    
class Ind:
    def x(self, a):
        return a
    
class SuperInd(Ind, Super):
    pass
    
class Child(SuperInd):
    pass
    
c=Child()
c.x(1)


class Super(metaclass = ABCMeta):
    
    def __init__(self, p):
        self._p = p
        
    @property
    @abstractmethod
    def p(self):
        return self._p
    
class Child(Super):
    
    