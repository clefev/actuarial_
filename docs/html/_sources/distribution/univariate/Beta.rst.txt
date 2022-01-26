.. _distribution.Beta:

Beta
====

.. autoclass:: actuarial.distribution::Beta()

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
                - Beta (four-parameters)
            *   - Notation
                - :math:`X \sim Beta(\alpha,\beta,a,b)`
            *   - Parameters
                - | `shape1` = :math:`\alpha > 0`
                  | `shape2` = :math:`\beta > 0`
                  | `min` = :math:`a \in \mathbb{R}`
                  | `max` = :math:`b \in \mathbb{R}`
            *   - Support
                - :math:`S = [a,b]`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.