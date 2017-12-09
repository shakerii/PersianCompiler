class QuadRuple:
    def __init__(self):
        self.table = []

    def add(self, result, op, arg1, arg2=None):
        self.table.append({
            'op': op,
            'arg1': arg1,
            'arg2': arg2,
            'res': result
        })

    def __str__(self):
        s = ''
        for t in self.table:
            # if t['arg2'] is None:
            #     s += t['res'].place + ', ' + t['op'] + ', ' + t['arg1'].place + '\n'
            # else:
            #     s += t['res'].place + ', ' + t['arg1'].place + ', ' + t['op'] + ', ' + t['arg2'].place + '\n'
            if t['arg2'] is None:
                if t['op'] == '=':
                    s += t['res'].unique + ' = ' + t['arg1'].unique + '\n'
                else:
                    s += t['res'].unique + ' = ' + t['op'] + t['arg1'].unique + '\n'
            else:
                s += t['res'].unique + ' = ' + t['arg1'].unique + ' ' + t['op'] + ' ' + t['arg2'].unique + '\n'
        return s
