from graphviz import Digraph


def construct_tree_graph(tree, root):
    graph = Digraph('Tree', engine='neato')

    def draw_from_level(root, x, y, v_dist):
        label = str(root)
        graph.node(label, label='' if label.startswith('_') else label,
                   shape='circle', fixedsize='true', pos=f'{x},{y}!', width='0.5')

        if root in tree:
            left, right = tree[root]
            v_dist /= 2
            if left is not None:
                draw_from_level(left, x + x_delta[left], y - 1, v_dist)
                # I hate you python, and graphviz as well
                graph.edge(label, str(left))  # , label='0')
                graph.node(f"{label}_{left}", label="0", shape="plaintext",
                           pos=f'{x + x_delta[left] / 2 - 0.1},{y - 0.4}!', width='0.5')

            if right is not None:
                draw_from_level(right, x + x_delta[right], y - 1, v_dist)
                graph.edge(label, str(right))
                graph.node(f"{label}_{right}", label="1", shape="plaintext",
                           pos=f'{x + x_delta[right] / 2 + 0.1},{y - 0.4}!', width='0.5')

    x_delta = {root: 0.0}

    def compute_distances(root):
        if root not in tree:
            return [(0, 0)]
        left, right = tree[root]
        left_distances = compute_distances(left) if left is not None else []
        right_distances = compute_distances(right) if right is not None else []
        d = 0
        for (_, r), (l, _) in zip(left_distances, right_distances):
            d = max(d, r - l + 1)
        x_delta[left] = -d / 2
        x_delta[right] = d / 2

        depth2 = min(len(left_distances), len(right_distances))
        return [(0, 0)] + \
            [(l - d / 2, r + d / 2) for (l, _), (_, r) in zip(left_distances, right_distances)] + \
            [(l - d / 2, r - d / 2) for (l, r) in left_distances[depth2:]] + \
            [(l + d / 2, r + d / 2) for (l, r) in right_distances[depth2:]]

    compute_distances(root)
    draw_from_level(root, 0, 0, 0)

    return graph
