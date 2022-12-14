# 2022-1130w ca. 1600 at Re66
###############################################################################
# Working TABLE-DRIVEN-AGENT components

table = {'red': 'thumbsup'}  # incorrect... this was the problem
table = {(('red'),): 'thumbsup'}  # correct

table = {(('red'),): 'thumbsup',
         (('red'), ('red')): 'yes...',
         (('red'), ('red'), ('green')): 'ok, yes...',
         (('red'), ('red'), ('green'), ('red')): 'THUMBSDOWN!'}

percepts = []

percept = 'red'

percepts.append(percept)

action = table.get(tuple(percepts))

print(action)

###############################################################################
# Working TABLE-DRIVEN-AGENT program

table = {(('red'),): 'thumbsup',
         (('red'), ('red')): 'yes...',
         (('red'), ('red'), ('green')): 'ok, yes...',
         (('red'), ('red'), ('green'), ('red')): 'THUMBSDOWN!'}

percepts = []


def program(percept):
    percepts.append(percept)
    action = table.get(tuple(percepts))
    return action


###############################################################################
# Copied from AIMA Git Python; nested function.  How to execute?

def TableDrivenAgentProgram(table):
    """
    [Figure 2.7]
    This agent selects an action based on the percept sequence.
    It is practical only for tiny domains.
    To customize it, provide as table a dictionary of all
    {percept_sequence:action} pairs.
    """
    percepts = []

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action

    return program

###############################################################################
# The below works, but I'm not sure why the prcpts doesn't get wiped
# out by each successive call. It does work with the whole percept history
# though. ... Because the list is initialized outside the function, dummy!

table = {(('red'),): 'thumbsup',
         (('red'), ('red')): 'yes...',
         (('red'), ('red'), ('green')): 'ok, yes...',
         (('red'), ('red'), ('green'), ('red')): 'THUMBSDOWN!'}

prcpts = []


def TableDrivenAgentProgramTHREEARG(table, percepts, pc):

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action

    return program(pc)
