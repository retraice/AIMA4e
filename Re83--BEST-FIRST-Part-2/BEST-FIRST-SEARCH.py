# 2022-1215h 1409
# Local: ReAIMA4e/Re83--BEST-FIRST-Part-2/BEST-FIRST-SEARCH.py
# source of code: https://github.com/aimacode/aima-python/blob/master/search4e.ipynb

###############################################################################
# USEFUL COMMANDS FOR RUNNING IN A venv AND ipython

# python -m venv vRe83
# echo "vRe83/" >> .gitignore
# source vRe83/bin/activate
# pip install --upgrade pip
# pip install matplotlib
# pip install ipython

###############################################################################
# PROBLEMS AND NODES

# %matplotlib inline # meant for use in jupyter notebook / .ipynb file # https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline
# import matplotlib.pyplot as plt
# import random
# import heapq
# import math
# import sys
# from collections import defaultdict, deque, Counter
# from itertools import combinations

###############################################################################
# ANNOTATED AIMA GITHUB CODE

class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states 
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""

    def __init__(self, initial=None, goal=None, **kwds):         # initialize the instance of Problem named <object> in memory
        self.__dict__.update(initial=initial, goal=goal, **kwds) # add argument values to self dictionary

    def actions(self, state):        raise NotImplementedError   # p. 65: This function (method) returns a finite set of actions that can be executed in state.
    def result(self, state, action): raise NotImplementedError   # p. 65: This function (method) is the transition model; it returns the state that results from doing action on state.
    def is_goal(self, state):        return state == self.goal   # p. 65: This function (method) checks the current state and returns it if it is a goal state.
    def action_cost(self, s, a, s1): return 1                    # p. 65: This function (method) is the action cost function, and returns the numeric cost of applying action a in state s to reach state s1.
    def h(self, node):               return 0                    # p. 84: This function (method) is for informed (heuristic) search. 
    
    def __str__(self):                                           # A method for representing the <object> instantiation of Problem as a string, callable as print(<object>) .
        return '{}({!r}, {!r})'.format(                          # string.format(<positional_argument(s)>, <keyword_argument(s)>) # https://realpython.com/python-formatted-output/
            type(self).__name__, self.initial, self.goal)        # ... 
    
###############################################################################
# run

p1 = Problem(1, 2)
p2 = Problem("a", "b", kwd="testingKwd")

print(p1)
print(p2)
# print(p1.type)

###############################################################################
# class Node:
#     "A Node in a search tree."
#     def __init__(self, state, parent=None, action=None, path_cost=0):
#         self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

#     def __repr__(self): return '<{}>'.format(self.state)
#     def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
#     def __lt__(self, other): return self.path_cost < other.path_cost
    
    
# failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't find a solution.
# cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening search was cut off.
    
    
# def expand(problem, node):
#     "Expand a node, generating the children nodes."
#     s = node.state
#     for action in problem.actions(s):
#         s1 = problem.result(s, action)
#         cost = node.path_cost + problem.action_cost(s, action, s1)
#         yield Node(s1, node, action, cost)
        

# def path_actions(node):
#     "The sequence of actions to get to this node."
#     if node.parent is None:
#         return []  
#     return path_actions(node.parent) + [node.action]


# def path_states(node):
#     "The sequence of states to get to this node."
#     if node in (cutoff, failure, None): 
#         return []
#     return path_states(node.parent) + [node.state]

