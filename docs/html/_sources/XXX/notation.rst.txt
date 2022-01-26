Notation
========

.. list-table::
    :header-rows: 1
    :stub-columns: 1
    :align: center
    :widths: 20 30 50

    *   - .. centered:: Notation
        - .. centered:: Description
        - .. centered:: Formula
    *   - :math:`n!`
        - Factorial
        - .. math:: n! = n \cdot (n-1) \cdot (n-2) ... 3 \cdot 2 \cdot 1
    *   - .. math:: C_n^k
        - Binomial coefficient
        - .. math:: C_n^k = \frac{n!}{k!(n-k)!}
    *   - :math:`\phi(x)`
        - Probability density function of the standard normal distribution
        - .. math:: \phi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
    *   - :math:`\Phi(x)`
        - Cumulative distribution function of the standard normal distribution
        - .. math:: \Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-\frac{t^2}{2}} dt
    *   - :math:`\Gamma(x)`
        - Gamma function
        - .. math:: \Gamma(x) = \int_0^{\infty} t^{x-1} e^{-t} dt
    *   - :math:`\gamma(x,u)`
        - Lower incomplete gamma function
        - .. math:: \gamma(x,u) = \int_0^u t^{x-1} e^{-t} dt
    *   - :math:`\Gamma(x,u)`
        - Upper incomplete gamma function
        - .. math:: \Gamma(x,u) = \int_u^{\infty} t^{x-1} e^{-t} dt
    *   - :math:`B(\alpha,\beta)`
        - Beta function
        - .. math:: B(\alpha,\beta) = \int_0^1 t^{\alpha-1} (1-t)^{\beta-1} dt
    *   - :math:`B(x;\alpha,\beta)`
        - Incomplete beta function
        - .. math:: B(x;\alpha,\beta) = \int_0^x t^{\alpha-1} (1-t)^{\beta-1} dt