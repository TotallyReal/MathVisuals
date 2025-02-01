from typing import List
from IPython.display import Math, display
import matplotlib.pyplot as plt
import matplotlib

# Runtime Configuration Parameters
matplotlib.rcParams["mathtext.fontset"] = "cm"

def latex_print(s: str):
  display(Math(s.replace(' ','\; ').replace('**','^').replace('*','\cdot ')))

# -------------------- vectors and matrices --------------------

def vec_latex(vec:List[float], column=True):
  sep = '\\\\' if column else '&'
  vec_with_newlines = sep.join(str(num) for num in vec)
  return f'\\begin{{pmatrix}}{vec_with_newlines}\\end{{pmatrix}}'

def vec_list_latex(vec_list: List[List[float]]):
  return ','.join(vec_latex(vec) for vec in vec_list)

def matrix_latex(matrix):
  inside_matrix = '\\\\'.join(
      '&'.join(str(elem) for elem in row)
      for row in matrix)
  return f'\\begin{{pmatrix}}{inside_matrix}\\end{{pmatrix}}'

def latex_image(latex_expression:str):
    fig = plt.figure(figsize=(3, 0.5))  # Dimensions of figsize are in inches
    text = fig.text(
        x=0.5,  # x-coordinate to place the text
        y=0.5,  # y-coordinate to place the text
        s=latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=20,
    )

    plt.show()



