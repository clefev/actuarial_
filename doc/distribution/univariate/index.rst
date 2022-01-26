Univariate
==========

.. toctree::
   :maxdepth: 1
   :hidden:
   
   Bernoulli.rst
   Beta.rst
   Exponential.rst
   Gamma.rst
   GeneralizedPareto.rst
   Lognormal.rst
   Normal.rst
   Pareto.rst
   Poisson.rst
   Uniform.rst
   Weibull.rst
   Empirical.rst
   Truncated.rst
   Mixture.rst

.. autoclass:: actuarial.distribution::UnivariateDistribution

    .. tabbed:: Initialization

        .. automethod:: __init__

    .. tabbed:: Abstract

        .. autoproperty:: dtype
        .. automethod:: cdf
        .. automethod:: pdf
        .. automethod:: quantile
        .. automethod:: random
        .. autoclass:: actuarial.distribution::UnivariateDistribution.Decorators
            :members:

    .. tabbed:: Properties

        |none|

    .. tabbed:: Methods

        .. automethod:: log_likelihood

    .. tabbed:: Special

        |none|

    .. tabbed:: Examples

        |none|