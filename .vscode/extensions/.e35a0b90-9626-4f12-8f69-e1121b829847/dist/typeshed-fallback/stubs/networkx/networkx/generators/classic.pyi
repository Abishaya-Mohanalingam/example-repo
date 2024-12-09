from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def full_rary_tree(r, n, create_using: Incomplete | None = None): ...
@_dispatchable
def balanced_tree(r, h, create_using: Incomplete | None = None): ...
@_dispatchable
def barbell_graph(m1, m2, create_using: Incomplete | None = None): ...
@_dispatchable
def binomial_tree(n, create_using: Incomplete | None = None): ...
@_dispatchable
def complete_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def circular_ladder_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def circulant_graph(n, offsets, create_using: Incomplete | None = None): ...
@_dispatchable
def cycle_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def dorogovtsev_goltsev_mendes_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def empty_graph(n: Incomplete | int = 0, create_using: Incomplete | None = None, default=...): ...
@_dispatchable
def ladder_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def lollipop_graph(m, n, create_using: Incomplete | None = None): ...
@_dispatchable
def null_graph(create_using: Incomplete | None = None): ...
@_dispatchable
def path_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def star_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def trivial_graph(create_using: Incomplete | None = None): ...
@_dispatchable
def turan_graph(n, r): ...
@_dispatchable
def wheel_graph(n, create_using: Incomplete | None = None): ...
@_dispatchable
def complete_multipartite_graph(*subset_sizes): ...
