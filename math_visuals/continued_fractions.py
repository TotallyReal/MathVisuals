from typing import Callable

"""
See the google colab for examples:
https://colab.research.google.com/drive/1nQy1q_-6ik0ylvbXvW2jRzZkaLhLzMG5#scrollTo=5doyMuvjRm2t
"""


def frac(numerator, denominator):
    """
    LaTeX expression for fraction
    :param numerator:
    :param denominator:
    :return:
    """

    # Because of course python has no idea what \cfrac is .........
    # Why would I even expect otherwise?
    return rf'\frac{{{numerator}}}{{{denominator}}}'



def latex_CF(
        numerators: Callable, denominators: Callable, depth: int,
        final_str='', remove_final_denominator: bool=False) -> str:
    """
    Generates a LaTeX generalized continued fraction expression
    :param numerators:      A Callable from (at least) integer to a representable object (__repr__)
    :param denominators:    Same as numerator
    :param depth:           Depth of the continued fraction
    :param final_str:       The string to put in the bottom right corner of the continued fraction
                            (e.g. empty string, '+0', '+\ddots', etc.
    :param remove_final_denominator:  Keep or remove the final denominator
    :return:                A LaTex string for the continued fraction
    """
    if depth < 1:
        return ''
    final_a = '' if remove_final_denominator else str(numerators(depth))
    s = frac(denominators(depth), final_a + final_str)
    for i in range(depth - 1, 0, -1):
        s = frac(denominators(i), f'{numerators(i)}+{s}')
    return s
