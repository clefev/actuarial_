.. _distribution.Weibull:

Weibull
=======

.. autoclass:: actuarial.distribution::Weibull()

    .. tabbed:: Initialization

        .. automethod:: __init__

    .. tabbed:: Properties

        |none|

    .. tabbed:: Methods

        .. automethod:: pdf
        .. automethod:: cdf
        .. automethod:: quantile
        .. automethod:: random

    .. tabbed:: Special

        |none|

    .. tabbed:: Technical sheet

        .. list-table::
            :stub-columns: 1
            :align: center
            :widths: 20 80

            *   - Distribution name
                - Weibull (shifted)
            *   - Notation
                - :math:`X \sim A + Wei(\lambda, k)`
            *   - Parameters
                - | `scale` = :math:`\lambda > 0`
                  | `shape` = :math:`k > 0`
                  | `min` = :math:`A \in \mathbb{R}` (location/shift)
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.