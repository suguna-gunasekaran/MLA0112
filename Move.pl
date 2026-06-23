move(1,X,Y,_):-
    write('Move disk from '),
    write(X),
    write(' to '),
    write(Y),nl.

move(N,X,Y,Z):-
    N>1,
    N1 is N-1,
    move(N1,X,Z,Y),
    move(1,X,Y,_),
    move(N1,Z,Y,X).
