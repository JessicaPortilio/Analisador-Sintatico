import ply.yacc as yacc
from lexico import tokens
import sintaxeabstrata as sa

# Gramática
# programa : listadecomandos
# listadecomandos : comando
#                | listadecomandos comando
# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE
# expressao : expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO

#########################################################################

# Definindo as regras da gramática
precedence = (('left', 'MAIS', 'MENOS'),
              ('left', 'DIVIDE', 'VEZES'),
            )
# programa : listadecomandos
def p_programa(p):
    '''programa : listadecomandos'''
    p[0] = sa.Programa(p[1])

#########################################################################

# listadecomandos : comando
#                | listadecomandos comando
def p_listadecomandos(p):
    '''listadecomandos : comando
                      | listadecomandos comando'''
    if len(p) == 2:
        p[0] = sa.UmComando(p[1])
    else:
        p[0] = sa.MaisdeUmComando(p[1], p[2])

#########################################################################

#comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
def p_comando_declaracaovariavel(p):
    '''comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.DeclaracaoVariavel(p[2], p[4])
# comando : ID ATRIBUICAO expressao PONTOEVIRGULA
def p_comando_atribuicao(p):
    '''comando : ID ATRIBUICAO expressao PONTOEVIRGULA'''
    p[0] = sa.AtribuicaoVariavel(p[1], p[3])
# comando :IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
def p_comando_expressaoIF(p):
    '''comando : IF expressao THEN listadecomandos ELSE listadecomandos ENDIF'''
    p[0] = sa.expressaoIF(p[2], p[4], p[6])
# comando : WHILE expressao DO listadecomandos ENDWHILE
def p_comando_expressaoWhile(p):
    '''comando : WHILE expressao DO listadecomandos ENDWHILE'''
    p[0] = sa.expressaoWhile(p[2], p[4])

#########################################################################

# expressao : expressao MAIS expressao
def p_comando_maisExpressao(p):
    '''expressao : expressao MAIS expressao'''
    p[0] = sa.maisExpressao(p[1], p[3])

# expressao : expressao MENOS expressao
def p_comando_menosExpressao(p):
    '''expressao : expressao MENOS expressao'''
    p[0] = sa.menosExpressao(p[1], p[3])

# expressao : expressao VEZES expressao
def p_comando_vezesExpressao(p):
    '''expressao : expressao VEZES expressao'''
    p[0] = sa.vezesExpressao(p[1], p[3])

# expressao : expressao DIVIDE expressao
def p_comando_divideExpressao(p):
    '''expressao : expressao DIVIDE expressao'''
    p[0] = sa.divideExpressao(p[1], p[3])

# expressao : ID
def p_comando_idExpressao(p):
    '''expressao : ID'''
    p[0] = sa.idExpressao(p[1])

# expressao : NUMERO
def p_comando_numeroExpressao(p):
    '''expressao : NUMERO'''
    p[0] = sa.numeroExpressao(p[1])

###############################################
# Gerando a árvore sintática abstrata
# Gerando a árvore sintática abstrata
def parse_programa(input_string):
    parser = yacc.yacc()
    return parser.parse(input_string)

# Testando o parser
input_string = """
VAR x = 5;
VAR y = 3;
WHILE x + 0 DO
    x = x - y;
    IF x + 2 THEN
        y = y * 2;
    ELSE
        y = y + 1;
    ENDIF
ENDWHILE
"""
abstract_syntax_tree = parse_programa(input_string)

abstract_syntax_tree.print()