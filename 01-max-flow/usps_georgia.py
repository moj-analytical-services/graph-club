from copy import deepcopy

nodes = list(range(1, 53))
nodes.extend(['S', 'T'])

ud_edges_tuples = [
    ('T', 1  , 1200),
    ('T', 22 , 2500),
    ('T', 45 , 1000),
    ('T', 46 , 2000),
    
    (1  , 2 , 800 ),
    (2  , 15, 800),
    (15 , 3 , 600),
    (3  , 4 , 400),
    (4  , 16, 400),
    (4  , 5 , 400),
    (5  , 16, 400),
    (15 , 16, 1000),
    (16 , 17, 800),
    (5  , 6 , 400),
    (6  , 17, 400),
    (6  , 7 , 300),
    (7  , 18, 800),
    (15 , 17, 600),
    (16 , 24, 600),
    (17 , 18, 600),
    (17 , 30, 400),
    (24 , 30, 200),
    (7  , 8 , 400),
    (8  , 9 , 600),
    (9  , 10, 400),
    (19 , 10, 400),
    (8  , 19, 400),
    (19 , 17, 400),
    (10 , 26, 600),
    (17 , 26, 800),
    (9  , 19, 100),
    (10 , 11, 400),
    (11 , 12, 200),
    (12 , 20, 150),
    (20 , 21, 600),
    (11 , 27, 600),
    (26 , 27, 1000),
    (26 , 33, 800),
    (26 , 32, 400),
    (32 , 33, 100),
    (11 , 20, 100),
    (27 , 28, 600),
    (28 , 29, 800),
    (33 , 34, 600),
    (20 , 34, 400),
    (34 , 35, 800),
    (22 , 15, 300),
    (22 , 23, 800),
    (23 , 36, 1000),
    (36 , 37, 1200),
    (37 , 38, 1200),
    (38 , 39, 1100),
    (39 , 51, 2000),
    (39 , 40, 100),
    (24 , 36, 400),
    (36 , 30, 400), 
    (30 , 37, 150),
    (22 , 46, 200),
    (45 , 46, 1200),
    (46 , 47, 800),
    (46 , 48, 1500),
    (47 , 48, 200),
    (47 , 49, 800),
    (48 , 49, 800),
    (49 , 50, 600),
    (37 , 50, 100),
    (38 , 50, 100),
    (39 , 50, 600),
    (36 , 47, 400),
    (36 , 49, 350),
    
    (30, 25, 400),
    (25, 26, 600),
    (25, 31, 200),
    (31, 32, 100),
    (31, 42, 100),
    (31, 41, 100),
    (41, 40, 800),
    (41, 42, 600),
    (33, 42, 400),
    (32, 42, 400),
    
    (41, 52, 100),
    (40, 52, 100),
    (40, 51, 300),
    (52, 51, 900),
    (44, 52, 150),
    (43, 44, 200),
    (43, 34, 400),
    (44, 34, 300),
    
    (32, 42, 400),
    (32, 53, 200),
    
    (35, 29, 800),
    (13, 21, 150),
    (13, 14, 500),
    (14, 21, 200),
    
    (29, 'S', 2000),
    (14, 'S', 1400),
    (44, 'S', 200)
]


def tuple_to_nx(t: tuple) -> tuple:
    """Convert tuples above to NetworkX format of (u,v,data)
    Where data is a dictionary of k-v pairs."""
    return (t[0], t[1], {'capacity': t[2]})

ud_edges_nx = [tuple_to_nx(t) for t in ud_edges_tuples]

def reverse_edge(e: tuple) -> tuple:
    """Reverse an edge to double it up for use in a
    symmetric-weight directed graph made from a weighted
    undirected one."""
    (u, v, data) = e
    return (v, u, data)

dir_edges_nx = deepcopy(ud_edges_nx)
dir_edges_nx.extend([reverse_edge(e) for e in ud_edges_nx])

def check_dup_ud_edges_tuples():
    unweighted = [(u, v) for (u,v,w) in ud_edges_tuples]
    count = 0
    for (u, v) in unweighted:
        if (v, u) in unweighted:
            count += 0.5
        count += 1
    test = (len(unweighted) == count)
    print(f'{count} distinct edges defined; '
          f'{len(unweighted)} edges in list. Pass = {test}.')
    
if __name__ == '__main__':
    check_dup_ud_edges_tuples()
    print(f':::::::: {len(nodes)} nodes:')
    print(nodes)
    print('::::::::')
    print(f'{len(ud_edges_nx)} undirected edges convert to '
          f'{len(dir_edges_nx)} symmetric doubled directed edges.')
