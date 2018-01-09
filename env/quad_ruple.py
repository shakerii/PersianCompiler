class QuadRuple:
    def __init__(self):
        self.table = []

    def add(self, result, op, arg1=None, arg2=None):
        self.table.append({
            'op': op,
            'arg1': arg1,
            'arg2': arg2,
            'res': result
        })

    def __str__(self):
        s = ''
        for t in self.table:
            if t['arg2'] is None:
                if t['op'] == '=':
                    s += t['res'].unique + ' = ' + t['arg1'].unique + '\n'
                else:
                    s += t['res'].unique + ' = ' + t['op'] + t['arg1'].unique + '\n'
            else:
                if t['op'] == '=[]':
                    s += t['res'].unique + ' = ' + t['arg1'].unique + '[' + t['arg2'].unique + ']' + '\n'
                elif t['op'] == '[]=':
                    s += t['res'].unique + '[' + t['arg1'] + '] = ' + t['arg2'].unique + '\n'
                else:
                    s += t['res'].unique + ' = ' + t['arg1'].unique + ' ' + t['op'] + ' ' + t['arg2'].unique + '\n'
        return s
