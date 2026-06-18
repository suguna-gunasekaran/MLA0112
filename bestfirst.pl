edge(a,b,2).
edge(a,c,1).
edge(b,d,4).
edge(c,e,2).

best_first(Start,Goal) :-
    path(Start,Goal).

path(Node,Node).

path(Start,Goal) :-
    edge(Start,Next,_),
    path(Next,Goal).