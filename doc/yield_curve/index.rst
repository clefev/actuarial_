Yield Curve
===========

.. toctree::
   :maxdepth: 1
   :hidden:
   
   Flat.rst
   NelsonSiegel.rst
   LinearInterpolation.rst
   RawInterpolation.rst
   Mixture.rst

   

The yield curve module provides all the tools needed to work with yield curves.

.. panels::
    :column: col-12 col-sm-6 col-lg-3 text-center p-1

    :fa:`puzzle-piece,fa-4x`

    Use various built-in yield curves
    ---
    :fa:`crosshairs,fa-4x`

    Calibrate your yield curves
    ---
    :fa:`sync-alt,fa-4x`

    Easy conversion to discount factors
    ---
    :fa:`tools,fa-4x`

    Build your own yield curve classes



.. rubric:: Module description

The yield curve module can be easily imported from the actuarial package:

.. code-block:: python

    from actuarial import yield_curve

Several classes are implemented in this module.

First, we can find an abstract class called `YieldCurve`.
This abstract class allows building yield curve models in a standardized way and with various features pre-implemented.
Therefore, all yield curve models implemented in this package inherit from this abstract class.
Moreover, it also allows you to build and customize your own yield curve models (by inheriting from this abstract class).
Related documentation can be found below:

.. dropdown:: YieldCurve

    .. autoclass:: actuarial.yield_curve::YieldCurve()

        .. tabbed:: Initialization

            .. automethod:: __init__

        .. tabbed:: Abstract

            .. automethod:: evaluate
            .. autoclass:: actuarial.yield_curve::YieldCurve.Decorators
                :members:

        .. tabbed:: Properties

            .. autoattribute:: kind

        .. tabbed:: Methods

            .. automethod:: convert
            .. automethod:: discount_factor
            .. automethod:: capitalization_factor
            .. automethod:: to_discounting
            .. automethod:: fit

        .. tabbed:: Special

            .. automethod:: __call__

        .. tabbed:: Examples

            To be added.

Secondly, the module offers different yield curve models.
For example, it implements the flat yield curve model, the Nelson-Siegel model, the linearly interpolated yield curve, ...
All these models inherit from the `YieldCurve` abstract class as described above.
In this way, they all share a common set of features (properties and methods) and they can be easily identified as a yield curve
(using Python's built-in functions `isinstance` or `issubclass`).
The following yield curve models are implemented in this module:

.. list-table::
    :header-rows: 1
    :align: center

    *   - .. centered:: Yield curve model
        - .. centered:: Parametric
        - .. centered:: Interpolation
    *   - :ref:`yield_curve.Flat`
        - .. centered:: |V|
        - .. centered:: |X|
    *   - :ref:`yield_curve.NelsonSiegel`
        - .. centered:: |V|
        - .. centered:: |X|
    *   - :ref:`yield_curve.LinearInterpolation`
        - .. centered:: |X|
        - .. centered:: |V|
    *   - :ref:`yield_curve.RawInterpolation`
        - .. centered:: |X|
        - .. centered:: |V|
    *   - :ref:`yield_curve.Mixture`
        - .. centered:: |X|
        - .. centered:: |X|

Finally, the yield curve module provides a `Discounting` class.
This class is used to efficiently manage discount values such as compound rates, continuously compounded rates,
simple rates, discount factors and capitalization factors.
In particular, it allows easy conversion from one type to another, for example, to convert compound rates into discount factors,
simple rates into continuously compounded rates, ...
The documentation of this class can be found below:

.. dropdown:: Discounting

    .. autoclass:: actuarial.yield_curve::Discounting()

        .. tabbed:: Initialization

            .. automethod:: __init__

        .. tabbed:: Abstract

            |none|

        .. tabbed:: Properties

            .. autoattribute:: maturities1
            .. autoattribute:: maturities2
            .. autoattribute:: maturities
            .. autoattribute:: values
            .. autoattribute:: kind

        .. tabbed:: Methods

            .. automethod:: broadcast
            .. automethod:: convert

        .. tabbed:: Special

            .. automethod:: __arithmetic__
            .. automethod:: __comparison__

        .. tabbed:: Decorators

            |none|

        .. tabbed:: Examples

            To be added.