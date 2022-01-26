Copula
======

.. toctree::
   :maxdepth: 1
   :hidden:
   
   Clayton.rst
   Comonotonic.rst
   Countermonotonic.rst
   Gaussian.rst
   Independence.rst



The copula module provides all the tools needed to work with copulas.

.. panels::
    :column: col-12 col-sm-6 col-lg-3 text-center p-1

    :fa:`puzzle-piece,fa-4x`

    Use various built-in copulas
    ---
    :fa:`crosshairs,fa-4x`

    Calibrate your copulas
    ---
    :fa:`dice,fa-4x`

    Generate random samples
    ---
    :fa:`tools,fa-4x`

    Build your own copula classes



.. rubric:: Module description

The copula module can be easily imported from the actuarial package:

.. code-block:: python

    from actuarial import copula

Several classes are implemented in this module.

First, we can find an abstract class called `Copula`.
This abstract class allows building copula models in a standardized way and with various features pre-implemented.
Therefore, all copula models implemented in this package inherit from this abstract class.
Moreover, it also allows you to build and customize your own copula models (by inheriting from this abstract class).
Related documentation can be found below:

.. dropdown:: Copula

    .. autoclass:: actuarial.copula::Copula()

        .. tabbed:: Initialization

            .. automethod:: __init__

        .. tabbed:: Abstract

            .. autoproperty:: dim
            .. automethod:: cdf
            .. automethod:: pdf
            .. automethod:: random
            .. autoclass:: actuarial.copula::Copula.Decorators
                :members:

        .. tabbed:: Properties

            |none|

        .. tabbed:: Methods

            .. automethod:: log_likelihood

        .. tabbed:: Special

            .. automethod:: __len__
            
        .. tabbed:: Examples

            To be added.

Secondly, the module offers different copula models.
For example, it implements the Gaussian copula, the comonotonic copula, the Clayton copula, ...
All these models inherit from the `Copula` abstract class as described above.
In this way, they all share a common set of features (properties and methods) and they can be easily identified as a copula
(using Python's built-in functions `isinstance` or `issubclass`).
The following copula models are implemented in this module:

.. list-table::
    :header-rows: 1
    :align: center

    *   - .. centered:: Copula model
        - .. centered:: Parametric
    *   - :ref:`copula.Comonotonic`
        - .. centered:: |X|
    *   - :ref:`copula.Countermonotonic`
        - .. centered:: |X|
    *   - :ref:`copula.Independence`
        - .. centered:: |X|
    *   - :ref:`copula.Gaussian`
        - .. centered:: |V|
    *   - :ref:`copula.Clayton`
        - .. centered:: |V|