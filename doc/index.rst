.. actuarial documentation master file, created by
   sphinx-quickstart on Tue Sep 21 10:16:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to actuarial's documentation!
=====================================

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Test
   
   hello.rst
   test.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: SUPERCLASS
   
   superclass/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: PROBABILITY & STATISTICS
   
   distribution/index.rst
   copula/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: FIXED INCOME

   fixed_income/index.rst
   yield_curve/index.rst
   indexation/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: NON-LIFE

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: LIFE & HEALTH

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: MATHEMATICS

   math/index.rst
   parameter/index.rst
   function/index.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: UTILITIES

   aggregation/index.rst
   util/util.rst

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: XXX

   XXX/notation.rst


The actuarial package is a Python package dedicated to actuarial science and risk management.

.. panels::
   :column: col-12 col-lg-10 text-center p-2

   ACTUARIAL MODELLING

   :fa:`chart-line,fa-4x`

   The actuarial package implements various models and tools for actuarial science and risk management.
   It covers several topics such as yield curves, fixed incomes, distributions, copulas, quantitative finance, ALM, life insurance, non-life insurance and health insurance.
   ---
   EASY TO USE

   :fa:`code,fa-4x`

   The package is designed to facilitate the use of actuarial models and tools.
   Its high level syntax makes it accessible and productive for programmers and actuaries from any background or experience level.
   An extensive documentation and various concrete examples accompany this package.
   ---
   TRANSPARENT

   :fa:`eye,fa-4x`

   The code is fully transparent and well documented.
   It is accessible from this documentation or can be downloaded from the dedicated Github repository.
   It provides best practices for programming, building and documenting actuarial models.
   ---
   PERFORMANT

   :fa:`stopwatch,fa-4x`

   The actuarial package is optimized for computation times.
   The calculations are based on the numpy framework and take full advantage of vectorization.
   ---
   HIGH STANDARDIZATION

   :fa:`industry,fa-4x`

   The code relies on an object-oriented framework where the concepts of class and inheritance are widely used.
   The high level classes implemented in this package allow the standardization and industrialization of all actuarial models.
   They can also serve as toolkits to create and customize your own actuarial models.

.. Ajouter la modularité ?



Objective
---------

The actuarial package was built on the basis of an observation: the actuarial tools implemented in companies are often
outdated, difficult to use, poorly documented and not optimized.

This package aims to be the fundamental high-level building block for actuarial and risk management modelling in Python.
It is designed based on a set of best practices:

   * Easy to use
   * Fast
   * Robust
   * Well documented
   * Powerful
   * Modular

Therefore, it should serve as a reference for all actuaries, programmers and students who want to code actuarial tools.



Package content
---------------

The actuarial package is divided into different modules to facilitate its use and separate its functionalities.
A module generally contains a set of classes and/or functions.
The table below provides an overview of the modules implemented in the actuarial package (in alphabetical order):

.. list-table::
   :header-rows: 1
   :align: center

   *  - .. centered:: Module name
      - .. centered:: Description
   *  - `copula`
      - Tools for working with copulas
   *  - `distribution`
      - Tools for working with probability distribution (discrete or continuous, univariate or multivariate)
   *  - `indexation`
      - Tools for working with indexation and inflation
   *  - `yield_curve`
      - Tools for working with yield curves



How to use the documentation ?
------------------------------

Documentation is just as important as code.
A good documentation is important to clearly understand how the code works and all the features offered.
For actuarial science, the documentation should also help actuaries and programmers to make the connection between theory
(the mathematics and formulas behind an actuarial model) and code (its implementation in practice).
In addition, concrete examples should illustrate how the code works.

The actuarial package being divided into different modules, a documentation is associated with each module.
The documentation of a module is accessible via the sidebar on the left.
It provides:

   * A global overview of the module (description, content and code structure).
   * A detailed documentation for each class and function implemented in the module.
   * Links to the code.
   * Concrete examples.
   * Theoretical reminders on models and formulas.

A search bar in the upper left corner also allows you to do custom searches.
For example, you can type "nelson siegel" to find the documentation associated with the Nelson-Siegel model.