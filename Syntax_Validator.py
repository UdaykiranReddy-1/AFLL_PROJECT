'''
S -> IF A | IF A ELSE {B} | IF A ELSEIF A ELSE {B}
A -> (C){S|B}
B -> statements; | statements | statement; | statement
C -> E | F | G
ID -> [a-zA-z]
NUM -> [0-9]
ALNUM -> ID | NUM 
E -> ID=ID | ID=NUM
F -> ID==ALNUM |  ID!=ALNUM | ID>ALNUM | ID<ALNUM | ID>=ALNUM | ID<=ALNUM
G -> ID++ | ID-- | ++ID | --ID
'''

import ply.lex as lex
import ply.yacc as yacc

tokens = [  'newline',
            'ID',
            'LPAREN',
          'RPAREN', 
          'curlyopenbracket', 
          'curlyclosebracket', 
          'semicolon',
          'EQUALS',
        'GREATER_THAN_OR_EQUAL_TO',
        'LESSER_THAN_OR_EQUAL_TO',
        'GREATER_THAN',
        'LESSER_THAN',
        'INCREMENT',
        'DECREMENT',
        'ASSIGN',
        'NUMBER',
        'NOTEQUALS' ]

reserved = {
    'if': 'if',
    'elseif': 'elseif',
    'else':'else',
    'statement':'statement',
    'statements':'statements',
    }

t_ignore = ' \t'
t_newline = ' \\n'
t_curlyopenbracket = r'\{'
t_curlyclosebracket = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_semicolon = r';'
t_ASSIGN = r'\='
t_EQUALS = r'\=='
t_NOTEQUALS = r'\!='
t_GREATER_THAN_OR_EQUAL_TO = r'\>='
t_LESSER_THAN_OR_EQUAL_TO = r'\<='
t_GREATER_THAN = r'\>'
t_LESSER_THAN = r'\<'
t_INCREMENT = r'\++'
t_DECREMENT = r'\--'
t_NUMBER = r'\d+'

tokens += list(reserved.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_if(t):
    r'if'
    return t

def t_elseif(t):
    r'elseif'
    return t

def t_else(t):
    r'else'
    return t

def t_statement(t):
    r'statement'
    return t

def t_statements(t):
    r'statements'
    return t

def p_if_loop(p):
    '''assign : if expression
    | if expression newline else statementsub
    | if expression else statementsub
    | if expression newline elseif expression newline else statementsub
    | if expression newline elseif expression else statementsub
    | if expression elseif expression newline else statementsub
    | if expression elseif expression else statementsub
    | if expression elseif expression
    | if expression newline elseif expression'''
    print("Syntax is correct.")

def p_if_nested(p):
    '''if_nested : if expression
    | if expression newline
    | if expression newline else statementsub
    | if expression newline else statementsub newline
    | if expression else statementsub
    | if expression else statementsub newline
    | if expression newline elseif expression newline else statementsub
    | if expression newline elseif expression else statementsub
    | if expression elseif expression newline else statementsub
    | if expression elseif expression else statementsub
    | if expression elseif expression
    | if expression newline elseif expression'''

def p_expression(p):
    '''expression : conditionsub statementsub'''


def p_conditionsub(p):
    '''conditionsub : LPAREN condition RPAREN 
                    | LPAREN assign RPAREN
                    | newline LPAREN condition RPAREN
                    '''

def p_statementsub(p):
    '''statementsub : curlyopenbracket newline statements semicolon newline curlyclosebracket
                    | curlyopenbracket newline statements newline curlyclosebracket
                    | curlyopenbracket statement semicolon curlyclosebracket
                    | curlyopenbracket statement curlyclosebracket
                    | newline curlyopenbracket statements semicolon curlyclosebracket
                    | newline curlyopenbracket statements semicolon newline curlyclosebracket
                    | newline curlyopenbracket statements curlyclosebracket
                    | newline curlyopenbracket statements newline curlyclosebracket
                    | newline curlyopenbracket newline statements semicolon curlyclosebracket
                    | newline curlyopenbracket newline statements semicolon newline curlyclosebracket
                    | newline curlyopenbracket newline statements curlyclosebracket
                    | newline curlyopenbracket newline statements newline curlyclosebracket
                    | curlyopenbracket newline if_nested newline curlyclosebracket
                    | curlyopenbracket newline if_nested curlyclosebracket
                    | curlyopenbracket if_nested curlyclosebracket
                    | newline curlyopenbracket if_nested curlyclosebracket
                    | newline curlyopenbracket if_nested newline curlyclosebracket
                    | newline curlyopenbracket newline if_nested curlyclosebracket
                    | newline curlyopenbracket newline if_nested newline curlyclosebracket
                ''' 
def p_condition(p):
    '''condition : Assign
                | Check
                | Action'''

def p_condition_part_one(p):
    '''Assign : ID ASSIGN ID
              | ID ASSIGN NUMBER'''

def p_condition_part_two(p):
    '''Check : ID EQUALS Alnum
             | ID NOTEQUALS Alnum
             | ID GREATER_THAN Alnum
             | ID LESSER_THAN Alnum
             | ID GREATER_THAN_OR_EQUAL_TO Alnum
             | ID LESSER_THAN_OR_EQUAL_TO Alnum'''

def p_condition_part_three(p):
    '''Action : ID INCREMENT
              | ID DECREMENT
              | INCREMENT ID
              | DECREMENT ID
              | ID ASSIGN ID'''

def p_alnum(p):
    '''Alnum : ID
             | NUMBER'''

def p_error(p):
    print("Syntax error")
    quit()
def t_error(p):
    print("Token error,")

lex.lex()
yacc.yacc()

data = '''if(!=1){
    statements;
}
else{
    statements;
}'''

yacc.parse(data)
