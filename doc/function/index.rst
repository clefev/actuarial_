.. _function:

Function
========

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   Constant.rst
   Linear.rst
   Logarithm.rst
   Exponential.rst
   PiecewiseFunction.rst

.. autoclass:: actuarial.function::Function

    .. rubric:: Abstract methods
    .. automethod:: evaluate
    .. automethod:: derivative
    .. automethod:: integrate

    .. rubric:: Decorators
    .. autoclass:: actuarial.function::Function.Decorators
        :members:

    .. rubric:: Special methods
    .. automethod:: __call__
