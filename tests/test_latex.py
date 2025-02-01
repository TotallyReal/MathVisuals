from math_visuals.latex import matrix_latex

def test_matrix():
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    assert matrix_latex((matrix)) == r'\begin{pmatrix}1&2&3&4\\5&6&7&8\\9&10&11&12\end{pmatrix}'

def test_matrix_image():
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]