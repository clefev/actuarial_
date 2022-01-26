.. _superclass.Comparison:

Comparison
==========

.. autoclass:: actuarial.superclass::Comparison()

    .. tabbed:: Initialization

        |none|

    .. tabbed:: Abstract

        .. automethod:: __comparison__

    .. tabbed:: Properties

        |none|

    .. tabbed:: Methods

        |none|

    .. tabbed:: Special

        .. automethod:: __eq__
        .. automethod:: __ge__
        .. automethod:: __gt__
        .. automethod:: __le__
        .. automethod:: __lt__
        .. automethod:: __ne__

    .. tabbed:: Examples
    
        Import the `Comparison` superclass.
        
        .. code-block:: python
        
            from actuarial.superclass import Comparison
            
        Create a class `Example` inheriting from the Comparison superclass and
        having an `amount` attribute representing a number.
        The application of comparison operators on the instance (`==`, `!!=`, `<`, `>`, `<=` and `>=`)
        should return the comparison with the `amount` attribute of the instance.
            
        .. code-block:: python
            
            class Example(Comparison):
            
                def __init__(self, amount: float):
                    self.amount = float(amount)
                    
                def __comparison__(self, value, operator):
                    return operator(self.amount, value) # return the comparison with the 'amount' attribute of the instance