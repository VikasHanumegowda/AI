class BinOp:
    def __init__(self, left, operation_p, right, parent=None):
        self.type = "binop"
        self.operation = operation_p
        self.parent = parent
        self.left = left
        self.right = right


class Predicate():
    def __init__(self, name, children=None):
        self.type = "pred"
        self.name = name
        self.operation = "pred"
        if children:  # list of children
            self.children = children
        else:
            self.children = []


class Variable():
    def __init__(self, value):
        self.type = "var"
        self.value = value


class NegateOp:
    def __init__(self, left, parent=None):
        self.type = "not"
        self.operation = "~"
        self.parent = parent
        self.left = left
        self.right = None


class List():
    def __init__(self, child):
        self.type = "list"
        self.children = []
        self.children.append(child)


class Constant():
    def __init__(self, constant_value):
        self.type = "const"
        self.value = constant_value


class Start:  # start of a sentence
    def __init__(self, left):
        self.type = "start"
        self.operation = "start"
        self.left = left
        self.right = None
