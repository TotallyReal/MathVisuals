from math_visuals import continued_fractions as cf
from math_visuals.latex import latex_image, python_to_latex_conv

def a(x):
  return x**3 + (1+x)**3

def b(x):
  return -x**6

def test_only_numbers():
    latex_str = cf.latex_CF(numerators=a, denominators=b, depth=3, final_str='')
    assert latex_str == r'\frac{-1}{9+\frac{-64}{35+\frac{-729}{91}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot

    latex_str = cf.latex_CF(numerators=a, denominators=b, depth=3, final_str='+0')
    assert latex_str == r'\frac{-1}{9+\frac{-64}{35+\frac{-729}{91+0}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot

    latex_str = cf.latex_CF(numerators=a, denominators=b, depth=3, final_str='+\ddots')
    print(latex_str)
    assert latex_str == r'\frac{-1}{9+\frac{-64}{35+\frac{-729}{91+\ddots}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot


def a_poly(x):
  return f'{x}**3 + {1+x}**3'

def b_poly(x):
  return f'-{x}**6'

def test_func_of_n():

    latex_str = python_to_latex_conv(cf.latex_CF(numerators=a_poly, denominators=b_poly, depth=3, final_str=''))
    print(latex_str)
    assert latex_str == r'\frac{-1^6}{1^3\; +\; 2^3+\frac{-2^6}{2^3\; +\; 3^3+\frac{-3^6}{3^3\; +\; 4^3}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot

    latex_str = python_to_latex_conv(cf.latex_CF(numerators=a_poly, denominators=b_poly, depth=3, final_str='+0'))
    print(latex_str)
    assert latex_str == r'\frac{-1^6}{1^3\; +\; 2^3+\frac{-2^6}{2^3\; +\; 3^3+\frac{-3^6}{3^3\; +\; 4^3+0}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot

    latex_str = python_to_latex_conv(cf.latex_CF(numerators=a_poly, denominators=b_poly, depth=3, final_str='+\ddots'))
    print(latex_str)
    assert latex_str == r'\frac{-1^6}{1^3\; +\; 2^3+\frac{-2^6}{2^3\; +\; 3^3+\frac{-3^6}{3^3\; +\; 4^3+\ddots}}}'
    # latex_image(f'${latex_str}$')     # Use to print LaTeX using pyplot