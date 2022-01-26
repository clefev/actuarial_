Indexation
==========

.. toctree::
   :maxdepth: 1
   :hidden:

   Flat.rst
   PriceIndex.rst



The indexation module provides all the tools needed to work with indexation and deal with inflation.

.. panels::
    :column: col-12 col-sm-6 col-lg-3 text-center p-1

    :fa:`puzzle-piece,fa-4x`

    Use various built-in indexations
    ---
    :fa:`search-dollar,fa-4x`

    Manage and determine inflation
    ---
    :fa:`sync-alt,fa-4x`

    Easy conversion to discount factors
    ---
    :fa:`tools,fa-4x`

    Build your own indexation classes



.. rubric:: Module description

The indexation module can be easily imported from the actuarial package:

.. code-block:: python

    from actuarial import indexation

Several classes are implemented in this module.
   
First, we can find an abstract class called `Indexation`.
This abstract class allows building indexation models in a standardized way and with various features pre-implemented.
Therefore, all indexation models implemented in this package inherit from this abstract class.
Moreover, it also allows you to build and customize your own indexation models (by inheriting from this abstract class).
Related documentation can be found below:

.. dropdown:: Indexation

    .. autoclass:: actuarial.indexation::Indexation()

        .. tabbed:: Initialization

            .. automethod:: __init__

        .. tabbed:: Abstract

            .. automethod:: price_index
            .. autoclass:: actuarial.indexation::Indexation.Decorators
                :members:

        .. tabbed:: Properties

            |none|

        .. tabbed:: Methods

            .. automethod:: discount_factor
            .. automethod:: capitalization_factor
            .. automethod:: inflation
            .. automethod:: to_discounting

        .. tabbed:: Special

            .. automethod:: __call__
            
        .. tabbed:: Examples

            To be added.

Secondly, the module offers different indexation models.
It implements the flat indexation model (constant inflation) and the indexation based on a given price index.
All these models inherit from the `Indexation` abstract class as described above.
In this way, they all share a common set of features (properties and methods) and they can be easily identified as an indexation
(using Python's built-in functions `isinstance` or `issubclass`).
The following indexation models are implemented in this module:

.. list-table::
    :header-rows: 1
    :align: center

    *   - .. centered:: Indexation model
        - .. centered:: Parametric
    *   - :ref:`indexation.Flat`
        - .. centered:: |V|
    *   - :ref:`indexation.PriceIndex`
        - .. centered:: |X|