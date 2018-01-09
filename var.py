i = -1


def unique_generator():
    global i
    i += 1
    return 'var' + str(i)


class Var:
    def __init__(self, type=None, place=None, value=None):
        self.is_const = False
        self.is_array = False
        self.type = type
        self.place = place
        self.value = value
        self.trueList = []
        self.falseList = []
        self.nextList = []
        self.unique = None

    def set_unique(self):
        self.unique = unique_generator()

    def __str__(self):
        return '{' + '\n' + \
               '    place:' + str(self.place) + '\n' + \
               '    type: ' + str(self.type) + '\n' + \
               '    value: ' + str(self.value) + '\n' + \
               '    unique: ' + str(self.unique) + '\n' + \
               '}'
