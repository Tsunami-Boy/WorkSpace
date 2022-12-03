%consult('C:/Users/Benja/Desktop/Programación/WorkSpace/Prolog/Tarea_prolog.pl').
%swipl -s Tarea_prolog.pl

%sepparimpar: separa en dos listas, los datos situados en ubicaciones pares e impares, o generar la lista a partir de dos listas de par e impar.
%
%Parámetro 1: Lista la que tiene contenida los datos en ubicaciones pares e impares.
%Parámetro 2: Lista de datos ubicados en casillas pares.
%Parámetro 3: Lista de datos ubicados en casillas impares.
%
%return: debería mostrar en pantalla las listas que se desean conseguir (Lista completa, Lista de pares, Lista de impares).

sepparimpar([],[],[]).
sepparimpar([Lx|[]],[Lx|Ps],I):- sepparimpar([],Ps,I).
sepparimpar([Lx,Ly|Ls],[Lx|Ps],[Ly|Is]):- sepparimpar(Ls,Ps,Is).
%------------------------------------------------------------------------------------------

%todosrango: Comprueba que dentro de un rango, la lista no se pase de los limites.
%
%Parámetro 1: Lista que se desea comprobar.
%Parámetro 2: Número minimo.
%Parámetro 3: Numero maximo.
%
%return: Solo llama a la funcion auxiliar.

todosrango([],[],[]).
todosrango(L, Min, Max):- aux(L,Min,Max,Min).

%aux: Se encarga a traves de un contador comprobar que los numeros entre Min y Max esten en la lista, aunque existan otros numeros.
%
%Parámetro 1: Lista que se desea comprobar.
%Parámetro 2: Número minimo.
%Parámetro 3: Numero maximo.
%Parámetro 4: Contador que inicia en Min hasta Max.
%
%return: Retorna true o false, dependiendo si se cumple el enunciado.

aux([],_,_,_).
aux(L,Min,Max,M):-
    M >= Min,
    (M < Max) ->
        member(M,L), N is (M + 1), aux(L,Min,Max,N) 
        ;
        N is (M - 1), member(N,L).
%------------------------------------------------------------------------------------------
%rangomax: A partir de un rango de Min (Contandolo) hasta un Max (sin contarlo), comprobar que estén todos los numeros de este rango en la lista.
%
%Parámetro 1: Lista que se desea comprobar.
%Parámetro 2: Número minimo.
%Parámetro 3: Numero maximo.
%
%return: Retorna true o false, dependiendo si se cumple el enunciado.

rangomax([], _, _).
rangomax([Lx|Ls], Min, Max):-
    Lx >= Min,
    Lx < Max,
    rangomax(Ls, Min, Max).
%------------------------------------------------------------------------------------------
%chicograndechico(L, Min, Max).