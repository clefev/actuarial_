.. _distribution.Normal:

Normal
======

.. autoclass:: actuarial.distribution::Normal()

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
                - Normal/Gaussian
            *   - Notation
                - :math:`X \sim N(\mu, \sigma^2)`
            *   - Parameters
                - | `mean` = :math:`\mu \in \mathbb{R}` (location)
                  | `std` = :math:`\sigma > 0` (scale)
            *   - Support
                - :math:`S = \mathbb{R}`
            *   - Properties
                - 

    .. tabbed:: Examples

        To be added.