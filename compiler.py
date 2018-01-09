import codecs

import yacc
import lex


def compile(code):
    yacc.parser.parse(code, lexer=lex.lexical_analyser)


if __name__ == '__main__':
    f = codecs.open('./test/expression.txt', encoding='utf-8')
    code = ''
    for i in f:
        code += str(i)
    compile(code)
    # result = open('res.c', 'w+')
    # for v in yacc.var:
    #     result.write(str(yacc.var[v].type) + ' ' + str(yacc.var[v].unique) + ';\n')
    # try:
    #     compile(code)
    # except Exception as e:
    #     print(e)
    f.close()
    for v in yacc.var:
        print(str(yacc.var[v]))
    print(str(yacc.qr))
