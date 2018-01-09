import codecs

import yacc
import lex


def compile(code):
    yacc.parser.parse(code, lexer=lex.lexical_analyser)


if __name__ == '__main__':
    f = codecs.open('./smpl.txt', encoding='utf-8')
    code = ''
    for i in f:
        code += str(i)
    compile(code)
    f.close()
    for v in yacc.var:
        print(str(yacc.var[v]))
    print(str(yacc.qr))
