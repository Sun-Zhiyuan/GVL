import sys

from ply import lex
import ply.yacc as yacc

from NodeAddEdge import NodeAddEdge
from NodeAddNode import NodeAddNode
from NodeAddSubTail import NodeAddSubTail
from NodeArrayAccess import NodeArrayAccess
from NodeArrayAccessExpression import NodeArrayAccessExpression
from NodeArrayAssignment import NodeArrayAssignment
from NodeAssignExpression import NodeAssignExpression
from NodeBlock import NodeBlock
from NodeChangeEdgeRgb import NodeChangeEdgeRGB
from NodeChangeNodeRgb import NodeChangeNodeRGB
from NodeChangeNodeX import NodeChangeNodeX
from NodeDfs import NodeDFS
from NodeEqualityExpression import NodeEqualityExpression
from NodeExpressionStatement import NodeExpressionStatement
from NodeForStatement import NodeForStatement
from NodeFormalParameter import NodeFormalParameter, NodeArrayParameter
from NodeFunctionCall import NodeFunctionCall
from NodeFunctionNum import NodeFunctionNum
from NodeGreaterThan import NodeGreaterThan
from NodeGreaterThanOrEqual import NodeGreaterThanOrEqual
from NodeIdentifer import NodeIdentifier
from NodeIfElseStatement import NodeIfElseStatement
from NodeIfStatement import NodeIfStatement
from NodeLessThan import NodeLessThan
from NodeLessThanOrEqual import NodeLessThanOrEqual
from NodeMulDivMod import NodeMulDivMod
from NodePIExpression import NodePIExpression
from NodePostDecrementExpression import NodePostDecrementExpression
from NodePreincrementExpression import NodePreIncrementExpression
from NodeProgram import NodeProgram
from NodeFunctionDefinition import NodeFunctionDefinition
from NodeRemoveEdge import NodeRemoveEdge
from NodeRemoveNode import NodeRemoveNode
from NodeReturn import NodeReturnStatement
from NodeShow import NodeShow
from NodeStructDefinition import NodeStructDefinition
from NodeTypeSpecification import NodeTypeSpecification
from NodeUnaryExpression import NodeUnaryExpression
from NodeVariableDeclaration import NodeVariableDeclaration
from NodeWhileStatement import NodeWhileStatement
from NodeNodeExpresion import NodeNodeExpression

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
    'ADJ',
    'LENGTH',
    'BOOL',
    'DFS',
    'VISITED',
    'UNVISITED',
    'BFS',
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
    'ADD_NODE',
    'ADD_EDGE',
    'REMOVE_NODE',
    'REMOVE_EDGE',
    'CHANGE_NODE_RGB',
    'CHANGE_NODE_X',
    'CHANGE_NODE_Y',
    'CHANGE_EDGE_RGB',
    'SHOW',
    'TRUE',
    'FALSE',
    'RETURN'
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
    'adj': 'ADJ',
    'length': 'LENGTH',
    'array': 'ARRAY',
    'struct': 'STRUCT',
    'node': 'NODE',
    'dfs': 'DFS',
    'bfs': 'BFS',
    'edge': 'EDGE',
    'graph': 'GRAPH',
    'void': 'VOID',
    'add_node': 'ADD_NODE',
    'add_edge': 'ADD_EDGE',
    'remove_node': 'REMOVE_NODE',
    'remove_edge': 'REMOVE_EDGE',
    'change_node_rgb': 'CHANGE_NODE_RGB',
    'change_node_x': 'CHANGE_NODE_X',
    'change_node_y': 'CHANGE_NODE_Y',
    'change_edge_rgb': 'CHANGE_EDGE_RGB',
    'show': 'SHOW',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN',
}


# 正则表达式规则
def t_KEYWORD(t):
    r'if|else|while|for|int|float|char|bool|array|struct|node|edge|graph|void|true|false|adj|length|dfs|bfs|return|VISITED|UNVISITED'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    return t


def t_OPERATOR(t):
    r'\+|-|\*|/|%|==|!=|>|<|>=|<=|&&|\|\||!|='
    t.type = operators.get(t.value, 'ID')  # 如果是运算符则替换类型为对应的运算符类型
    return t


def t_FLOAT_CONST(t):
    r'\d+\.\d+'  # 匹配浮点数
    t.value = float(t.value)  # 转换为浮点数类型
    return t


def t_INT_CONST(t):
    r'\d+'  # 匹配一个或多个数字
    t.value = int(t.value)  # 转换为整数类型
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    # line_start = content.rfind('\n', 0, t.lexpos) + 1
    # if line_start == 0:
    #     line_start = 1  # 如果没有找到换行符，表示在第一行
    #
    # line_end = content.find('\n', t.lexpos)
    # if line_end == -1:
    #     line_end = len(content)  # 如果没有找到下一个换行符，表示在最后一行
    #
    # line = content.count('\n', 0, t.lexpos) + 1
    # column = t.lexpos - line_start + 1
    #
    # # print(f"{t.type}('{t.value}', {line}, {column})")
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


def t_BOOL(t):
    r'bool'
    t.type = 'BOOL'
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


# Parsing rules

def p_program(p):
    '''program :   function_definition_list struct_definition_list '''
    p[0] = NodeProgram(p[1], p[2])


def p_function_definition_list(p):
    '''function_definition_list : function_definition function_definition_list
                                | empty'''
    if len(p) == 3:  # 如果有两个子节点，即存在 function_definition 和 function_definition_list
        p[0] = [p[1]] + p[2]  # 将当前 function_definition 添加到已解析的 function_definition_list 中
    else:
        p[0] = []  # 如果为空，则初始化一个空列表，表示没有 function_definition

    print("Function definition list parsed.")
    # print('this is len of p: -----------------------------', len(p))
    # print('Content of p:')
    # for item in p:
    #     print(item)
    #


def p_struct_definition_list(p):
    '''struct_definition_list : struct_definition struct_definition_list
                              | empty'''
    if len(p) == 3:  # 如果有两个子节点
        p[0] = [p[1]] + p[2]  # 将当前 struct_definition 添加到已解析的 struct_definition_list 中
    else:
        p[0] = []  # 如果为空，则初始化一个空列表，表示没有 struct_definition
    print("Struct definition list parsed.")


def p_function_definition(p):
    '''function_definition : type_specification ID LPAREN formal_parameters RPAREN block
                           | type_specification DFS LPAREN formal_parameters RPAREN block
                           | type_specification BFS LPAREN formal_parameters RPAREN block'''
    print("Function definition parsed.")

    if len(p) == 7:  # 如果有7个子节点
        p[0] = NodeFunctionDefinition(p[1], p[2], p[4], p[6])  # 将解析结果存储为一个元组
    else:
        p[0] = None  # 如果解析失败，则将 p[0] 设为 None


def p_struct_definition(p):
    '''struct_definition : STRUCT ID LBRACE type_specification RBRACE SEMICOLON'''
    print("Struct definition parsed.")

    struct_name = p[2]  # 结构体名称
    struct_body = p[4]  # 结构体内容

    p[0] = NodeStructDefinition(struct_name, struct_body)


def p_formal_parameters(p):
    '''formal_parameters : formal_parameter COMMA formal_parameters
                         | formal_parameter
                         | empty'''
    print("Formal parameters parsed.")

    if len(p) == 4:  # 如果有3个子节点，即存在 formal_parameter 和 formal_parameters
        p[0] = [p[1]] + p[3]  # 将当前 formal_parameter 添加到已解析的 formal_parameters 列表中
    else:  # 如果只有一个子节点，即存在单个 formal_parameter
        p[0] = [p[1]]  # 创建一个只包含一个 formal_parameter 的列表
    print("Formal parameters parsed.")
    # print('this is len of p: -----------------------------', len(p))
    # print('Content of p:')
    # for item in p:
    #     print(item)


def p_formal_parameter(p):
    '''formal_parameter : type_specification ID
                        | type_specification ID LBRACKET INT_CONST RBRACKET
                        | type_specification ID LBRACKET RBRACKET'''
    print("Formal parameter parsed.")

    if len(p) == 3:  # 第一种情况：普通变量参数
        p[0] = NodeFormalParameter(p[1], p[2])
    elif len(p) == 6:  # 第二种情况：带有数组大小的数组参数
        p[0] = NodeArrayParameter(p[1], p[2], p[4])
    elif len(p) == 5:  # 第三种情况：没有数组大小的数组参数
        p[0] = NodeArrayParameter(p[1], p[2], None)


def p_type_specification(p):
    '''type_specification : INT
                          | FLOAT
                          | CHAR
                          | BOOL
                          | GRAPH
                          | EDGE
                          | NODE
                          | VOID'''
    p[0] = NodeTypeSpecification(p[1])


def p_block(p):
    '''block : LBRACE compound_statement RBRACE'''
    print("Block parsed.")
    p[0] = NodeBlock(p[2])  # 创建一个包含 compound_statement 的节点


def p_compound_statement(p):
    '''compound_statement : statement compound_statement
                          | empty
                          | variable_declaration compound_statement
                          | special_function compound_statement'''
    print("Compound statement parsed.")
    if len(p) == 3:  # 如果有两个子节点，即存在语句和剩余的语句列表
        p[0] = [p[1]] + p[2]  # 将当前语句添加到已解析的语句列表中
    else:
        p[0] = []  # 如果为空，则初始化一个空列表


def p_variable_declaration(p):
    '''variable_declaration : type_specification ID SEMICOLON
                             | type_specification ID ASSIGN expression_statement SEMICOLON
                             | type_specification ID COMMA variable_declaration SEMICOLON
                             | type_specification ID LBRACKET INT_CONST RBRACKET SEMICOLON'''

    if len(p) == 4:  # 单个变量声明
        p[0] = NodeVariableDeclaration(p[1], p[2])
    elif len(p) == 6 and p[3] == 'ASSIGN':  # 带有赋值的变量声明
        p[0] = NodeVariableDeclaration(p[1], p[2], p[4])
    elif len(p) == 6 and p[3] == 'COMMA':  # 变量列表声明
        p[0] = NodeVariableDeclaration(p[1], p[2], variable_list=p[4])
    elif len(p) == 6 and p[3] == 'LBRACKET':  # 数组声明
        p[0] = NodeVariableDeclaration(p[1], p[2], array_size=p[4])


def p_statement(p):
    '''statement : expression_statement
                 | return_statement
                 | if_statement
                 | for_statement
                 | while_statement'''
    print("Statement parsed.")
    p[0] = p[1]


def p_special_function(p):
    '''special_function : add_node
                        | add_edge
                        | remove_node
                        | remove_edge
                        | change_node_rgb
                        | change_node_x
                        | change_node_y
                        | change_edge_rgb
                        | show
                        | dfs'''
    p[0] = p[1]


def p_add_node(p):
    '''add_node : ADD_NODE LPAREN expression COMMA expression COMMA LBRACE expression COMMA expression COMMA expression COMMA expression COMMA expression COMMA expression RBRACE RPAREN SEMICOLON'''
    print("Add node parsed.")
    p[0] = NodeAddNode(p[3], p[5], p[8], p[10], p[12], p[14], p[16])


def p_add_edge(p):
    '''add_edge : ADD_EDGE LPAREN expression COMMA LBRACE expression COMMA expression COMMA expression COMMA expression COMMA expression COMMA expression RBRACE RPAREN SEMICOLON'''

    print("Add edge parsed.")
    p[0] = NodeAddEdge(p[3], p[6], p[8], p[10], p[12], p[14])


# 在 p_remove_node 函数中生成节点
def p_remove_node(p):
    '''remove_node : REMOVE_NODE LPAREN expression COMMA expression RPAREN SEMICOLON'''
    print("Remove node parsed.")
    p[0] = NodeRemoveNode(p[3], p[5])


def p_remove_edge(p):
    '''remove_edge : REMOVE_EDGE LPAREN expression COMMA expression RPAREN SEMICOLON'''
    print("Remove edge parsed.")
    p[0] = NodeRemoveEdge(p[3], p[5])


def p_change_node_rgb(p):
    '''change_node_rgb : CHANGE_NODE_RGB LPAREN expression COMMA expression COMMA LBRACE expression COMMA expression COMMA expression RBRACE RPAREN SEMICOLON'''
    print("Change node RGB parsed.")
    p[0] = NodeChangeNodeRGB(p[3], p[5], p[7], p[9], p[11])


def p_change_node_x(p):
    '''change_node_x : CHANGE_NODE_X LPAREN expression COMMA expression COMMA expression RPAREN SEMICOLON'''
    print("Change node X parsed.")
    p[0] = NodeChangeNodeX(p[3], p[5], p[7])


def p_change_node_y(p):
    '''change_node_y : CHANGE_NODE_Y LPAREN expression COMMA expression COMMA expression RPAREN SEMICOLON'''
    print("Change node Y parsed.")
    p[0] = NodeChangeNodeX(p[3], p[5], p[7])


def p_change_edge_rgb(p):
    '''change_edge_rgb : CHANGE_EDGE_RGB LPAREN expression COMMA expression COMMA expression COMMA expression COMMA expression COMMA expression RPAREN SEMICOLON'''
    print("Change edge RGB parsed.")
    p[0] = NodeChangeEdgeRGB(p[3], p[5], p[7], p[9], p[11], p[13])


def p_show(p):
    '''show : SHOW LPAREN expression RPAREN SEMICOLON'''
    print("Show parsed.")
    p[0] = NodeShow(p[3])


def p_dfs(p):
    '''dfs : DFS LPAREN ID COMMA node_expression COMMA ID RPAREN SEMICOLON'''
    print("DFS parsed.")
    p[0] = NodeDFS(p[3], p[5], p[7])


def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''
    print("Expression statement parsed.")
    p[0] = NodeExpressionStatement(p[1])


def p_return_statement(p):
    '''return_statement : RETURN expression_statement'''
    print("Return statement parsed.")
    p[0] = NodeReturnStatement(p[2])


def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE compound_statement RBRACE
                    | IF LPAREN expression RPAREN block ELSE LBRACE compound_statement RBRACE
                    | IF LPAREN expression RPAREN block ELSE if_statement'''
    print("If statement parsed.")

    if len(p) == 8:  # 如果是简单的if语句
        p[0] = NodeIfStatement(p[3], p[6])  # 创建if语句节点，传入条件表达式和语句块
    elif len(p) == 7:  # 如果有else块
        p[0] = NodeIfElseStatement(p[3], p[5], p[7])  # 创建if-else语句节点，传入条件表达式、if块和else块
    else:  # 如果有嵌套的if-else块
        p[0] = NodeIfElseStatement(p[3], p[5], p[7])  # 创建if-else语句节点，传入条件表达式、if块和嵌套的if-else块

    print("If statement node created.")


def p_for_statement(p):
    '''for_statement : FOR LPAREN INT ID ASSIGN INT_CONST SEMICOLON expression SEMICOLON post_increment_expression RPAREN block'''
    p[0] = NodeForStatement(p[4], p[6], p[9], p[11])
    print("For statement parsed.")


def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN block'''
    p[0] = NodeWhileStatement(p[3], p[5])
    print("While statement parsed.")


def p_empty(p):
    'empty :'
    pass


def p_expression(p):
    '''expression : assign_expression
                  | node_expression'''
    print("Expression parsed.")
    p[0] = p[1]  # 将子节点的解析结果传递给父节点


def p_assign_expression(p):
    '''assign_expression : equality_expression ASSIGN assign_expression
                         | equality_expression
                         | MINUS MINUS primary_expression
                         | PLUS PLUS primary_expression'''
    print("Assignment expression parsed.")
    if len(p) == 4:  # 赋值表达式
        p[0] = NodeAssignExpression(p[1], p[3])
    elif len(p) == 2:  # 相等性表达式
        p[0] = NodeEqualityExpression(p[1])
    else:  # 后增表达式或前增表达式
        if p[1] == '--':
            p[0] = NodePostDecrementExpression(p[3])
        else:
            p[0] = NodePreIncrementExpression(p[3])


def p_equality_expression(p):
    '''equality_expression : relational_expression
                           | relational_expression EQUAL relational_expression
                           | relational_expression LOGICAL_NOT ASSIGN relational_expression'''
    if len(p) == 2:  # If only one relational expression
        p[0] = NodeEqualityExpression(p[1])
    elif len(p) == 4:  # If two relational expressions with equality operator
        p[0] = NodeEqualityExpression(p[1], p[2], p[3])
    else:  # If there's a logical_not and an assignment
        p[0] = NodeEqualityExpression(p[1], p[2], p[4])


def p_unary_expression(p):
    '''unary_expression : primary_expression
                        | PLUS primary_expression
                        | MINUS primary_expression
                        | LOGICAL_NOT primary_expression'''
    if len(p) == 2:  # If only primary expression
        p[0] = NodeUnaryExpression(expression=p[1])
    else:  # If unary operator present
        p[0] = NodeUnaryExpression(operator=p[1], expression=p[2])


def p_relational_expression(p):
    '''relational_expression : add_sub_expression compare_expression'''
    p[0] = (p[1], p[2])


def p_compare_expression(p):
    '''compare_expression : empty
                          | LESS_THAN add_sub_expression compare_expression
                          | LESS_THAN_EQUAL ASSIGN add_sub_expression compare_expression
                          | GREATER_THAN add_sub_expression compare_expression
                          | GREATER_THAN_EQUAL ASSIGN add_sub_expression compare_expression'''
    print("Compare expression parsed.")

    if len(p) == 2:  # 如果只有一个子节点，即为空
        p[0] = None  # 创建一个空节点
    elif len(p) == 4:  # 如果有三个子节点
        if p[1] == '<':  # 如果是小于号
            p[0] = NodeLessThan(p[2], p[3])  # 创建小于节点，传入左右子表达式
        elif p[1] == '<=':  # 如果是小于等于号
            p[0] = NodeLessThanOrEqual(p[2], p[4])  # 创建小于等于节点，传入左右子表达式
        elif p[1] == '>':  # 如果是大于号
            p[0] = NodeGreaterThan(p[2], p[3])  # 创建大于节点，传入左右子表达式
        elif p[1] == '>=':  # 如果是大于等于号
            p[0] = NodeGreaterThanOrEqual(p[2], p[4])  # 创建大于等于节点，传入左右子表达式
    else:
        # 处理其他情况
        pass


def p_add_sub(p):
    '''add_sub_expression : mul_div_mod_expression add_sub_tail'''
    print("Addition/Subtraction parsed.")
    p[0] = (p[1], p[2])


def p_add_sub_tail(p):
    '''add_sub_tail : PLUS mul_div_mod_expression add_sub_tail
                    | MINUS mul_div_mod_expression add_sub_tail
                    | empty'''
    print("Addition/Subtraction tail parsed.")
    if len(p) == 4:
        p[0] = NodeAddSubTail(p[1], p[2], p[3])
    else:
        p[0] = None


def p_mul_div_mod(p):
    '''mul_div_mod_expression : unary_expression mul_div_mod_tail'''
    print("Multiplication/Division/Modulus parsed.")
    p[0] = (p[1], p[2])


def p_mul_div_mod_tail(p):
    '''mul_div_mod_tail : TIMES unary_expression mul_div_mod_tail
                        | DIVIDE unary_expression mul_div_mod_tail
                        | MODULO unary_expression mul_div_mod_tail
                        | empty'''
    print("Multiplication/Division/Modulus tail parsed.")
    if len(p) == 4:
        p[0] = NodeMulDivMod(p[1], p[2], p[3])
    else:
        p[0] = None


def p_array_assignment_expression(p):
    '''array_assignment_expression : array_access ASSIGN expression'''
    print("Array assignment expression parsed.")
    p[0] = NodeArrayAssignment(p[1], p[3])


def p_post_increment_expression(p):
    '''post_increment_expression : PLUS PLUS primary_expression
                                 | MINUS MINUS primary_expression'''
    print("Post-increment expression parsed.")
    if len(p) == 4:
        p[0] = NodePIExpression(p[1], p[3])  # 创建后自增/自减表达式节点，传入操作符和表达式


def p_node_expression(p):
    '''node_expression : ID
                       | ID DOT ADJ LBRACKET ID RBRACKET LBRACKET ID RBRACKET
                       | INT_CONST'''
    if len(p) == 2:  # 只有一个标识符或整数常量
        p[0] = p[1]
    else:  # 有ADJ的节点表达式
        p[0] = NodeNodeExpression(p[1], p[5], p[9])


def p_array_access(p):
    '''array_access : ID LBRACKET expression RBRACKET'''
    print("Array access parsed.")
    p[0] = NodeArrayAccessExpression(p[1], p[3])


def p_primary_expression(p):
    '''primary_expression : ID
                          | ID args_expression
                          | TRUE
                          | FALSE
                          | num_expression
                          | ID LBRACKET expression RBRACKET
                          | NODE
                          | EDGE
                          | GRAPH
                          | LPAREN expression RPAREN'''
    print("Primary expression parsed.")

    if len(p) == 2:
        if p[1] in ['TRUE', 'FALSE', 'NODE', 'EDGE', 'GRAPH']:
            p[0] = p[1]  # 直接将 TRUE、FALSE、NODE、EDGE、GRAPH 存储在 p[0] 中
        else:
            p[0] = NodeIdentifier(p[1])  # 将 ID 存储在 NodeIdentifier 类的实例中
    elif len(p) == 3:
        p[0] = NodeFunctionCall(p[1], p[2])  # 创建函数调用节点，传入函数名和参数表达式
    elif len(p) == 5:
        p[0] = NodeArrayAccess(p[1], p[3])  # 创建数组访问节点，传入数组 ID 和索引表达式
    else:
        p[0] = p[2]  # 括号中的表达式不需要节点


def p_args_expression(p):
    '''args_expression : LPAREN RPAREN
                       | LPAREN assign_expression_list RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_assign_expression_list(p):
    '''assign_expression_list : empty
                              | assign_expression
                              | assign_expression COMMA assign_expression_list'''
    print("Assign expression list parsed.")

    if len(p) == 2:
        if p[1] is not None:
            p[0] = [p[1]]  # 如果只有一个赋值表达式，则直接存储在列表中
        else:
            p[0] = []  # 如果是空的，直接初始化一个空列表
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]  # 如果有多个赋值表达式，则将当前表达式和后面的表达式列表合并

def p_num_expression(p):
    '''num_expression : INT_CONST
                      | FLOAT_CONST
                      | function_num_expression'''
    p[0] = p[1]


def p_function_num_expression(p):
    '''function_num_expression : LENGTH LPAREN ID DOT ADJ LBRACKET ID RBRACKET RPAREN'''
    p[0] = NodeFunctionNum(p[3],p[7])


def p_error(p):
    if p:
        print("Syntax error:")
        print(f"    p.type: {p.type}")
        print(f"    p.value: {p.value}")
        print(f"    p.lineno: {p.lineno}")
        print(f"    p.lexpos: {p.lexpos}")
    else:
        print("Syntax error: unexpected end of input")


# Build the parser
parser = yacc.yacc()

# Test the parser
parser.parse(content)
