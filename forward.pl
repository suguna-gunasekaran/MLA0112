fact(a).
fact(b).

rule(c) :-
    fact(a),
    fact(b).

forward_chain(X) :-
    rule(X).