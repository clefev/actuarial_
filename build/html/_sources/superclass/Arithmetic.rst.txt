.. _superclass.Arithmetic:

Arithmetic
==========

.. autoclass:: actuarial.superclass::Arithmetic()

    .. tabbed:: Initialization

        |none|

    .. tabbed:: Abstract

        .. automethod:: __arithmetic__

    .. tabbed:: Properties

        |none|

    .. tabbed:: Methods

        |none|

    .. tabbed:: Special

        .. automethod:: __add__
        .. automethod:: __mul__
        .. automethod:: __pow__
        .. automethod:: __sub__
        .. automethod:: __truediv__
        .. automethod:: __radd__
        .. automethod:: __rmul__
        .. automethod:: __rpow__
        .. automethod:: __rsub__
        .. automethod:: __rtruediv__

    .. tabbed:: Examples
        
        Import the `Arithmetic` superclass.
        
        .. code-block:: python
        
            from actuarial.superclass import Arithmetic
            
        Create a class `Example` inheriting from the Arithmetic superclass and
        having an `amount` attribute representing a number.
        The application of arithmetic operators on the instance (`+`, `-`, `*`, `/` and `**`)
        should return the result of this arithmetic operator applied on the `amount`
        attribute of the instance.
            
        .. code-block:: python
            
            class Example(Arithmetic):
            
                def __init__(self, amount: float):
                    self.amount = float(amount)
                    
                def __arithmetic__(self, value, operator):
                    return operator(self.amount, value) # return the result of the arithmetic operator applied on the 'amount' attribute of the instance
                    
        If the application of an arithmetic operator on the instance should return
        the result through a new instance instead, the `__arithmetic__` method could
        be defined as
        
        .. code-block:: python
        
            def __arithmetic__(self, value, operator):
                return Example(amount = operator(self.amount, value)) # return a new instance containing the result of the arithmetic operator applied on the 'amount' attribute of the existing instance