.. _distribution.Exponential:

Exponential
===========

.. autoclass:: actuarial.distribution::Exponential()

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
                - Exponential (shifted)
            *   - Notation
                - :math:`X \sim A + Exp(\lambda)`
            *   - Parameters
                - | `scale` = :math:`\lambda > 0`
                  | `min` = :math:`A \in \mathbb{R}` (location/shift)
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.