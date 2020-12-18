import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'INT',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
)

t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_ignore  = ' \n'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    pass

lexer = lex.lex()

def p_multiply(p):
    'expr : expr TIMES factor'
    p[0] = p[1] * p[3]

def p_expr_factor(p):
    'expr : factor'
    p[0] = p[1]

def p_num(p):
    'term : INT'
    p[0] = p[1]

def p_add(p):
    'factor : factor PLUS term'
    p[0] = p[1] + p[3]

def p_factor_term(p):
    'factor : term'
    p[0] = p[1]

def p_parens(p):
    'term : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error(p):
    pass

parser = yacc.yacc()

with open('input18') as fd:
    print(sum(parser.parse(expr) for expr in fd.readlines()))
