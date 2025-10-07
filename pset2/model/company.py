from .node import Node

class Company:
    def __init__(self):
        self.nodes = []

    def add_ceo(self, name):
        ceo = Node(name, "CEO", None)
        self.nodes.append(ceo)
        return ceo

    def add_manager(self, name, department, ceo):
        manager = Node(name, f"{department} Manager", ceo)
        self.nodes.append(manager)
        return manager

    def add_staff(self, name, manager):
        staff = Node(name, "Staff", manager)
        self.nodes.append(staff)
        return staff

    def get_nodes(self):
        return self.nodes
