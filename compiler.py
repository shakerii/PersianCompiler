import ply.lex as lex

tokens2 = (
    'FIXED_CHARACTER',
    'SEMICOLON',
    'COMMA',
    'PROGRAM_KW',
    'STRUCTURE_KW',
    'OPENING_BRACE',
    'CLOSING_BRACE_K',
    'CONSTANT_KW',
    'CHAR_KW',
    'BOOLEAN_KW',
    'FLOAT_KW',
    'INTEGER_KW',
    'OPENING_BRACKET',
    'CLOSING_BRACKET',
    'OPENING_PARENTHESES',
    'COSING_PARENTHESES',
    'IF_KW',
    'THEN_KW',
    'ELSE_KW',
    'SWITCH_KW',
    'END_KW',
    'CASE_KW',
    'COLON',
    'DEFAULT_KW',
    'WHILE_KW',
    'RETURN_KW',
    'BREAK_KW',
    'EXP',
    'PLUS_EXP',
    'MINUS_EXP',
    'MUL_EXP',
    'DIV_EXP',
    'PLUSPLUS',
    'MINUSMINUS',
    'CIRCUIT_OR_KW',
    'CIRCUIT_AND_KW',
    'OR_KW',
    'AND_KW',
    'NOT_KW',
    'LT',
    'LE',
    'EQ',
    'GE',
    'G',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'MOD',
    'QUESTION_MARK',
    'DOT',
    'TRUE_KW',
    'FALSE_KW',
    'MAIN',
    'ID',
    'COMMENT',
    'NUMBER',
)

tokens = (
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
)

# Tokens

ragham = r'\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3|\u06F4' \
         r'|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9'

harf = r'\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632|\u0698' \
       r'|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644|\u0645|\u0646' \
       r'|\u0647|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_'

harf_ragham = r'' + harf + r'|' + ragham

t_SHENASE = r'' + harf + r'[' + harf_ragham + r']*'
t_ADAD = r'[' + ragham + r']+'

t_HARFE_SABET = r"'" + harf + r"'"  # wtf?
# t_FIXED_CHARACTER = r'\\.{1}'

t_JAYEKHALI = r'[" "|\n|\t]+'  # ?
t_ignore = r' \t\r\f\v'
# # Ignored characters
# t_ignore = " \t"

t_NOGHTE_VIRGUL = r';|\u061B'
t_COMMA = r',|\u060C'

t_COMMENTS = r''  # ?

t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'٪'
t_EQUALS = r'='
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_MUL_EQ = r'\*='
t_DIV_EQ = r'\/='
t_COLON = r':'
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='

t_OPEN_PAREN = r'\)'
t_CLOSE_PAREN = r'\('
t_OPEN_BRACE = r'\}'
t_CLOSE_BRACE = r'\{'
t_OPEN_BRACKET = r'\]'
t_CLOSE_BRACKET = r'\['

# t_QUESTION_MARK = r'\?|\؟'

result = ''


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    global result
    result += "Illegal character '%s'" % t.value[0] + '\n'
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()


if __name__ == '__main__':
    print(result)
