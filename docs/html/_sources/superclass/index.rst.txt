Superclass
==========

.. toctree::
   :maxdepth: 1
   :hidden:

   Arithmetic.rst
   Base.rst
   Broadcast.rst
   Comparison.rst
   Dictionary.rst
   Mixture.rst
   Parametric.rst
   Piecewise.rst
   Random.rst
   TermStructure.rst



The superclass module provides all the tools needed to build advanced and standardized actuarial classes.

.. panels::
    :column: col-12 col-sm-6 col-lg-3 text-center p-1

    :fa:`puzzle-piece,fa-4x`

    Use various built-in superclasses
    ---
    :fa:`atom,fa-4x`

    Atom of all implemented actuarial classes
    ---
    :fa:`sitemap,fa-4x`

    High standardization
    ---
    :fa:`tools,fa-4x`

    Build your own actuarial classes



.. rubric :: What is a superclass ?

A superclass is a class that can be inherited by another class to implement functionality.
The purpose of superclasses is to benefit from a whole series of standardized features without any implementation effort.
Of course, a class can inherit from several superclasses at the same time in order to multiply and extend its functionalities.
Superclasses are therefore considered as the atoms used to build other classes in this package.
Most of the classes implemented in the actuarial package are indeed built from at least one superclass.

An example of superclass is the `Random` superclass.
The functionality of this superclass is to incorporate a random number generator as well as methods for working with it.
By inheritance, all classes inheriting from the `Random` superclass will also get the same functionality.
Therefore, if we want to create a class capable of generating randomness (e.g., for generating random samples of a given distribution, generating random brownian motion samples, ...),
this class should inherit from the `Random` superclass.
In this way, the implemented class will directly have access to a random number generator to generate randomness and the ability to manage it easily.



.. rubric:: Module description

The superclass module can be easily imported from the actuarial package:

.. code-block:: python

    from actuarial import superclass

This module contains several superclasses.
Each superclass has its own functionality.
The table below provides a short description of the implemented superclasses (in alphabetical order):

.. list-table::
    :header-rows: 1
    :align: center

    *   - .. centered:: Superclass
        - .. centered:: Description
    *   - :ref:`superclass.Arithmetic`
        - Describe how arithmetic operators (`+`, `-`, `*`, `/` and `**`) should behave on the instance
    *   - :ref:`superclass.Base`
        - Nice formatting when printing the instance and basic methods such as copy instance
    *   - :ref:`superclass.Broadcast`
        - Mimic how input arguments are broadcast with an instance and provide a `shape`, `ndim` and `size` attributes
    *   - :ref:`superclass.Comparison`
        - Describe how comparison operators (`==`, `!!=`, `<`, `>`, `<=` and `>=`) should behave on the instance
    *   - :ref:`superclass.Dictionary`
        - Build a dictionary of key-component pairs
    *   - :ref:`superclass.Mixture`
        - Build mixture models (containing components and weights)
    *   - :ref:`superclass.Parametric`
        - Build parametric models (containing parameters)
    *   - :ref:`superclass.Piecewise`
        - Build piecewise models (containing a piecewise function)
    *   - :ref:`superclass.Random`
        - Build random models (containing a random number generator and capable of generating randomness)
    *   - :ref:`superclass.TermStructure`
        - Build term structure models (containing values associated with maturities)

Note that the `Base` superclass is the most common.
It is good practice to inherit actuarial classes from this superclass.