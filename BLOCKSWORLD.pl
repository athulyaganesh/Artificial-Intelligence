%
% Artificial Intelligence
% Assignment 5
% 
% Authors:
% Athulya Ganesh
% David Earnest
% Haneesha Dushara
% Nishanth Chidambaram
% Robbie Schad

% permutation of the original list
permute([], []).
permute(List, [X|Xs]) :- 
    append(W, [X|U], List), 
    append(W, U, MinusX), 
    permute(MinusX, Xs).

% delete element from empty list - return empty list
delete_element([], X, []).
% the head of the list is the element we need to delete - return just the tail (and stop backtracking)
delete_element([H|T], H, T) :- !.
% the head of the list is not what we're looking for - recurse with tail of the list
delete_element([H|T], X, [H|New_List]) :-
			delete_element(T, X, New_List).

%:- set_prolog_flag(occurs_check, error).
%:- set_prolog_stack(global, limit(8 000 000)).
%:- set_prolog_stack(local,  limit(2 000 000)).

is_goal(State):-
    permute(State, PermuteState),
    goal(PermuteState), !.

% defines the blocks in our world
blocks([a, b, c, d, e, f]).

% returns blocks
block(X):-
	blocks(BLOCKS),  % this extracts the list BLOCKS
	member(X, BLOCKS).

%notequal(X11, X2) holds when X1 and X2 are not equal
notequal(X,X):-!, fail.
notequal(_, _).

% substitute(E, E1, OLD, NEW) holds when NEW is the list OLD in which 
% E is substituted by E1.  There are no duplicates in OLD or NEW.
substitute(X, Y, [X|T1], [Y|T1]).
substitute(X, Y, [H|T], [H|T1]):- 
    substitute(X, Y, T, T1).

% move(X, Y, Z, S1, S2) holds when S2 is obtained from S1 by moving the block X
% from the block Y onto the block Z.
move(X, Y, Z, S1, S2):-
	member([clear, X], S1), %find a clear block X in S1
	member([on, X, Y], S1), block(Y), %find a block on which X sits
	member([clear, Z], S1), notequal(X, Z), %find another clear block, Z
	substitute([on, X, Y], [on, X, Z], S1, INT), %remove X from Y, place it on Z
	substitute([clear, Z], [clear, Y], INT, S2). %Z is no longer clear; Y is now clear

% move from a block onto the table
move(X, Y, _, S1, S2):-
    member([clear, X], S1), %find a clear block X in S1
    member([on, X, Y], S1), block(Y), %find a block on which X sits
    substitute([on, X, Y], [clear, Y], S1, INT), %Y is now clear
    append([[on, X, "table"]], INT, S2).

% move from the table onto a block
move(X, _, Z, S1, S2):-
    member([clear, X], S1), %find a clear block X in S1
    member([on, X, "table"], S1), %make sure X is on the table
    member([clear, Z], S1), notequal(X, Z), %find another clear block, Z
    substitute([on, X, "table"], [on, X, Z], S1, INT), %Y is now clear
    delete_element(INT, [clear, Z], S2). %Z is no longer clear

% a path between two state, S1 and S2 exists if a move between them exists
path(S1, S2):-
	move(_, _, _, S1, S2).

% connect: symmetric version of path
connected(S1, S2) :- path(S1, S2).
connected(S1, S2) :- path(S2, S1).

% utility : negation of member
notmember(X, [X|_]):-
    !,fail.
notmember(X, [_|T]):-
    !, notmember(X, T).
notmember(_, _).

% checks that a state has not been visited yet
notYetVisited(State, PathSoFar):-
	permute(State, PermuteState),
	member(PermuteState, PathSoFar), !, fail.
notYetVisited(_, _).

% dfs(State1, Path, PathSoFar): returns the Path from the start to the goal states.
%
% Trivial: if X is the goal return X as the path from X to X.
dfs(X, [X],_):- is_goal(X).

% else expand X by Y and find path from Y
dfs(X, [X|Ypath], VISITED):-
	path(X, Y),
 	notYetVisited(Y, VISITED),
	dfs(Y, Ypath, [Y|VISITED]).

% Test Cases
%
% Run with: start(X), dfs(X, PATH, [X]).
% 
% Test Case 1
% start([[on, a, "table"],[on, b, a],[on, c, b],[clear, c]]).  
% goal([[on, a, b],[on, b, c],[on, c, "table"], [clear, a]]). 
% 
% Test Case 2
% start([[on, a, "table"],[on, b, c],[on, c, "table"], [clear, b], [clear, a]]). 
% goal([[on, a, "table"],[on, b, a],[on, c, "table"], [clear, b], [clear, c]]). 
%
% Assignment Case
start([[on, a, b],[on, b, "table"], [on, c, d], [clear, c], [clear, a], [on, d, "table"]]).
goal([[on, d, a], [on, a, c], [on, c, b], [on, b, "table"], [clear, d]]).
%