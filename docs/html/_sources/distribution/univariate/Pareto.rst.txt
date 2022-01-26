.. _distribution.Preto:

Pareto
======

.. autoclass:: actuarial.distribution::Pareto()

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
                - Pareto
            *   - Notation
                - :math:`X \sim Par(A, \alpha)`
            *   - Parameters
                - | `min` = :math:`A > 0` (scale)
                  | `shape` = :math:`\alpha > 0`
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.