class Node:
    state: []
    parent: None
    depth: None

    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def set_state(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent
        