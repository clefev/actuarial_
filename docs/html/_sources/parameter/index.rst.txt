Parameter
=========

.. toctree::
   :maxdepth: 1
   :hidden:
   
   Array.rst
   CorrelationMatrix.rst
   Scalar.rst



The parameter module provides all the tools needed to work with parameters.

.. panels::
    :column: col-12 col-sm-6 col-lg-3 text-center p-1

    :fa:`puzzle-piece,fa-4x`

    Use various built-in parameters
    ---
    :fa:`check-square,fa-4x`

    Set up controls and validate your parameters
    ---
    :fa:`object-group,fa-4x`

    Collect and centralize your parameters
    ---
    :fa:`tools,fa-4x`

    Build your own parameter classes



.. rubric:: Module description

The parameter module can be easily imported from the actuarial package:

.. code-block:: python

    from actuarial import parameter

Several classes are implemented in this module.

First, we can find an abstract class called `Parameter`.
This abstract class allows building parameter classes in a standardized way and with various features pre-implemented.
Therefore, all parameter classes implemented in this package inherit from this abstract class.
Moreover, it also allows you to build and customize your own parameter classes (by inheriting from this abstract class).
Related documentation can be found below:
  
.. dropdown:: Parameter

    .. autoclass:: actuarial.parameter::Parameter()

            .. tabbed:: Initialization

                |none|

            .. tabbed:: Abstract

                .. automethod:: control
                .. autoclass:: actuarial.parameter::Parameter.Decorators
                    :members:

            .. tabbed:: Properties

                .. autoattribute:: value

            .. tabbed:: Methods

                .. automethod:: broadcast
                .. automethod:: set
                .. automethod:: reset

            .. tabbed:: Special

                .. automethod:: __arithmetic__
                .. automethod:: __comparison__
                .. automethod:: __getitem__
                .. automethod:: __setitem__
                
            .. tabbed:: Examples

                To be added.


Secondly, the module offers different parameter classes.
For example, it implements scalar parameters, array parameters, correlation matrix parameters, ...
All these parameter classes inherit from the `Parameter` abstract class as described above.
In this way, they all share a common set of features (properties and methods) and they can be easily identified as a parameter
(using Python's built-in functions `isinstance` or `issubclass`).
The following parameter classes are implemented in this module:

    * :ref:`parameter.Scalar`
    * :ref:`parameter.Array`
    * :ref:`parameter.CorrelationMatrix`

Finally, the parameter module provides a `Parameters` class (with a "s" at the end).
This class represents a collection of parameters.
It is used to efficiently store and manage multiple parameters.
In particular, it allows easy storage, extraction and controls of several parameters.
The documentation of this class can be found below:

.. dropdown:: Parameters

    .. autoclass:: actuarial.parameter::Parameters()

            .. tabbed:: Initialization

                .. automethod:: __init__

            .. tabbed:: Abstract

                |none|

            .. tabbed:: Properties

                .. autoattribute:: shapes
                .. autoattribute:: values

            .. tabbed:: Methods

                .. automethod:: set
                .. automethod:: control
                .. automethod:: reset

            .. tabbed:: Special

                |none|

            .. tabbed:: Decorators

                |none|

            .. tabbed:: Examples

                To be added.
