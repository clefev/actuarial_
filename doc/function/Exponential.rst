.. _function.Exponential:

Exponential
===========

.. autoclass:: actuarial.function::Exponential()

    .. tabbed:: Initialization

        .. automethod:: __init__

    .. tabbed:: Technical sheet

        +----------------------+--------------------------------------------------------------------------------+
        |**Form**              |:math:`f(x) = ae^{bx} + c`                                                      |
        +----------------------+--------------------------------------------------------------------------------+
        |**Parameters**        || `scale` = :math:`a \in \mathbb{R}`                                            |
        |                      || `rate` = :math:`b \in \mathbb{R}`                                             |
        |                      || `shift` = :math:`c \in \mathbb{R}`                                            |
        +----------------------+--------------------------------------------------------------------------------+
        |**Domain**            |:math:`\mathbb{R}`                                                              |
        +----------------------+--------------------------------------------------------------------------------+
        |**Range**             || :math:`(c, +\infty)` if :math:`a > 0`                                         |
        |                      || :math:`(-\infty, c)` if :math:`a < 0`                                         |
        +----------------------+--------------------------------------------------------------------------------+
        |**Properties**        |                                                                                |
        +----------------------+--------------------------------------------------------------------------------+
        |**Other comments**    |                                                                                |
        +----------------------+--------------------------------------------------------------------------------+
        
    .. tabbed:: Properties

        |none|

    .. tabbed:: Methods

        .. automethod:: evaluate
        .. automethod:: derivative
        .. automethod:: integrate

    .. tabbed:: Special

        |none|

    .. tabbed:: Examples

        To be added.
