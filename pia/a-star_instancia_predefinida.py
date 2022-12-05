instance = {
    'a': [ ['b',75], ['c',118], ['f',140] ],
    'b': [ ['a',75], ['d',71] ],
    'c': [ ['a',118], ['e',111] ],
    'd': [ ['b',71], ['f',151] ],
    'e': [ ['c',111], ['i',70] ],
    'f': [ ['a',140], ['d',151], ['g',99], ['h',80] ],
    'g': [ ['f',99], ['m',211] ],
    'h': [ ['f',80], ['l',146], ['k',97] ],
    'i': [ ['j',75], ['e',70] ],
    'j': [ ['i',75], ['l',120] ],
    'k': [ ['h',97], ['l',138], ['m',101] ],
    'l': [ ['j',120], ['h',146], ['k',138] ],
    'm': [ ['k',101], ['g',211], ['n',90], ['o',98] ],
    'n': [ ['m',90] ],
    'o': [ ['m',85], ['p',142], ['q',98] ],
    'p': [ ['s',92], ['o',142] ],
    'q': [ ['r',86], ['o',98] ],
    'r': [ ['q',86] ],
    's': [ ['t',87], ['p',92] ],
    't': [ ['s',87] ]
}

current_node = 'a'
target_node = 'm'

# A*

# Straight line distances
slds = {
    'a': 366,
    'b': 374,
    'c': 329,
    'd': 380,
    'e': 244,
    'f': 253,
    'g': 176,
    'h': 193,
    'i': 241,
    'j': 242,
    'k': 100,
    'l': 160,
    'm': 0,
    'n': 77,
    'o': 80,
    'p': 199,
    'q': 151,
    'r': 161,
    's': 226,
    't': 234
}

visited_nodes = []

# Functions
def a_star(current_node, target_node):
    node_fns = []
    for node in instance[current_node]:
        node_fns.append( node[1] + slds[node[0]] )
    return instance[current_node][ node_fns.index( min(node_fns) ) ][0]


# Main
while current_node != target_node:
    visited_nodes.append(current_node)
    current_node = a_star(current_node, target_node)
    print("")
    print("Visited Nodes:")
    print(visited_nodes)

cost = 0
index = 0
for node in visited_nodes:
    for _node in instance[node]:
        if (index + 1) < len(visited_nodes):
            if _node[0] == visited_nodes[index + 1]:
                cost += _node[1]
        else:
            if _node[0] == target_node:
                cost += _node[1]
    index += 1

print("")
print("Cost:")
print(cost)

