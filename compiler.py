import codecs

import yacc
import lex

if __name__ == '__main__':
    f = codecs.open('./smpl.txt', encoding='utf-8')
    r = ''
    for i in f:
        r += str(i)
    yacc.parser.parse(r, lexer=lex.lexical_analyser)
    f.close()
    print(str(yacc.qr))
