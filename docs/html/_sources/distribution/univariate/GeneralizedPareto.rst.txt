.. _distribution.GeneralizedPareto:

Generalized Pareto
==================

.. autoclass:: actuarial.distribution::GeneralizedPareto()

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
                - Generalized Pareto
            *   - Notation
                - :math:`X \sim GPD(A, \xi, \sigma)`
            *   - Parameters
                - | `min` = :math:`A \in \mathbb{R}` (location/shift)
                  | `shape` = :math:`\xi > 0`
                  | `scale` = :math:`\sigma > 0`
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.