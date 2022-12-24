""" 2022-1224s
    Local: ReAIMA4e/Re93
    source of (most of the) code:
    https://github.com/aimacode/aima-python/blob/master/search4e.ipynb"""

# #%matplotlib inline
import matplotlib.pyplot as plt
import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations

class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""
    def __init__(self, initial=None, goal=None, **kwds):
        self.__dict__.update(initial=initial, goal=goal, **kwds)

    def actions(self, state):        raise NotImplementedError  # ***NOT DONE***
    def result(self, state, action): raise NotImplementedError  # ***NOT DONE***
                                                                # in romania, state is "'A': ( 76, 497),",
                                                                # and action is "('O', 'Z'): 71,".
    def is_goal(self, state):        return state == self.goal
    def action_cost(self, s, a, s1): return 1                   # ***NOT DONE***
    def h(self, node):               return 0

    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)

class Node:
    # "A Node in a search tree."
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

    def __repr__(self): return '<{}>'.format(self.state)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other): return self.path_cost < other.path_cost

failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't
                                              # find a solution.
cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening
                                              # search was cut off.

def expand(problem, node):
    # "Expand a node, generating the children nodes."
    s = node.state                                 # set variable s equal to the state attribute of the given node
    for action in problem.actions(s):              # for each action
        s1 = problem.result(s, action)             # s1 is the state that results from applying given action to state s
        cost = node.path_cost + problem.action_cost(s, action, s1)  # set variable cost to cost of going to s1
        yield Node(s1, node, action, cost) # generate child node given arguments s1, parent node, action applied, cost


class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x): 
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        for item in items:
            self.add(item)
         
    def add(self, item):
        """Add item to the queuez."""
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """Pop and return the item with min f(item) value."""
        return heapq.heappop(self.items)[1]
    
    def top(self): return self.items[0][1]

    def __len__(self): return len(self.items)

        
def best_first_search(problem, f):           # ***PROBLEM NOT DONE***
    # "Search nodes with minimum f(node) value first."
    node = Node(problem.initial)             # Make node out of initial state
    frontier = PriorityQueue([node], key=f)  # ***NOT DONE***
#    return frontier
    reached = {problem.initial: node}   # create dict. reached: {'<problem initial state>': '<Node(problem.initial)>',}
    while frontier:                          # Starting with first node in frontier, ??and continuing through queue??
        node = frontier.pop()                # set node equal to the top node in frontier, removing it from queue
        if problem.is_goal(node.state):      # check if the state of this node is the goal state of the problem
            return node                      # if it is, return the node as output and stop
        for child in expand(problem, node):  # if not, expand the node and for each child node of it....
            s = child.state                  # set s equal to the child node's state
            if s not in reached or child.path_cost < reached[s].path_cost: # if node is new or cheaper than known ones
                reached[s] = child           # ?? add pair to reached dict. {'<child.state>': '<child node>',} ??
                frontier.add(child)          # add <child node> to frontier queue.<see ***CORRECTION*** below>
                    # ***CORRECTION***: During the livestream I said that after the while loop was done, we'd return to the newly updated
                    # frontier. False.  The frontier updates at the end of each loop through the while, then the while starts over, and if
                    # the while never finds a goal state, it terminates and return failure is executed.

    return failure                           # if goal state not found by while loop above, return failure and stop.

################################################################################
# for printing colorized text
class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
################################################################################

class RouteProblem(Problem): # e.g. atobproblem = RouteProblem('A', 'B',
                             # map=simpleMap) """A problem to find a route
                             # between locations on a `Map`.  Create a problem
                             # with RouteProblem(start, goal, map=Map(...)}).  #
                             # here we'd pass the map romania States are the
                             # vertexes in the Map graph; actions are
                             # destination states."""

    def actions(self, state):   # e.g. atobproblem.actions('A')
        # """The places neighboring `state`."""
        return self.map.neighbors[state] # actions-STEP-1, e.g. atobproblem.map.neighbors['A']

    def result(self, state, action):
        # """Go to the `action` place, if the map says that is possible."""
        return action if action in self.map.neighbors[state] else state

    def action_cost(self, s, action, s1):
        # """The distance (cost) to go from s to s1."""
        return self.map.distances[s, s1]

    # h stuff
    def h(self, node):
        "Straight-line distance between state and the goal."
        locs = self.map.locations
        return straight_line_distance(locs[node.state], locs[self.goal])

def straight_line_distance(A, B):  # seems to be for informed h search
    "Straight-line distance between two points."
    return sum(abs(a - b)**2 for (a, b) in zip(A, B)) ** 0.5

class Map:
    """A map of places in a 2D world: a graph with vertexes and links between them.
    In `Map(links, locations)`, `links` can be either [(v1, v2)...] pairs,
    or a {(v1, v2): distance...} dict. Optional `locations` can be {v1: (x, y)}
    If `directed=False` then for every (v1, v2) link, we add a (v2, v1) link."""

    def __init__(self, links, locations=None, directed=False):
        if not hasattr(links, 'items'):          # Distances are 1 by default
                                                 # --AIMA ## returns t or f

            links = {link: 1 for link in links}  # If your links doesn't have
                                                 # 'items' ?attributes, set each
                                                 # 'items' to 1
        if not directed:                         # 'directed=False' by default
                                                 # above;

            for (v1, v2) in list(links):         # list() creates list object.
                links[v2, v1] = links[v1, v2]    # This adds mirror-like entries
                                                 # in our dict, for backtracking

        self.distances = links                   # distances attribute is the
                                                 # updated, backtrack-able links
                                                 # dict. This outputs a look-up
                                                 # table of the updated links
                                                 # dictionary, key=state pair,
                                                 # value = distance.

        self.neighbors = multimap(links)	 # get all neighbors of all
                                                 # states, i.e. actions
                                                 # available at each state

        self.locations = locations or defaultdict(lambda: (0, 0))
#        self.locations = locations or defaultdict()        
                                                 # "from collections import
                                                 # defaultdict" above

                    # In [7]: tmap.locations Out[7]: {'A': (76, 497), 'S': (187,
                    # 463), 'T': (83, 414), 'Z': (92, 539)}

                    # In [8]: tmap = Map(tlinks)

                    # In [9]: tmap.locations Out[9]: defaultdict(<function
                    # __main__.Map.__init__.<locals>.<lambda>()>, {})

                    # Maybe to avoid errors / exceptions?


# with lambda
# In [24]: tmap.locations
# Out[24]: defaultdict(<function __main__.Map.__init__.<locals>.<lambda>()>, {})

# without lambda
# In [32]: tmap.locations
# Out[32]: defaultdict(None, {})
                                                 
def multimap(pairs) -> dict:    # "-> dict" is function annotation.  "Given
                                # (key, val) pairs, make a dict of {key:
                                # [val,...]}." --AIMA.
    result = defaultdict(list)  # "from collections import defaultdict" above;
                                # list() creates list object.  defaultdict is a
                                # "dict subclass that calls a factory function
                                # to supply missing values" -- python.org
    for key, val in pairs:	# pairs is now our reversed tlinks.
                    	        # pairs will be links, as in "self.neighbors =
                                # multimap(links)" above
       result[key].append(val)  # add key value pair to result
    return result

################################################################################
# run Re90 and Re91; t stands for test

tlinks = {('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
          ('Yo', 'Momma'): 90, ('Momma', 'Dadda'): 91, ('T', 'Yo'): 38,}

tlocations = {'A': ( 76, 497), 'S': (187, 463), 'T': ( 83, 414), 'Z': (92, 539),
              'Yo': ( 60, 30), 'Momma': ( 87, 17), 'Dadda': (100, 40),}

tmap = Map(tlinks, tlocations)

# tmap.distances
# tmap.locations

tproblem = RouteProblem('A', 'Dadda', map=tmap)


def f(tvalue):
    return tvalue

# best_first_search(tproblem, f)

################################################################################
# AIMA:
# Some specific RouteProblems
# romania = Map(  # instantiate class Map with following arguments:
#     # 'links': acitons (p. 71): "`links` can be either [(v1, v2)...] pairs, or a {(v1, v2): distance...} dict."
#     {('O', 'Z'):  71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
#      ('L', 'T'): 111, ('L', 'M'):  70, ('D', 'M'): 75, ('C', 'D'): 120, ('C', 'R'): 146,
#      ('C', 'P'): 138, ('R', 'S'):  80, ('F', 'S'): 99, ('B', 'F'): 211, ('B', 'P'): 101,
#      ('B', 'G'):  90, ('B', 'U'):  85, ('H', 'U'): 98, ('E', 'H'):  86, ('U', 'V'): 142,
#      ('I', 'V'):  92, ('I', 'N'):  87, ('P', 'R'): 97},
#     # 'locations': states (p. 71): "Optional `locations` can be {v1: (x, y)}"
#     {'A': ( 76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294),
#      'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
#      'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
#      'S': (187, 463), 'T': ( 83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})

# r0 = RouteProblem('A', 'A', map=romania)
# r1 = RouteProblem('A', 'B', map=romania)
# r2 = RouteProblem('N', 'L', map=romania)
# r3 = RouteProblem('E', 'T', map=romania)
# r4 = RouteProblem('O', 'M', map=romania)
