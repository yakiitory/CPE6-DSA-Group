def indent(level):
    return "    " * level

def show_subordinates(parent, nodes, level):
    for node in nodes:
        if node.parent == parent:
            print(f"{indent(level)}" + node.role + ": " + node.name)
            show_subordinates(node, nodes, level + 1)

def display_hierarchy(nodes):
    for node in nodes:
        if node.parent == None:
            print("Chief Executive Officer (CEO): ")
            show_subordinates(node, nodes, 1)
