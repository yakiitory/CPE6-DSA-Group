def indent(level):
    return "    " * level

def show_subordinates(parent, nodes, level):
    for node in nodes:
        if node.parent == parent:
            print(f"{indent(level)}" + node.role + ": " + node.name)
            show_subordinates(node, nodes, level + 1)

def display_hierarchy(nodes, ceo_name):
    for node in nodes:
        if node.parent == None:
            print(f"Chief Executive Officer (CEO): {ceo_name}")
            show_subordinates(node, nodes, 1)
