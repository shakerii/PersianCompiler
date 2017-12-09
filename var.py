i = -1


def unique_generator():
    global i
    i += 1
    return 'a' + str(i)


class Var:
    def __init__(self, type=None, place=None, value=None):
        self.type = type
        self.place = place
        self.value = value
        self.unique = unique_generator()

    def __eq__(self, other):
        self.type = other.type
        self.place = other.place
        self.value = other.value
