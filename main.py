import sys

from ply import lex

file_name = "input.txt"

try:
    with open(file_name, 'r') as file:
        # 读取文件内容
        content = file.read()
except FileNotFoundError:
    print(f"文件 '{file_name}' 不存在.")
except Exception as e:
    print(f"发生了错误: {e}")

# 定义词法分析器规则
tokens = (
    'ID',
    'INT_CONST',
    'FLOAT_CONST',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'INT',
    'FLOAT',
    'CHAR',
    'BOOL',
    'ARRAY',
    'STRUCT',
    'NODE',
    'EDGE',
    'GRAPH',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'MODULO_ASSIGN',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_THAN_EQUAL',
    'LESS_THAN_EQUAL',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_NOT',
    'LPAREN',  # (
    'RPAREN',  # )
    'LBRACKET',  # [
    'RBRACKET',  # ]
    'LBRACE',  # {
    'RBRACE',  # }
    'SEMICOLON',  # ;
    'COMMA',  # ,
    'DOT',  # .
    'VOID',
)

operators = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'TIMES',
    '/': 'DIVIDE',  # 添加 DIVIDE 到 operators 字典中
    '%': 'MODULO',
    '=': 'ASSIGN',
    '+=': 'PLUS_ASSIGN',
    '-=': 'MINUS_ASSIGN',
    '*=': 'TIMES_ASSIGN',
    '%=': 'MODULO_ASSIGN',
    '==': 'EQUAL',
    '!=': 'NOT_EQUAL',
    '>': 'GREATER_THAN',
    '<': 'LESS_THAN',
    '>=': 'GREATER_THAN_EQUAL',
    '<=': 'LESS_THAN_EQUAL',
    '&&': 'LOGICAL_AND',
    '||': 'LOGICAL_OR',
    '!': 'LOGICAL_NOT',
}

keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'array': 'ARRAY',
    'struct': 'STRUCT',
    'node': 'NODE',
    'edge': 'EDGE',
    'graph': 'GRAPH',
    'void': 'VOID',
}


# 正则表达式规则
def t_KEYWORD(t):
    r'if|else|while|for|int|float|char|bool|array|struct|node|edge|graph|void'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    return t


def t_OPERATOR(t):
    r'\+|-|\*|/|%|==|!=|>|<|>=|<=|&&|\|\||!|='
    t.type = operators.get(t.value, 'ID')  # 如果是运算符则替换类型为对应的运算符类型
    return t


def t_INT_CONST(t):
    r'\d+'  # 匹配一个或多个数字
    t.value = int(t.value)  # 转换为整数类型
    return t


def t_FLOAT_CONST(t):
    r'\d+\.\d+'  # 匹配浮点数
    t.value = float(t.value)  # 转换为浮点数类型
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    line_start = content.rfind('\n', 0, t.lexpos) + 1
    if line_start == 0:
        line_start = 1  # 如果没有找到换行符，表示在第一行

    line_end = content.find('\n', t.lexpos)
    if line_end == -1:
        line_end = len(content)  # 如果没有找到下一个换行符，表示在最后一行

    line = content.count('\n', 0, t.lexpos) + 1
    column = t.lexpos - line_start + 1

    print(f"{t.type}('{t.value}', {line}, {column})")
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at index {t.lexpos}")
    t.lexer.skip(1)


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COMMA = r','


def t_SEMICOLON(t):
    r';'
    return t


# 忽略空格和制表符
t_ignore = ' \t\n'


# 创建词法分析器
lexer = lex.lex()

input_data = content

# 打开文件以写入模式
with open('output.txt', 'w') as output_file:
    # 重定向输出到文件
    original_stdout = sys.stdout
    sys.stdout = output_file

    # 输入词法分析器
    lexer.input(input_data)

    # 打印识别到的词法单元
    for token in lexer:
        print(token)

    # 恢复原始的 stdout
    sys.stdout = original_stdout
