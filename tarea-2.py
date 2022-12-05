import random

def generate_instance(number_of_nodes=40):
    instance = {}
    i = 0
    while (i < number_of_nodes):
        instance['n'+str(i+1)] = []
        i += 1

    i = 0
    while (i < number_of_nodes):
        number_of_children = random.choice(range(1,4))
        j = 0
        while (j < number_of_children):
            node_key = 'n' + str(i+1)
            new_node_key = ''
            while (True):
                new_node_key = instance.keys()[ random.choice(range(0,40)) ]
                if node_key != new_node_key:
                    break
            instance[node_key].append( [new_node_key, random.choice(range(1,200))] )
            j += 1
        i += 1

    return instance


a = generate_instance()
print("Instancia:")
print(a)
print("Nodos:")
print(len(a.keys()))

