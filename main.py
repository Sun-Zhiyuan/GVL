from ply import lex
file_name = "input.txt"

try:
    with open(file_name, 'r') as file:
        # 读取文件内容
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"文件 '{file_name}' 不存在.")
except Exception as e:
    print(f"发生了错误: {e}")

# 定义词法分析器规则
tokens = (
    'ID',
    'IF',
    'ELSE',
    'WHILE',
)

# 关键字
keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    # 其他关键字
}

# 正则表达式规则
def t_KEYWORD(t):
    r'if|else|while'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'ID')  # 如果是关键字则替换类型为对应的关键字类型
    return t

# 忽略空格和制表符
t_ignore = ' \t'

# 创建词法分析器
lexer = lex.lex()

# 测试输入
input_data = content

# 输入词法分析器
lexer.input(input_data)

# 打印识别到的词法单元
for token in lexer:
    print(token)

output_file_path = "output.txt.txt"
with open(output_file_path, 'w') as output_file:
    print(lexer, file=output_file)