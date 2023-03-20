import ply.lex as lex

# Lista de tokens
reservadas = [
    'IF',
    'THEN',
    'ELSE',
    'ENDIF',
    'WHILE',
    'DO',
    'ENDWHILE',
    'VAR',
]

tokens = [
    'ID',
    'NUMERO',
    'MAIS',
    'MENOS',
    'VEZES',
    'DIVIDE',
    'ATRIBUICAO',
    'PONTOEVIRGULA',
]

tokens = tokens + reservadas

# Expressões regulares para cada token
t_MAIS      = r'\+'
t_MENOS     = r'-'
t_VEZES     = r'\*'
t_DIVIDE    = r'/'
t_ATRIBUICAO    = r'='
t_PONTOEVIRGULA = r';'
t_IF        = r'IF'
t_THEN      = r'THEN'
t_ELSE      = r'ELSE'
t_ENDIF     = r'ENDIF'
t_WHILE     = r'WHILE'
t_DO        = r'DO'
t_ENDWHILE  = r'ENDWHILE'
t_VAR       = r'VAR'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = t.value 
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorando espaços e quebras de linha
t_ignore = ' \t\n'

# Função de erro
def t_error(t):
    print(f"Caractere ilegal {t.value[0]!r} na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Criando o analisador léxico
lexer = lex.lex()