%consult('C:/Users/Benja/Desktop/Programación/WorkSpace/Tarea_prolog.pl').
%swipl -s Tarea_prolog.pl

sepparimpar(L, P, I).

%lista([],[],[]).
%lista(Ps,Ps,[]).
%lista([X|Xs],Ps,[X|Zs]):-
%lista(Xs,Ys,Zs).

len([],0,-1).
len([L|R],Q,N):-
    len(R,_,N1),
    Q is L, N is N1+1.
%------------------------------------------------------------------------------------------
%todosrango(L, Min, Max).
%------------------------------------------------------------------------------------------
%rangomax(L, Min, Max).
%------------------------------------------------------------------------------------------
%chicograndechico(L, Min, Max).

