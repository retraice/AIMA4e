""" 2022-1225u
    Local: ReAIMA4e/Re94"""



# def best_first_search(problem, f):

def f(dvalue):
    return 'F-you'

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

tmap = Map(tlinks, tlocations)
tproblem = RouteProblem('A', 'Dadda', map=tmap)

class Node:
    # "A Node in a search tree."
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.__dict__.update(state=state, parent=parent, action=action, path_cost=path_cost)

    def __repr__(self): return '<{} booya'.format(self.state)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other): return self.path_cost < other.path_cost



class PriorityQueue:
    """A queue in which the item with minimum f(item) is always popped first."""

    def __init__(self, items=(), key=lambda x: x): 
        self.key = key
        self.items = [] # a heap of (score, item) pairs
        for item in items:
            self.add(item)


            
# node = Node(tproblem.initial)             # Make node out of initial state
# frontier = PriorityQueue([node], key=f)  

    
