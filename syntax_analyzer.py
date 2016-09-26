import re

def initialize_keywords():
    global keywords
    keywords = {}
    keywords["algoritmo"] = "algoritmo"
    keywords["finalgoritmo"] = "finalgoritmo"
    keywords["proceso"] = "proceso"
    keywords["finproceso"] = "finproceso"
    keywords["definir"] = "definir"
    keywords["como"] = "como"
    keywords["numero"] = "numero"
    keywords["numerico"] = "numerico"
    keywords["entero"] = "entero"
    keywords["caracter"] = "caracter"
    keywords["real"] = "real"
    keywords["logico"] = "logico"
    keywords["texto"] = "texto"
    keywords["cadena"] = "cadena"
    keywords["verdadero"] = "verdadero"
    keywords["falso"] = "falso"
    keywords["leer"] = "leer"
    keywords["escribir"] = "escribir"
    keywords["dimension"] = "dimension"
    keywords["para"] = "para"
    keywords["hasta"] = "hasta"
    keywords["con"] = "con"
    keywords["paso"] = "paso"
    keywords["hacer"] = "hacer"
    keywords["finpara"] = "finpara"
    keywords["borrar"] = "borrar"
    keywords["pantalla"] = "pantalla"
    keywords["esperar"] = "esperar"
    keywords["tecla"] = "tecla"
    keywords["segundos"] = "segundos"
    keywords["milisegundos"] = "milisegundos"
    keywords["si"] = "si"
    keywords["entonces"] = "entonces"
    keywords["sino"] = "sino"
    keywords["finsi"] = "finsi"
    keywords["segun"] = "segun"
    keywords["caso"] = "caso"
    keywords["de"] = "de"
    keywords["otro"] = "otro"
    keywords["modo"] = "modo"
    keywords["finsegun"] = "finsegun"
    keywords["mientras"] = "mientras"
    keywords["finmientras"] = "finmientras"
    keywords["repetir"] = "repetir"
    keywords["hasta"] = "hasta"
    keywords["que"] = "que"
    keywords["subproceso"] = "subproceso"
    keywords["finsubproceso"] = "finsubproceso"
    keywords["funcion"] = "funcion"
    keywords["finfuncion"] = "finfuncion"

    #Operators as keywords
    keywords["mod"] = "mod"
    keywords["no"] = "no"


def initialize_operators():
    global operators
    operators = {}
    operators["~"] = "token_neg"
    operators["="] = "token_igual"
    operators["<-"] = "token_asig"
    operators["<>"] = "token_dif"
    operators["<"] = "token_menor"
    operators[">"] = "token_mayor"
    operators["<="] = "token_menor_igual"
    operators[">="] = "token_mayor_igual"

    operators["+"] = "token_mas"
    operators["-"] = "token_menos"
    operators["/"] = "token_div"
    operators["*"] = "token_mul"
    operators["%"] = "token_mod"
    operators[";"] = "token_pyc"
    operators[":"] = "token_dosp"
    operators["("] = "token_par_izq"
    operators[")"] = "token_par_der"
    operators["["] = "token_cor_izq"
    operators["]"] = "token_cor_der"
    operators["|"] = "token_o"
    operators["&"] = "token_y"
    operators["o"] = "token_o"
    operators[","] = "token_coma"
    operators["^"] = "token_pot"

    operators["y"] = "token_y"
    operators["no"] = "token_neg"
    operators["mod"] = "token_mod"

def initialize_alias():
    global alias
    alias.append(['algoritmo', 'algoritmo'])
    alias.append(['borrar', 'borrar'])
    alias.append(['cadena', 'cadena'])
    alias.append(['caracter', 'caracter'])
    alias.append(['caso', 'caso'])
    alias.append(['como', 'como'])
    alias.append(['con', 'con'])
    alias.append(['de', 'de'])
    alias.append(['definir', 'definir'])
    alias.append(['dimension', 'dimension'])
    alias.append(['entero', 'entero'])
    alias.append(['entonces', 'entonces'])
    alias.append(['escribir', 'escribir'])
    alias.append(['esperar', 'esperar'])
    alias.append(['falso', 'falso'])
    alias.append(['finalgoritmo', 'finalgoritmo'])
    alias.append(['finfuncion', 'finfuncion'])
    alias.append(['finmientras', 'finmientras'])
    alias.append(['finpara', 'finpara'])
    alias.append(['finproceso', 'finproceso'])
    alias.append(['finsegun', 'finsegun'])
    alias.append(['finsi', 'finsi'])
    alias.append(['finsubproceso', 'finsubproceso'])
    alias.append(['funcion', 'funcion'])
    alias.append(['hacer', 'hacer'])
    alias.append(['hasta', 'hasta'])
    alias.append(['id', 'identificador'])
    alias.append(['leer', 'leer'])
    alias.append(['limpiar', 'limpiar'])
    alias.append(['logico', 'logico'])
    alias.append(['mientras', 'mientras'])
    alias.append(['milisegundos', 'milisegundos'])
    alias.append(['modo', 'modo'])
    alias.append(['numerico', 'numerico'])
    alias.append(['numero', 'numero'])
    alias.append(['otro', 'otro'])
    alias.append(['pantalla', 'pantalla'])
    alias.append(['para', 'para'])
    alias.append(['paso', 'paso'])
    alias.append(['proceso', 'proceso'])
    alias.append(['que', 'que'])
    alias.append(['real', 'real'])
    alias.append(['repetir', 'repetir'])
    alias.append(['segun', 'segun'])
    alias.append(['segundos', 'segundos'])
    alias.append(['si', 'si'])
    alias.append(['sino', 'sino'])
    alias.append(['subproceso', 'subproceso'])
    alias.append(['tecla', 'tecla'])
    alias.append(['texto', 'texto'])
    alias.append(['token_asig', '<-'])
    alias.append(['token_cadena', 'valor_cadena'])
    alias.append(['token_coma', ','])
    alias.append(['token_cor_der', ']'])
    alias.append(['token_cor_izq', '['])
    alias.append(['token_dif', '<>'])
    alias.append(['token_div', '/'])
    alias.append(['token_dosp', ':'])
    alias.append(['token_entero', 'valor_entero'])
    alias.append(['token_igual', '='])
    alias.append(['token_mas', '+'])
    alias.append(['token_mayor', '>'])
    alias.append(['token_mayor_igual', '>='])
    alias.append(['token_menor', '<'])
    alias.append(['token_menor_igual', '<='])
    alias.append(['token_menos', '-'])
    alias.append(['token_mod', '%'])
    alias.append(['token_mul', '*'])
    alias.append(['token_neg', '~'])
    alias.append(['token_o', '|'])
    alias.append(['token_par_der', ')'])
    alias.append(['token_par_izq', '('])
    alias.append(['token_pot', '^'])
    alias.append(['token_pyc', ';'])
    alias.append(['token_real', 'valor_real'])
    alias.append(['token_y', '&'])
    alias.append(['verdadero', 'verdadero'])


#####################################################################################################
############################################### LEXER ###############################################
#####################################################################################################

def is_other(character):
    return re.match("[ \t\n]", character)


def is_digit(character):
    return re.match("[0-9]", character)


def is_letter(character):
    return re.match("[a-zA-Z]", character)

def is_operator(character):
    global operators

    return character in operators


def is_string(character):
    return character == "\"" or character == "'"


def lex_error():
    global row, col
    return ">>> Error lexico (linea: " + str(row + 1) + ", posicion: " + str(col + 1) + ")"


def read_comment(line):
    global row, col

    length_line = len(line)

    token = None
    advance = 0

    index = col
    if index + 1 < length_line and line[index + 1] == "/": # It's a comment
        token = line[index:]
        advance = len(token)

    return token, advance


def read_number(line):
    global row, col

    length_line = len(line)
    index = col
    token = None
    advance = 0

    while index < length_line:
        character = line[index]

        if is_digit(character) or character == ".":
            index += 1
        elif is_operator(character) or is_other(character): # Read integer number
            break
        else:
            return None, 0  # Lexer error

    token = line[col:index]
    advance = len(token)
    return token, advance

def read_identifier(line):
    global row, col

    length_line = len(line)

    token = ""
    advance = 0

    index = col

    while index < length_line:
        character = line[index]

        if is_letter(character) or is_digit(character) or character == "_":
            index += 1
            token += character
        else:
            break

    if token is not None:
        advance = len(token)

    return token, advance


def read_keyword_identifier(line):
    global row, col, keywords

    length_line = len(line)

    index = col

    token = None
    advance = 0
    type = None

    while index < length_line:
        character = line[index]

        if not is_letter(character):
            if is_digit(character) or character == "_":
                token, advance = read_identifier(line)
                type = "id"
            else:
                value = line[col:index:].lower()
                if value in keywords:
                    token = keywords[value]
                    advance = len(token)
                    type = "token_keyword"
                else:
                    token, advance = read_identifier(line)
                    type = "id"
            break
        else:
            index += 1

    if index == length_line:
        value = line[col:index:].lower()
        if value in keywords:
            token = keywords[value]
            advance = len(token)
            type = "token_keyword"
        else:
            token, advance = read_identifier(line)
            type = "id"

    return type, token, advance


def read_operator(line):
    global row, col

    length_line = len(line)

    index = col

    token = None
    advance = 0

    if index + 1 < length_line and is_operator(line[index:index + 2: 1]):
        token = line[index:index + 2:]
        advance = 2
    else:
        token = line[index]
        advance = 1

    return token, advance


def read_string(line):
    global row, col
    length_line = len(line)

    advance = 0
    token = None
    index = col + 1 # Skip quote or apostrophe

    while index < length_line:
        if line[index] == "\"" or line[index] == "'":
            token = line[col + 1:index]
            return token, len(token) + 2

        index += 1

    return token, advance

def next_token(line):
    global col, operators

    character = line[col]

    type = None
    token = None
    advance = 0

    # End line there is not token
    if col == len(line):
        token = ""
        advance = 0
        type = "fin_linea"

    # Space, tab or end line
    if token is None and is_other(character):
        token = character
        advance = 1
        type = "token_otro"

    # Could be a comment
    if token is None and character == "/":
        token, advance = read_comment(line)
        if token is not None:
            type = "token_comentario"

    # Integer or real number
    if token is None and is_digit(character):
        token, advance = read_number(line)
        if token is not None:
            #Not sure about this (pseint read it right)
            if token[-1] == ".":
                type = "lex_error"
            else:
                type = "token_real" if "." in token else "token_entero"

    # String
    if token is None and is_string(character):
        token, advance = read_string(line)
        if token is not None:
            type = "token_cadena"

    # Keyword or identifier
    if token is None and is_letter(character):
        type, token, advance = read_keyword_identifier(line)

    # Operator
    if token is None and is_operator(character):
        token, advance = read_operator(line)
        if token is not None:
            type = operators[token]

    if token is None:
        type = "lex_error"
        return type, token, row, col
    else:
        index = col
        col += advance
        return type, token, row, index


def build_token(title, lexema, r, c):
    global keywords, operators

    token = "<"

    if lexema in keywords:
        if lexema not in operators:
            token += lexema
        else:
            token += operators[lexema]
    elif lexema in operators:
        token += title
    else:
        token += title + "," + lexema.lower()

    token += "," + str(r) + "," + str(c) + ">"

    return token


class Token(object):
    def __init__(self, title = None, lexema = None, r = None, c = None):
        global keywords, operators
        if title != None:
            if lexema in keywords:
                if lexema not in operators:
                    self.lexema = lexema
                    self.type = lexema
                else:
                    self.lexema = operators[lexema]
                    self.type = operators[lexema]
            elif lexema in operators:
                self.type = title
                self.lexema = lexema
            else:
                self.lexema = lexema.lower() if lexema != "EOF" else "EOF"
                self.type = title

            self.row = r
            self.col = c

current_token = 0
def get_next_token():
    global current_token, tokens
    c = current_token
    current_token += 1
    return tokens[c]


def generate_tokens(input = None, output = None):
    global tokens, row, col

    lines = []
    if input != None:
        stdin = open(input, "r")
        lines = stdin.readlines()
    if output != None:
        stdout = open(output, "w")

    tokens = []
    type = ""

    for line in lines:
        while col < len(line) and type is not "lex_error":
            type, token, x, y = next_token(line)
            if type is not "token_otro" and type is not "lex_error" and type is not "token_comentario":
                #print build_token(type, token, x + 1, y + 1)
                #if output != None:
                #    stdout.write(build_token(type, token, x + 1, y + 1) + "\n")
                tokens.append(Token(type, token, x + 1, y + 1))

        if type is "lex_error":
            #print lex_error()
            #if output != None:
            #    stdout.write(lex_error() + "\n")
            return

        row += 1
        col = 0
    tokens.append(Token("EOF", "EOF", row + 1, col + 1))

tokens = []
alias = []
keywords = {}
operators = {}
initialize_keywords()
initialize_operators()
initialize_alias()
row = 0
col = 0
def generate_prediction_sets(grammar):
    global expected
    grammar_array = grammar.split(";")
    for g in grammar_array:
        temp = g.split(":")
        rule = temp[0]
        left_part = rule.split("->")[0]
        pred = temp[1]
        predictions[rule] = pred.split(",")
        if left_part not in expected:
            expected[left_part] = {}
        for p in predictions[rule]:
            expected[left_part][p] = True

def syntax_error(expec, token, error_syntax_in_match):
    error = ""
    error += "<" + str(token.row) + "," + str(token.col) + "> Error sintactico: se encontro: \"" + token.lexema + "\"; se esperaba: "
    if error_syntax_in_match:
        error += "\"" + expec + "\". "
    else:
        for e in alias:
            if e[0] in expected[expec]:
                error += "\"" + e[1] + "\", "
    return error[:-2] + "."

def match(expected_token):
    global token
    if token.type == expected_token:
        token = get_next_token()
    else:
        print syntax_error(expected_token, token, True)
        return False
    return True

def PSEINT():
    global token
    if token.type in predictions["PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC"]:
        if not FUNCION_SUBPROC():
            return False
        if not PROCESO():
            return False
        if not FUNCION_SUBPROC():
            return False
    elif "PSEINT->epsilon" in predictions:
        return True
    else:
        print syntax_error("PSEINT", token, False)
        return False
    return True

def FUNCION_SUBPROC():
    global token
    if token.type in predictions["FUNCION_SUBPROC->PROC-FUNCION_SUBPROC"]:
        if not PROC():
            return False
        if not FUNCION_SUBPROC():
            return False
    elif "FUNCION_SUBPROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("FUNCION_SUBPROC", token, False)
        return False
    return True

def PROCESO():
    global token
    if token.type in predictions["PROCESO->INICIO_PROCESO-id-BLOQUE_PROCESO"]:
        if not INICIO_PROCESO():
            return False
        if not match("id"):
            return False
        if not BLOQUE_PROCESO():
            return False
    elif "PROCESO->epsilon" in predictions:
        return True
    else:
        print syntax_error("PROCESO", token, False)
        return False
    return True

def INICIO_PROCESO():
    global token
    if token.type in predictions["INICIO_PROCESO->proceso"]:
        if not match("proceso"):
            return False
    elif token.type in predictions["INICIO_PROCESO->algoritmo"]:
        if not match("algoritmo"):
            return False
    elif "INICIO_PROCESO->epsilon" in predictions:
        return True
    else:
        print syntax_error("INICIO_PROCESO", token, False)
        return False
    return True

def BLOQUE_PROCESO():
    global token
    if token.type in predictions["BLOQUE_PROCESO->BLOQUE-FIN_PROCESO"]:
        if not BLOQUE():
            return False
        if not FIN_PROCESO():
            return False
    elif "BLOQUE_PROCESO->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_PROCESO", token, False)
        return False
    return True

def FIN_PROCESO():
    global token
    if token.type in predictions["FIN_PROCESO->finproceso"]:
        if not match("finproceso"):
            return False
    elif token.type in predictions["FIN_PROCESO->finalgoritmo"]:
        if not match("finalgoritmo"):
            return False
    elif "FIN_PROCESO->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_PROCESO", token, False)
        return False
    return True

def PROC():
    global token
    if token.type in predictions["PROC->INICIO_PROC-id-FIRMA-BLOQUE_PROC"]:
        if not INICIO_PROC():
            return False
        if not match("id"):
            return False
        if not FIRMA():
            return False
        if not BLOQUE_PROC():
            return False
    elif "PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("PROC", token, False)
        return False
    return True

def INICIO_PROC():
    global token
    if token.type in predictions["INICIO_PROC->funcion"]:
        if not match("funcion"):
            return False
    elif token.type in predictions["INICIO_PROC->subproceso"]:
        if not match("subproceso"):
            return False
    elif "INICIO_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("INICIO_PROC", token, False)
        return False
    return True

def BLOQUE_PROC():
    global token
    if token.type in predictions["BLOQUE_PROC->BLOQUE-FIN_PROC"]:
        if not BLOQUE():
            return False
        if not FIN_PROC():
            return False
    elif "BLOQUE_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_PROC", token, False)
        return False
    return True

def FIN_PROC():
    global token
    if token.type in predictions["FIN_PROC->finfuncion"]:
        if not match("finfuncion"):
            return False
    elif token.type in predictions["FIN_PROC->finsubproceso"]:
        if not match("finsubproceso"):
            return False
    elif "FIN_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_PROC", token, False)
        return False
    return True

def FIRMA():
    global token
    if token.type in predictions["FIRMA->token_asig-id-ARG_PROC"]:
        if not match("token_asig"):
            return False
        if not match("id"):
            return False
        if not ARG_PROC():
            return False
    elif token.type in predictions["FIRMA->ARG_PROC"]:
        if not ARG_PROC():
            return False
    elif "FIRMA->epsilon" in predictions:
        return True
    else:
        print syntax_error("FIRMA", token, False)
        return False
    return True

def ARG_PROC():
    global token
    if token.type in predictions["ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der"]:
        if not match("token_par_izq"):
            return False
        if not LISTA_ARG_PROC():
            return False
        if not match("token_par_der"):
            return False
    elif "ARG_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("ARG_PROC", token, False)
        return False
    return True

def LISTA_ARG_PROC():
    global token
    if token.type in predictions["LISTA_ARG_PROC->id-LISTA_ARG_PROC1"]:
        if not match("id"):
            return False
        if not LISTA_ARG_PROC1():
            return False
    elif "LISTA_ARG_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_ARG_PROC", token, False)
        return False
    return True

def LISTA_ARG_PROC1():
    global token
    if token.type in predictions["LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1"]:
        if not match("token_coma"):
            return False
        if not match("id"):
            return False
        if not LISTA_ARG_PROC1():
            return False
    elif "LISTA_ARG_PROC1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_ARG_PROC1", token, False)
        return False
    return True

def BLOQUE():
    global token
    if token.type in predictions["BLOQUE->DECLARACION-BLOQUE"]:
        if not DECLARACION():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->ASIGNACION-BLOQUE"]:
        if not ASIGNACION():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->DIMENSION-BLOQUE"]:
        if not DIMENSION():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->SI-BLOQUE"]:
        if not SI():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->PARA-BLOQUE"]:
        if not PARA():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->MIENTRAS-BLOQUE"]:
        if not MIENTRAS():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->REPETIR-BLOQUE"]:
        if not REPETIR():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->SEGUN-BLOQUE"]:
        if not SEGUN():
            return False
        if not BLOQUE():
            return False
    elif token.type in predictions["BLOQUE->OTRO-BLOQUE"]:
        if not OTRO():
            return False
        if not BLOQUE():
            return False
    elif "BLOQUE->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE", token, False)
        return False
    return True

def DECLARACION():
    global token
    if token.type in predictions["DECLARACION->definir-LISTA_ID-como-TIPO_DATO-token_pyc"]:
        if not match("definir"):
            return False
        if not LISTA_ID():
            return False
        if not match("como"):
            return False
        if not TIPO_DATO():
            return False
        if not match("token_pyc"):
            return False
    elif "DECLARACION->epsilon" in predictions:
        return True
    else:
        print syntax_error("DECLARACION", token, False)
        return False
    return True

def ASIGNACION():
    global token
    if token.type in predictions["ASIGNACION->id-ASIGNACION1"]:
        if not match("id"):
            return False
        if not ASIGNACION1():
            return False
    elif "ASIGNACION->epsilon" in predictions:
        return True
    else:
        print syntax_error("ASIGNACION", token, False)
        return False
    return True

def ASIGNACION1():
    global token
    if token.type in predictions["ASIGNACION1->token_cor_izq-LISTA_EXPR-token_cor_der-token_asig-EXPRESION-token_pyc"]:
        if not match("token_cor_izq"):
            return False
        if not LISTA_EXPR():
            return False
        if not match("token_cor_der"):
            return False
        if not match("token_asig"):
            return False
        if not EXPRESION():
            return False
        if not match("token_pyc"):
            return False
    elif token.type in predictions["ASIGNACION1->token_asig-EXPRESION-token_pyc"]:
        if not match("token_asig"):
            return False
        if not EXPRESION():
            return False
        if not match("token_pyc"):
            return False
    elif "ASIGNACION1->epsilon" in predictions:
        return True
    else:
        print syntax_error("ASIGNACION1", token, False)
        return False
    return True

def DIMENSION():
    global token
    if token.type in predictions["DIMENSION->dimension-id-token_cor_izq-LISTA_EXPR-token_cor_der-token_pyc"]:
        if not match("dimension"):
            return False
        if not match("id"):
            return False
        if not match("token_cor_izq"):
            return False
        if not LISTA_EXPR():
            return False
        if not match("token_cor_der"):
            return False
        if not match("token_pyc"):
            return False
    elif "DIMENSION->epsilon" in predictions:
        return True
    else:
        print syntax_error("DIMENSION", token, False)
        return False
    return True

def SI():
    global token
    if token.type in predictions["SI->si-EXPRESION-entonces-BLOQUE_SI"]:
        if not match("si"):
            return False
        if not EXPRESION():
            return False
        if not match("entonces"):
            return False
        if not BLOQUE_SI():
            return False
    elif "SI->epsilon" in predictions:
        return True
    else:
        print syntax_error("SI", token, False)
        return False
    return True

def BLOQUE_SI():
    global token
    if token.type in predictions["BLOQUE_SI->BLOQUE-SI1"]:
        if not BLOQUE():
            return False
        if not SI1():
            return False
    elif "BLOQUE_SI->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_SI", token, False)
        return False
    return True

def SI1():
    global token
    if token.type in predictions["SI1->sino-BLOQUE_SI1"]:
        if not match("sino"):
            return False
        if not BLOQUE_SI1():
            return False
    elif token.type in predictions["SI1->finsi"]:
        if not match("finsi"):
            return False
    elif "SI1->epsilon" in predictions:
        return True
    else:
        print syntax_error("SI1", token, False)
        return False
    return True

def BLOQUE_SI1():
    global token
    if token.type in predictions["BLOQUE_SI1->BLOQUE-finsi"]:
        if not BLOQUE():
            return False
        if not match("finsi"):
            return False
    elif "BLOQUE_SI1->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_SI1", token, False)
        return False
    return True

def PARA():
    global token
    if token.type in predictions["PARA->para-id-token_asig-EXPRESION-hasta-EXPRESION-con-paso-EXPRESION-hacer-BLOQUE_PARA"]:
        if not match("para"):
            return False
        if not match("id"):
            return False
        if not match("token_asig"):
            return False
        if not EXPRESION():
            return False
        if not match("hasta"):
            return False
        if not EXPRESION():
            return False
        if not match("con"):
            return False
        if not match("paso"):
            return False
        if not EXPRESION():
            return False
        if not match("hacer"):
            return False
        if not BLOQUE_PARA():
            return False
    elif "PARA->epsilon" in predictions:
        return True
    else:
        print syntax_error("PARA", token, False)
        return False
    return True

def BLOQUE_PARA():
    global token
    if token.type in predictions["BLOQUE_PARA->BLOQUE-finpara"]:
        if not BLOQUE():
            return False
        if not match("finpara"):
            return False
    elif "BLOQUE_PARA->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_PARA", token, False)
        return False
    return True

def MIENTRAS():
    global token
    if token.type in predictions["MIENTRAS->mientras-EXPRESION-hacer-BLOQUE_MIENTRAS"]:
        if not match("mientras"):
            return False
        if not EXPRESION():
            return False
        if not match("hacer"):
            return False
        if not BLOQUE_MIENTRAS():
            return False
    elif "MIENTRAS->epsilon" in predictions:
        return True
    else:
        print syntax_error("MIENTRAS", token, False)
        return False
    return True

def BLOQUE_MIENTRAS():
    global token
    if token.type in predictions["BLOQUE_MIENTRAS->BLOQUE-finmientras"]:
        if not BLOQUE():
            return False
        if not match("finmientras"):
            return False
    elif "BLOQUE_MIENTRAS->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_MIENTRAS", token, False)
        return False
    return True

def REPETIR():
    global token
    if token.type in predictions["REPETIR->repetir-BLOQUE_REPETIR"]:
        if not match("repetir"):
            return False
        if not BLOQUE_REPETIR():
            return False
    elif "REPETIR->epsilon" in predictions:
        return True
    else:
        print syntax_error("REPETIR", token, False)
        return False
    return True

def BLOQUE_REPETIR():
    global token
    if token.type in predictions["BLOQUE_REPETIR->BLOQUE-hasta-que-EXPRESION"]:
        if not BLOQUE():
            return False
        if not match("hasta"):
            return False
        if not match("que"):
            return False
        if not EXPRESION():
            return False
    elif "BLOQUE_REPETIR->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_REPETIR", token, False)
        return False
    return True

def SEGUN():
    global token
    if token.type in predictions["SEGUN->segun-EXPRESION-hacer-CASO_LISTA"]:
        if not match("segun"):
            return False
        if not EXPRESION():
            return False
        if not match("hacer"):
            return False
        if not CASO_LISTA():
            return False
    elif "SEGUN->epsilon" in predictions:
        return True
    else:
        print syntax_error("SEGUN", token, False)
        return False
    return True

def SEGUN1():
    global token
    if token.type in predictions["SEGUN1->finsegun"]:
        if not match("finsegun"):
            return False
    elif token.type in predictions["SEGUN1->de-otro-modo-token_dosp-BLOQUE_SEGUN1"]:
        if not match("de"):
            return False
        if not match("otro"):
            return False
        if not match("modo"):
            return False
        if not match("token_dosp"):
            return False
        if not BLOQUE_SEGUN1():
            return False
    elif "SEGUN1->epsilon" in predictions:
        return True
    else:
        print syntax_error("SEGUN1", token, False)
        return False
    return True

def BLOQUE_SEGUN1():
    global token
    if token.type in predictions["BLOQUE_SEGUN1->BLOQUE-finsegun"]:
        if not BLOQUE():
            return False
        if not match("finsegun"):
            return False
    elif "BLOQUE_SEGUN1->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_SEGUN1", token, False)
        return False
    return True

def CASO_LISTA():
    global token
    if token.type in predictions["CASO_LISTA->caso-EXPRESION-token_dosp-BLOQUE_CASO_LISTA"]:
        if not match("caso"):
            return False
        if not EXPRESION():
            return False
        if not match("token_dosp"):
            return False
        if not BLOQUE_CASO_LISTA():
            return False
    elif token.type in predictions["CASO_LISTA->SEGUN1"]:
        if not SEGUN1():
            return False
    elif "CASO_LISTA->epsilon" in predictions:
        return True
    else:
        print syntax_error("CASO_LISTA", token, False)
        return False
    return True

def BLOQUE_CASO_LISTA():
    global token
    if token.type in predictions["BLOQUE_CASO_LISTA->BLOQUE-CASO_LISTA"]:
        if not BLOQUE():
            return False
        if not CASO_LISTA():
            return False
    elif "BLOQUE_CASO_LISTA->epsilon" in predictions:
        return True
    else:
        print syntax_error("BLOQUE_CASO_LISTA", token, False)
        return False
    return True

def OTRO():
    global token
    if token.type in predictions["OTRO->borrar-pantalla"]:
        if not match("borrar"):
            return False
        if not match("pantalla"):
            return False
    elif token.type in predictions["OTRO->ESCRIBIR"]:
        if not ESCRIBIR():
            return False
    elif token.type in predictions["OTRO->ESPERAR"]:
        if not ESPERAR():
            return False
    elif token.type in predictions["OTRO->LEER"]:
        if not LEER():
            return False
    elif token.type in predictions["OTRO->limpiar-pantalla"]:
        if not match("limpiar"):
            return False
        if not match("pantalla"):
            return False
    elif "OTRO->epsilon" in predictions:
        return True
    else:
        print syntax_error("OTRO", token, False)
        return False
    return True

def LISTA_EXPR():
    global token
    if token.type in predictions["LISTA_EXPR->EXPRESION-LISTA_EXPR1"]:
        if not EXPRESION():
            return False
        if not LISTA_EXPR1():
            return False
    elif token.type in predictions["LISTA_EXPR->OPERADOR-TERMINO-LISTA_EXPR"]:
        if not OPERADOR():
            return False
        if not TERMINO():
            return False
        if not LISTA_EXPR():
            return False
    elif "LISTA_EXPR->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_EXPR", token, False)
        return False
    return True

def LISTA_EXPR1():
    global token
    if token.type in predictions["LISTA_EXPR1->token_coma-LISTA_EXPR1"]:
        if not match("token_coma"):
            return False
        if not LISTA_EXPR1():
            return False
    elif token.type in predictions["LISTA_EXPR1->EXPRESION"]:
        if not EXPRESION():
            return False
    elif "LISTA_EXPR1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_EXPR1", token, False)
        return False
    return True

def LISTA_ID():
    global token
    if token.type in predictions["LISTA_ID->id-LISTA_ID1"]:
        if not match("id"):
            return False
        if not LISTA_ID1():
            return False
    elif "LISTA_ID->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_ID", token, False)
        return False
    return True

def LISTA_ID1():
    global token
    if token.type in predictions["LISTA_ID1->token_coma-id-LISTA_ID1"]:
        if not match("token_coma"):
            return False
        if not match("id"):
            return False
        if not LISTA_ID1():
            return False
    elif "LISTA_ID1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_ID1", token, False)
        return False
    return True

def ESCRIBIR():
    global token
    if token.type in predictions["ESCRIBIR->escribir-LISTA_EXPR-token_pyc"]:
        if not match("escribir"):
            return False
        if not LISTA_EXPR():
            return False
        if not match("token_pyc"):
            return False
    elif "ESCRIBIR->epsilon" in predictions:
        return True
    else:
        print syntax_error("ESCRIBIR", token, False)
        return False
    return True

def ESPERAR():
    global token
    if token.type in predictions["ESPERAR->esperar-ESPERAR1"]:
        if not match("esperar"):
            return False
        if not ESPERAR1():
            return False
    elif "ESPERAR->epsilon" in predictions:
        return True
    else:
        print syntax_error("ESPERAR", token, False)
        return False
    return True

def ESPERAR1():
    global token
    if token.type in predictions["ESPERAR1->tecla-token_pyc"]:
        if not match("tecla"):
            return False
        if not match("token_pyc"):
            return False
    elif token.type in predictions["ESPERAR1->EXPRESION-MEDIDA_TIEMPO-token_pyc"]:
        if not EXPRESION():
            return False
        if not MEDIDA_TIEMPO():
            return False
        if not match("token_pyc"):
            return False
    elif "ESPERAR1->epsilon" in predictions:
        return True
    else:
        print syntax_error("ESPERAR1", token, False)
        return False
    return True

def MEDIDA_TIEMPO():
    global token
    if token.type in predictions["MEDIDA_TIEMPO->segundos"]:
        if not match("segundos"):
            return False
    elif token.type in predictions["MEDIDA_TIEMPO->milisegundos"]:
        if not match("milisegundos"):
            return False
    elif "MEDIDA_TIEMPO->epsilon" in predictions:
        return True
    else:
        print syntax_error("MEDIDA_TIEMPO", token, False)
        return False
    return True

def LEER():
    global token
    if token.type in predictions["LEER->leer-LISTA_ID-token_pyc"]:
        if not match("leer"):
            return False
        if not LISTA_ID():
            return False
        if not match("token_pyc"):
            return False
    elif "LEER->epsilon" in predictions:
        return True
    else:
        print syntax_error("LEER", token, False)
        return False
    return True

def EXPRESION():
    global token
    if token.type in predictions["EXPRESION->TERMINO-LISTA_EXPR"]:
        if not TERMINO():
            return False
        if not LISTA_EXPR():
            return False
    elif "EXPRESION->epsilon" in predictions:
        return True
    else:
        print syntax_error("EXPRESION", token, False)
        return False
    return True

def TERMINO():
    global token
    if token.type in predictions["TERMINO->FACTOR-LISTA_FACTOR"]:
        if not FACTOR():
            return False
        if not LISTA_FACTOR():
            return False
    elif "TERMINO->epsilon" in predictions:
        return True
    else:
        print syntax_error("TERMINO", token, False)
        return False
    return True

def LISTA_FACTOR():
    global token
    if token.type in predictions["LISTA_FACTOR->OPERADOR-FACTOR-LISTA_FACTOR"]:
        if not OPERADOR():
            return False
        if not FACTOR():
            return False
        if not LISTA_FACTOR():
            return False
    elif "LISTA_FACTOR->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_FACTOR", token, False)
        return False
    return True

def FACTOR():
    global token
    if token.type in predictions["FACTOR->token_par_izq-EXPRESION-token_par_der"]:
        if not match("token_par_izq"):
            return False
        if not EXPRESION():
            return False
        if not match("token_par_der"):
            return False
    elif token.type in predictions["FACTOR->LLAMADA_ID_PROC"]:
        if not LLAMADA_ID_PROC():
            return False
    elif token.type in predictions["FACTOR->token_real"]:
        if not match("token_real"):
            return False
    elif token.type in predictions["FACTOR->token_entero"]:
        if not match("token_entero"):
            return False
    elif token.type in predictions["FACTOR->token_cadena"]:
        if not match("token_cadena"):
            return False
    elif token.type in predictions["FACTOR->verdadero"]:
        if not match("verdadero"):
            return False
    elif token.type in predictions["FACTOR->falso"]:
        if not match("falso"):
            return False
    elif token.type in predictions["FACTOR->token_neg-EXPRESION"]:
        if not match("token_neg"):
            return False
        if not EXPRESION():
            return False
    elif token.type in predictions["FACTOR->token_menos-EXPRESION"]:
        if not match("token_menos"):
            return False
        if not EXPRESION():
            return False
    elif "FACTOR->epsilon" in predictions:
        return True
    else:
        print syntax_error("FACTOR", token, False)
        return False
    return True

def LLAMADA_ID_PROC():
    global token
    if token.type in predictions["LLAMADA_ID_PROC->id-LLAMADA_ID_PROC1"]:
        if not match("id"):
            return False
        if not LLAMADA_ID_PROC1():
            return False
    elif "LLAMADA_ID_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("LLAMADA_ID_PROC", token, False)
        return False
    return True

def LLAMADA_ID_PROC1():
    global token
    if token.type in predictions["LLAMADA_ID_PROC1->PAR_PROC"]:
        if not PAR_PROC():
            return False
    elif token.type in predictions["LLAMADA_ID_PROC1->LISTA_DIM"]:
        if not LISTA_DIM():
            return False
    elif "LLAMADA_ID_PROC1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LLAMADA_ID_PROC1", token, False)
        return False
    return True

def PAR_PROC():
    global token
    if token.type in predictions["PAR_PROC->token_par_izq-LISTA_PAR_PROC-token_par_der"]:
        if not match("token_par_izq"):
            return False
        if not LISTA_PAR_PROC():
            return False
        if not match("token_par_der"):
            return False
    elif "PAR_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("PAR_PROC", token, False)
        return False
    return True

def LISTA_DIM():
    global token
    if token.type in predictions["LISTA_DIM->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1"]:
        if not match("token_cor_izq"):
            return False
        if not EXPRESION():
            return False
        if not match("token_cor_der"):
            return False
        if not LISTA_DIM1():
            return False
    elif "LISTA_DIM->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_DIM", token, False)
        return False
    return True

def LISTA_DIM1():
    global token
    if token.type in predictions["LISTA_DIM1->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1"]:
        if not match("token_cor_izq"):
            return False
        if not EXPRESION():
            return False
        if not match("token_cor_der"):
            return False
        if not LISTA_DIM1():
            return False
    elif "LISTA_DIM1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_DIM1", token, False)
        return False
    return True

def LISTA_PAR_PROC():
    global token
    if token.type in predictions["LISTA_PAR_PROC->EXPRESION-LISTA_PAR_PROC1"]:
        if not EXPRESION():
            return False
        if not LISTA_PAR_PROC1():
            return False
    elif "LISTA_PAR_PROC->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_PAR_PROC", token, False)
        return False
    return True

def LISTA_PAR_PROC1():
    global token
    if token.type in predictions["LISTA_PAR_PROC1->token_coma-EXPRESION-LISTA_PAR_PROC1"]:
        if not match("token_coma"):
            return False
        if not EXPRESION():
            return False
        if not LISTA_PAR_PROC1():
            return False
    elif "LISTA_PAR_PROC1->epsilon" in predictions:
        return True
    else:
        print syntax_error("LISTA_PAR_PROC1", token, False)
        return False
    return True

def TIPO_DATO():
    global token
    if token.type in predictions["TIPO_DATO->numero"]:
        if not match("numero"):
            return False
    elif token.type in predictions["TIPO_DATO->numerico"]:
        if not match("numerico"):
            return False
    elif token.type in predictions["TIPO_DATO->entero"]:
        if not match("entero"):
            return False
    elif token.type in predictions["TIPO_DATO->real"]:
        if not match("real"):
            return False
    elif token.type in predictions["TIPO_DATO->caracter"]:
        if not match("caracter"):
            return False
    elif token.type in predictions["TIPO_DATO->texto"]:
        if not match("texto"):
            return False
    elif token.type in predictions["TIPO_DATO->cadena"]:
        if not match("cadena"):
            return False
    elif token.type in predictions["TIPO_DATO->logico"]:
        if not match("logico"):
            return False
    elif "TIPO_DATO->epsilon" in predictions:
        return True
    else:
        print syntax_error("TIPO_DATO", token, False)
        return False
    return True

def OPERADOR():
    global token
    if token.type in predictions["OPERADOR->token_mas"]:
        if not match("token_mas"):
            return False
    elif token.type in predictions["OPERADOR->token_menos"]:
        if not match("token_menos"):
            return False
    elif token.type in predictions["OPERADOR->token_div"]:
        if not match("token_div"):
            return False
    elif token.type in predictions["OPERADOR->token_mul"]:
        if not match("token_mul"):
            return False
    elif token.type in predictions["OPERADOR->token_mod"]:
        if not match("token_mod"):
            return False
    elif token.type in predictions["OPERADOR->token_pot"]:
        if not match("token_pot"):
            return False
    elif token.type in predictions["OPERADOR->token_igual"]:
        if not match("token_igual"):
            return False
    elif token.type in predictions["OPERADOR->token_dif"]:
        if not match("token_dif"):
            return False
    elif token.type in predictions["OPERADOR->token_menor"]:
        if not match("token_menor"):
            return False
    elif token.type in predictions["OPERADOR->token_mayor"]:
        if not match("token_mayor"):
            return False
    elif token.type in predictions["OPERADOR->token_menor_igual"]:
        if not match("token_menor_igual"):
            return False
    elif token.type in predictions["OPERADOR->token_mayor_igual"]:
        if not match("token_mayor_igual"):
            return False
    elif token.type in predictions["OPERADOR->token_y"]:
        if not match("token_y"):
            return False
    elif token.type in predictions["OPERADOR->token_o"]:
        if not match("token_o"):
            return False
    elif "OPERADOR->epsilon" in predictions:
        return True
    else:
        print syntax_error("OPERADOR", token, False)
        return False
    return True

def run_syntax_analyzer(input = None, output = None):
    global token
    if output != None:
        stdout = open(input,"r")

    generate_tokens(input)
    process_missing_error = True
    for t in tokens:
        if t.type == "proceso":
            process_missing_error = False
            break
    if process_missing_error:
        print "Error sintactico: falta proceso"
        return
    token = get_next_token()
    if PSEINT():
        print "El analisis sintactico ha finalizado exitosamente."
        if output != None:
            stdout.write("El analisis sintactico ha finalizado exitosamente." + "\n")

grammar = "" \
        "PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC:funcion,subproceso,proceso,algoritmo;" \
        "FUNCION_SUBPROC->PROC-FUNCION_SUBPROC:funcion,subproceso;" \
        "FUNCION_SUBPROC->epsilon:proceso,algoritmo,EOF;" \
        "PROCESO->INICIO_PROCESO-id-BLOQUE_PROCESO:proceso,algoritmo;" \
        "INICIO_PROCESO->proceso:proceso;" \
        "INICIO_PROCESO->algoritmo:algoritmo;" \
        "BLOQUE_PROCESO->BLOQUE-FIN_PROCESO:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finproceso,finalgoritmo;" \
        "FIN_PROCESO->finproceso:finproceso;" \
        "FIN_PROCESO->finalgoritmo:finalgoritmo;" \
        "PROC->INICIO_PROC-id-FIRMA-BLOQUE_PROC:funcion,subproceso;" \
        "INICIO_PROC->funcion:funcion;" \
        "INICIO_PROC->subproceso:subproceso;" \
        "BLOQUE_PROC->BLOQUE-FIN_PROC:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finfuncion,finsubproceso;" \
        "FIN_PROC->finfuncion:finfuncion;" \
        "FIN_PROC->finsubproceso:finsubproceso;" \
        "FIRMA->token_asig-id-ARG_PROC:token_asig;" \
        "FIRMA->ARG_PROC:token_par_izq;" \
        "ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der:token_par_izq;" \
        "ARG_PROC->epsilon:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finfuncion,finsubproceso;" \
        "LISTA_ARG_PROC->id-LISTA_ARG_PROC1:id;" \
        "LISTA_ARG_PROC->epsilon:token_par_der;" \
        "LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1:token_coma;" \
        "LISTA_ARG_PROC1->epsilon:token_par_der;" \
        "BLOQUE->DECLARACION-BLOQUE:definir;" \
        "BLOQUE->ASIGNACION-BLOQUE:id;" \
        "BLOQUE->DIMENSION-BLOQUE:dimension;" \
        "BLOQUE->SI-BLOQUE:si;" \
        "BLOQUE->PARA-BLOQUE:para;" \
        "BLOQUE->MIENTRAS-BLOQUE:mientras;" \
        "BLOQUE->REPETIR-BLOQUE:repetir;" \
        "BLOQUE->SEGUN-BLOQUE:segun;" \
        "BLOQUE->OTRO-BLOQUE:borrar,limpiar,escribir,leer,esperar;" \
        "BLOQUE->epsilon:caso,finsegun,de,hasta,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "DECLARACION->definir-LISTA_ID-como-TIPO_DATO-token_pyc:definir;" \
        "ASIGNACION->id-ASIGNACION1:id;" \
        "ASIGNACION1->token_cor_izq-LISTA_EXPR-token_cor_der-token_asig-EXPRESION-token_pyc:token_cor_izq;" \
        "ASIGNACION1->token_asig-EXPRESION-token_pyc:token_asig;" \
        "DIMENSION->dimension-id-token_cor_izq-LISTA_EXPR-token_cor_der-token_pyc:dimension;" \
        "SI->si-EXPRESION-entonces-BLOQUE_SI:si;" \
        "BLOQUE_SI->BLOQUE-SI1:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,sino,finsi;" \
        "SI1->sino-BLOQUE_SI1:sino;" \
        "SI1->finsi:finsi;" \
        "BLOQUE_SI1->BLOQUE-finsi:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finsi;" \
        "PARA->para-id-token_asig-EXPRESION-hasta-EXPRESION-con-paso-EXPRESION-hacer-BLOQUE_PARA:para;" \
        "BLOQUE_PARA->BLOQUE-finpara:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finpara;" \
        "MIENTRAS->mientras-EXPRESION-hacer-BLOQUE_MIENTRAS:mientras;" \
        "BLOQUE_MIENTRAS->BLOQUE-finmientras:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finmientras;" \
        "REPETIR->repetir-BLOQUE_REPETIR:repetir;" \
        "BLOQUE_REPETIR->BLOQUE-hasta-que-EXPRESION:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,hasta;" \
        "SEGUN->segun-EXPRESION-hacer-CASO_LISTA:segun;" \
        "SEGUN1->finsegun:finsegun;" \
        "SEGUN1->de-otro-modo-token_dosp-BLOQUE_SEGUN1:de;" \
        "BLOQUE_SEGUN1->BLOQUE-finsegun:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,finsegun;" \
        "CASO_LISTA->caso-EXPRESION-token_dosp-BLOQUE_CASO_LISTA:caso;" \
        "CASO_LISTA->SEGUN1:finsegun,de;" \
        "BLOQUE_CASO_LISTA->BLOQUE-CASO_LISTA:definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de;" \
        "OTRO->borrar-pantalla:borrar;" \
        "OTRO->ESCRIBIR:escribir;" \
        "OTRO->ESPERAR:esperar;" \
        "OTRO->LEER:leer;" \
        "OTRO->limpiar-pantalla:limpiar;" \
        "LISTA_EXPR->EXPRESION-LISTA_EXPR1:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "LISTA_EXPR->OPERADOR-TERMINO-LISTA_EXPR:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o;" \
        "LISTA_EXPR->epsilon:token_pyc,token_cor_der,token_coma,token_par_der,segundos,milisegundos,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id,token_dosp,hacer,hasta,con,entonces,token_mas,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "LISTA_EXPR1->token_coma-LISTA_EXPR1:token_coma;" \
        "LISTA_EXPR1->EXPRESION:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "LISTA_EXPR1->epsilon:token_pyc,token_cor_der,token_coma,token_par_der,segundos,milisegundos,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id,token_dosp,hacer,hasta,con,entonces,token_mas,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "LISTA_ID->id-LISTA_ID1:id;" \
        "LISTA_ID1->token_coma-id-LISTA_ID1:token_coma;" \
        "LISTA_ID1->epsilon:token_pyc,como;" \
        "ESCRIBIR->escribir-LISTA_EXPR-token_pyc:escribir;" \
        "ESPERAR->esperar-ESPERAR1:esperar;" \
        "ESPERAR1->tecla-token_pyc:tecla;" \
        "ESPERAR1->EXPRESION-MEDIDA_TIEMPO-token_pyc:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "MEDIDA_TIEMPO->segundos:segundos;" \
        "MEDIDA_TIEMPO->milisegundos:milisegundos;" \
        "LEER->leer-LISTA_ID-token_pyc:leer;" \
        "EXPRESION->TERMINO-LISTA_EXPR:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "TERMINO->FACTOR-LISTA_FACTOR:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "LISTA_FACTOR->OPERADOR-FACTOR-LISTA_FACTOR:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o;" \
        "LISTA_FACTOR->epsilon:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id,token_mas,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "FACTOR->token_par_izq-EXPRESION-token_par_der:token_par_izq;" \
        "FACTOR->LLAMADA_ID_PROC:id;" \
        "FACTOR->token_real:token_real;" \
        "FACTOR->token_entero:token_entero;" \
        "FACTOR->token_cadena:token_cadena;" \
        "FACTOR->verdadero:verdadero;" \
        "FACTOR->falso:falso;" \
        "FACTOR->token_neg-EXPRESION:token_neg;" \
        "FACTOR->token_menos-EXPRESION:token_menos;" \
        "LLAMADA_ID_PROC->id-LLAMADA_ID_PROC1:id;" \
        "LLAMADA_ID_PROC1->PAR_PROC:token_par_izq;" \
        "LLAMADA_ID_PROC1->LISTA_DIM:token_cor_izq;" \
        "LLAMADA_ID_PROC1->epsilon:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "PAR_PROC->token_par_izq-LISTA_PAR_PROC-token_par_der:token_par_izq;" \
        "LISTA_DIM->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1:token_cor_izq;" \
        "LISTA_DIM1->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1:token_cor_izq;" \
        "LISTA_DIM1->epsilon:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,de,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo;" \
        "LISTA_PAR_PROC->EXPRESION-LISTA_PAR_PROC1:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,token_menos,id;" \
        "LISTA_PAR_PROC->epsilon:token_par_der;" \
        "LISTA_PAR_PROC1->token_coma-EXPRESION-LISTA_PAR_PROC1:token_coma;" \
        "LISTA_PAR_PROC1->epsilon:token_par_der;" \
        "TIPO_DATO->numero:numero;" \
        "TIPO_DATO->numerico:numerico;" \
        "TIPO_DATO->entero:entero;" \
        "TIPO_DATO->real:real;" \
        "TIPO_DATO->caracter:caracter;" \
        "TIPO_DATO->texto:texto;" \
        "TIPO_DATO->cadena:cadena;" \
        "TIPO_DATO->logico:logico;" \
        "OPERADOR->token_mas:token_mas;" \
        "OPERADOR->token_menos:token_menos;" \
        "OPERADOR->token_div:token_div;" \
        "OPERADOR->token_mul:token_mul;" \
        "OPERADOR->token_mod:token_mod;" \
        "OPERADOR->token_pot:token_pot;" \
        "OPERADOR->token_igual:token_igual;" \
        "OPERADOR->token_dif:token_dif;" \
        "OPERADOR->token_menor:token_menor;" \
        "OPERADOR->token_mayor:token_mayor;" \
        "OPERADOR->token_menor_igual:token_menor_igual;" \
        "OPERADOR->token_mayor_igual:token_mayor_igual;" \
        "OPERADOR->token_y:token_y;" \
        "OPERADOR->token_o:token_o"
expected = {}
predictions = {}
generate_prediction_sets(grammar)

token = Token()
run_syntax_analyzer("ejemplos2/3.in")

#Replace FIN_PROCESO for BLOQUE_PROCESO
#Replace FIN_PROC for BLOQUE_PROC
