from math_visuals.graphs import construct_tree_graph
import PIL.Image
import io
import pytest

def test_tree_image_generation():
    tree = {
        '_0': (1, 2),
        1: (3, 4),
        2: (5, 6),
    }
    ll = 3
    rr = 5
    for i in range(3):
        tree[ll] = (f'a{i}', f'_b{i}')
        ll = f'_b{i}'
        tree[rr] = (f'c{i}', f'd{i}')
        rr = f'd{i}'

    graph = construct_tree_graph(tree, '_0')

    png_bytes = graph.pipe(format='png')
    image = PIL.Image.open(io.BytesIO(png_bytes))
    image.show()

    # to save the file use:
    # with open('tree.png', 'wb') as f:
    #     f.write(graph.pipe(format='png'))

    # In python notebooks, you can display the graph's image using:
    # from IPython.display import display_png
    # display_png(graph)
