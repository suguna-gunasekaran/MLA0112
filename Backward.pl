parent(john,mary).
parent(mary,sam).

grandparent(X,Y):-
    parent(X,Z),
    parent(Z,Y).
