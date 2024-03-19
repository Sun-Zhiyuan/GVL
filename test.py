import ply.lex as lex
import ply.yacc as yacc

# 定义词法分析器的词法规则
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# 忽略空白符
t_ignore = ' \t'

# 定义词法分析器的处理函数
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 词法分析器错误处理函数
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# 创建词法分析器
lexer = lex.lex()

# 定义语法分析器的语法规则
def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
    '''
    print(p[1])
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[1] == '(':
        p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# 语法分析器错误处理函数
def p_error(p):
    print("Syntax error")

# 创建语法分析器
parser = yacc.yacc()

# 测试
result = parser.parse("2 + 3 * (4 - 1)")
print("Result:", result)