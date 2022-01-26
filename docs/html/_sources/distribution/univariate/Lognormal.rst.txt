.. _distribution.Lognormal:

Lognormal
=========

.. autoclass:: actuarial.distribution::Lognormal()

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
                - Lognormal (shifted)
            *   - Notation
                - :math:`X \sim A + LN(\mu, \sigma^2)`
            *   - Parameters
                - | `mean_log` = :math:`\mu \in \mathbb{R}`
                  | `std_log` = :math:`\sigma > 0`
                  | `min` = :math:`A \in \mathbb{R}` (location/shift)
            *   - Support
                - :math:`S = [A,+\infty)`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.