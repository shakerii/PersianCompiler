import ply.lex as lex

tokens = (
    'SHENASE',
    # 'ADAD',
    'INT',
    'FLOAT',
    'HARFE_SABET',
    'JAYEKHALI',
    'NOGHTE_VIRGUL',
    'COMMA',
    'COMMENT',
    'DOT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EQUALS',
    'PLUS_EQ',
    'MINUS_EQ',
    'TIMES_EQ',
    'DIVIDE_EQ',
    'COLON',
    'PLUS_PLUS',
    'MINUS_MINUS',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'QUESTION_MARK',

    'PROGRAM_KW',
    'STRUCT_KW',
    'CONST_KW',
    'INT_KW',
    'FLOAT_KW',
    'BOOL_KW',
    'CHAR_KW',
    'IF_KW',
    'THEN_KW',
    'ELSE_KW',
    'SWITCH_KW',
    'END_KW',
    'CASE_KW',
    'DEFAULT_KW',
    'WHILE_KW',
    'RETURN_KW',
    'BREAK_KW',
    'OR_KW',
    'AND_KW',
    'SHORT_CIRCUIT_OR_KW',
    'SHORT_CIRCUIT_AND_KW',
    'NOT_KW',
    'TRUE_KW',
    'FALSE_KW',
    'MAIN'
)

# Tokens

ragham = r'\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3|\u06F4' \
         r'|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9'
ragham1_9 = r'|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3|\u06F4' \
            r'|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|1|2|3|4|5|6|7|8|9'

harf = r'\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632|\u0698' \
       r'|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644|\u0645|\u0646' \
       r'|\u0647|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_'

harf_ragham = r'' + harf + r'|' + ragham

t_SHENASE = r'' + harf + r'[' + harf_ragham + r']*'
# t_ADAD = r'[' + ragham + r']+'

t_HARFE_SABET = r"'" + harf + r"'"  # wtf?
# t_FIXED_CHARACTER = r'\\.{1}'

# t_JAYEKHALI = r'[" "|\n|\t]+'  # ?
# t_ignore = r'\t\r\f\v'
t_ignore = r' '
# # Ignored characters
# t_ignore = " \t"

t_NOGHTE_VIRGUL = r';|\u061B'
t_COMMA = r',|\u060C'

t_COMMENT = r'/\*([^*]|[\n]|(\*+([^*/]|[\n])))*\*+/|//.*'

t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'٪'
t_EQUALS = r'='
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_TIMES_EQ = r'\*='
t_DIVIDE_EQ = r'\/='
t_COLON = r':'
t_PLUS_PLUS = r'\+\+'
t_MINUS_MINUS = r'--'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='

t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_OPEN_BRACKET = r'\['
t_CLOSE_BRACKET = r'\]'

t_QUESTION_MARK = r'\?|\؟'

t_INT = r'[' + ragham1_9 + r']' + r'[' + ragham + r']*'
t_FLOAT = r'(([' + ragham1_9 + r']' + r'[' + ragham + r']*)|(0|\u0660|\u06F0))' + r'\.((0|\u0660|\u06F0)|' + r'([' + ragham + r']*' + r'[' + ragham1_9 + r']))'

keywords = {
    'برنامه': 'PROGRAM_KW',
    'ساختار': 'STRUCT_KW',
    'ثابت': 'CONST_KW',
    'صحیح': 'INT_KW',
    'اعشاری': 'FLOAT_KW',
    'منطقی': 'BOOL_KW',
    'حرف': 'CHAR_KW',
    'اگر': 'IF_KW',
    'آنگاه': 'THEN_KW',
    'وگرنه': 'ELSE_KW',
    'کلید': 'SWITCH_KW',
    'تمام': 'END_KW',
    'حالت': 'CASE_KW',
    'پیشفرض': 'DEFAULT_KW',
    'وقتی': 'WHILE_KW',
    'برگردان': 'RETURN_KW',
    'بشکن': 'BREAK_KW',
    'یا': 'OR_KW',
    'و': 'AND_KW',
    'یا وگرنه': 'SHORT_CIRCUIT_OR_KW',
    'و همچنین': 'SHORT_CIRCUIT_AND_KW',
    'خلاف': 'NOT_KW',
    'درست': 'TRUE_KW',
    'غلط': 'FALSE_KW',
    'اصلی ': 'MAIN'
}

variables = []


def t_SHENASE(t):
    r'[\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632|\u0698' \
    r'|\u0633|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644|\u0645|\u0646|\u0647' \
    r'|\u0648|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_]' \
    r'[\u0622|\u0627|\u0628|\u067E|\u062A|\u062B|\u062C|\u0686|\u062D|\u062E|\u062F|\u0630|\u0631|\u0632|\u0698|\u0633' \
    r'|\u0634|\u0635|\u0636|\u0637|\u0638|\u0639|\u063A|\u0641|\u0642|\u0643|\u06AF|\u0644|\u0645|\u0646|\u0647|\u0648' \
    r'|\u0649|\u06A9|\u064A|\u06CC|\u06BE|\u06D5|\u06C1|\_|\u0660|\u0661|\u0662|\u0663|\u0664|\u0665|\u0666|\u0667' \
    r'|\u0668|\u0669|\u06F0|\u06F1|\u06F2|\u06F3|\u06F4|\u06F5|\u06F6|\u06F7|\u06F8|\u06F9|0|1|2|3|4|5|6|7|8|9]+'

    t.type = keywords.get(t.value, 'SHENASE')
    if t.type == 'SHENASE':
        if t.value not in variables:
            variables.append(t.value)
    return t


def t_FLOAT(t):
    r'\d+.[\d]+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'/\*([^*]|[\n]|(\*+([^*/]|[\n])))*\*+/|//.*'
    print('Comment Found! :D')


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


lexical_analyser = lex.lex(optimize=True)
