.. _distribution.Gamma:

Gamma
=====

.. autoclass:: actuarial.distribution::Gamma()

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
                - Gamma (shifted)
            *   - Notation
                - :math:`X \sim A + Gam(\alpha, \beta)`
            *   - Parameters
                - | `shape` = :math:`\alpha > 0`
                  | `rate` = :math:`\beta > 0`
                  | `min` = :math:`A \in \mathbb{R}` (location/shift)
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.