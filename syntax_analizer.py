#
# Lexer Taller 1
#
#
from itertools import chain
from sys import stdin
import re
import filecmp

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
        token = line[index:-1]
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

    # Operator
    if token is None and is_operator(character):
        token, advance = read_operator(line)
        if token is not None:
            type = operators[token]

    # Keyword or identifier
    if token is None and is_letter(character):
        type, token, advance = read_keyword_identifier(line)

    # String
    if token is None and is_string(character):
        token, advance = read_string(line)
        if token is not None:
            type = "token_cadena"

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
    def __init__(self, title, lexema, r, c):
        global keywords, operators

        if lexema in keywords:
            if lexema not in operators:
                self.lexema = lexema
                self.type = lexema
            else:
                self.lexema = operators[lexema]
                self.type = operators[lexema]
        elif lexema in operators:
            self.lexema = title
            self.type = title
        else:
            self.lexema = lexema.lower()
            self.type = title

        self.row = r
        self.col = c

current_token = 0
def get_next_token():
    global current_token, tokens
    c = current_token
    current_token += 1
    return tokens[c]


def read_data():
    global tokens, row, col

    lines = stdin.readlines()

    tokens = []

    type = ""

    for line in lines:
        while col < len(line) and type is not "lex_error":
            type, token, x, y = next_token(line)
            if type is not "token_otro" and type is not "lex_error" and type is not "token_comentario":
                #print build_token(type, token, x + 1, y + 1)

                #Prints in file
                tokens.append(Token(type, token, x + 1, y + 1))
                stdout.write(build_token(type, token, x + 1, y + 1) + "\n")

        if type is "lex_error":
            #print lex_error()

            # Prints in file
            stdout.write(str(lex_error()) + "\n")
            break

        row += 1
        col = 0

    for token in tokens:
        print token.type, token.lexema, token.row, token.col

    #return tokens


def join_file (file):
    str = ""
    with open(file) as f:
        str += "".join(line.strip() for line in f)
    return str





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
    error += "<" + str(token.row) + "," + str(token.col) + "> Error sintactico: se encontro \"" + token.lexema + "\"; se esperaba: "
    if error_syntax_in_match:
        error += "\"" + expec + "\"."
    else:
        for e in expected[expec]:
            error += "\"" + e + "\","
    return error

def match(expected_token):
    global token
    if token.type == expected_token:
        print token.type, "matched"
        token = get_next_token()
    else:
        print syntax_error(expected_token, token, True)

def PSEINT():
    global token
    if token.type in predictions["PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC"]:
        FUNCION_SUBPROC()
        PROCESO()
        FUNCION_SUBPROC()
    else:
        print syntax_error("PSEINT", token, False)

def FUNCION_SUBPROC():
    global token
    if token.type in predictions["FUNCION_SUBPROC->PROC-FUNCION_SUBPROC"]:
        PROC()
        FUNCION_SUBPROC()
    elif token.type in predictions["FUNCION_SUBPROC->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("FUNCION_SUBPROC", token, False)

def PROCESO():
    global token
    if token.type in predictions["PROCESO->INICIO_PROCESO-id-BLOQUE-FIN_PROCESO"]:
        INICIO_PROCESO()
        match("id")
        BLOQUE()
        FIN_PROCESO()
    else:
        print syntax_error("PROCESO", token, False)

def INICIO_PROCESO():
    global token
    if token.type in predictions["INICIO_PROCESO->proceso"]:
        match("proceso")
    elif token.type in predictions["INICIO_PROCESO->algoritmo"]:
        match("algoritmo")
    else:
        print syntax_error("INICIO_PROCESO", token, False)

def FIN_PROCESO():
    global token
    if token.type in predictions["FIN_PROCESO->finproceso"]:
        match("finproceso")
    elif token.type in predictions["FIN_PROCESO->finalgoritmo"]:
        match("finalgoritmo")
    else:
        print syntax_error("FIN_PROCESO", token, False)

def PROC():
    global token
    if token.type in predictions["PROC->INICIO_PROC-id-FIRMA-BLOQUE-FIN_PROC"]:
        INICIO_PROC()
        match("id")
        FIRMA()
        BLOQUE()
        FIN_PROC()
    else:
        print syntax_error("PROC", token, False)

def INICIO_PROC():
    global token
    if token.type in predictions["INICIO_PROC->funcion"]:
        match("funcion")
    elif token.type in predictions["INICIO_PROC->subproceso"]:
        match("subproceso")
    else:
        print syntax_error("INICIO_PROC", token, False)

def FIN_PROC():
    global token
    if token.type in predictions["FIN_PROC->finfuncion"]:
        match("finfuncion")
    elif token.type in predictions["FIN_PROC->finsubproceso"]:
        match("finsubproceso")
    else:
        print syntax_error("FIN_PROC", token, False)

def FIRMA():
    global token
    if token.type in predictions["FIRMA->token_asig-id-ARG_PROC"]:
        match("token_asig")
        match("id")
        ARG_PROC()
    elif token.type in predictions["FIRMA->ARG_PROC"]:
        ARG_PROC()
    else:
        print syntax_error("FIRMA", token, False)

def ARG_PROC():
    global token
    if token.type in predictions["ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der"]:
        match("token_par_izq")
        LISTA_ARG_PROC()
        match("token_par_der")
    elif token.type in predictions["ARG_PROC->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("ARG_PROC", token, False)

def LISTA_ARG_PROC():
    global token
    if token.type in predictions["LISTA_ARG_PROC->id-LISTA_ARG_PROC1"]:
        match("id")
        LISTA_ARG_PROC1()
    elif token.type in predictions["LISTA_ARG_PROC->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_ARG_PROC", token, False)

def LISTA_ARG_PROC1():
    global token
    if token.type in predictions["LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1"]:
        match("token_coma")
        match("id")
        LISTA_ARG_PROC1()
    elif token.type in predictions["LISTA_ARG_PROC1->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_ARG_PROC1", token, False)

def BLOQUE():
    global token
    if token.type in predictions["BLOQUE->DECLARACION-BLOQUE"]:
        DECLARACION()
        BLOQUE()
    elif token.type in predictions["BLOQUE->ASIGNACION-BLOQUE"]:
        ASIGNACION()
        BLOQUE()
    elif token.type in predictions["BLOQUE->DIMENSION-BLOQUE"]:
        DIMENSION()
        BLOQUE()
    elif token.type in predictions["BLOQUE->SI_BLOQUE-BLOQUE"]:
        SI_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->PARA_BLOQUE-BLOQUE"]:
        PARA_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->MIENTRAS_BLOQUE-BLOQUE"]:
        MIENTRAS_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->REPETIR_BLOQUE-BLOQUE"]:
        REPETIR_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->SEGUN_BLOQUE-BLOQUE"]:
        SEGUN_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->OTRO_BLOQUE-BLOQUE"]:
        OTRO_BLOQUE()
        BLOQUE()
    elif token.type in predictions["BLOQUE->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("BLOQUE", token, False)

def DECLARACION():
    global token
    if token.type in predictions["DECLARACION->definir-LISTA_ID-como-TIPO_DATO-token_pyc"]:
        match("definir")
        LISTA_ID()
        match("como")
        TIPO_DATO()
        match("token_pyc")
    else:
        print syntax_error("DECLARACION", token, False)

def ASIGNACION():
    global token
    if token.type in predictions["ASIGNACION->id-ASIGNACION1"]:
        match("id")
        ASIGNACION1()
    else:
        print syntax_error("ASIGNACION", token, False)

def ASIGNACION1():
    global token
    if token.type in predictions["ASIGNACION1->token_cor_izq-LISTA_EXPR-token_cor_der-token_asig-EXPRESION-token_pyc"]:
        match("token_cor_izq")
        LISTA_EXPR()
        match("token_cor_der")
        match("token_asig")
        EXPRESION()
        match("token_pyc")
    elif token.type in predictions["ASIGNACION1->token_asig-EXPRESION-token_pyc"]:
        match("token_asig")
        EXPRESION()
        match("token_pyc")
    else:
        print syntax_error("ASIGNACION1", token, False)

def DIMENSION():
    global token
    if token.type in predictions["DIMENSION->dimension-id-token_cor_izq-LISTA_EXPR-token_cor_der-token_pyc"]:
        match("dimension")
        match("id")
        match("token_cor_izq")
        LISTA_EXPR()
        match("token_cor_der")
        match("token_pyc")
    else:
        print syntax_error("DIMENSION", token, False)

def SI_BLOQUE():
    global token
    if token.type in predictions["SI_BLOQUE->si-EXPR_BOOL-entonces-BLOQUE-SI_BLOQUE1"]:
        match("si")
        EXPR_BOOL()
        match("entonces")
        BLOQUE()
        SI_BLOQUE1()
    else:
        print syntax_error("SI_BLOQUE", token, False)

def SI_BLOQUE1():
    global token
    if token.type in predictions["SI_BLOQUE1->sino-BLOQUE-finsi"]:
        match("sino")
        BLOQUE()
        match("finsi")
    elif token.type in predictions["SI_BLOQUE1->finsi"]:
        match("finsi")
    else:
        print syntax_error("SI_BLOQUE1", token, False)

def PARA_BLOQUE():
    global token
    if token.type in predictions["PARA_BLOQUE->para-id-token_asig-EXPR_NUM-hasta-EXPR_NUM-con-paso-EXPR_NUM-hacer-BLOQUE-finpara"]:
        match("para")
        match("id")
        match("token_asig")
        EXPR_NUM()
        match("hasta")
        EXPR_NUM()
        match("con")
        match("paso")
        EXPR_NUM()
        match("hacer")
        BLOQUE()
        match("finpara")
    else:
        print syntax_error("PARA_BLOQUE", token, False)

def MIENTRAS_BLOQUE():
    global token
    if token.type in predictions["MIENTRAS_BLOQUE->mientras-EXPR_BOOL-hacer-BLOQUE-finmientras"]:
        match("mientras")
        EXPR_BOOL()
        match("hacer")
        BLOQUE()
        match("finmientras")
    else:
        print syntax_error("MIENTRAS_BLOQUE", token, False)

def REPETIR_BLOQUE():
    global token
    if token.type in predictions["REPETIR_BLOQUE->repetir-BLOQUE-hasta-que-EXPR_BOOL"]:
        match("repetir")
        BLOQUE()
        match("hasta")
        match("que")
        EXPR_BOOL()
    else:
        print syntax_error("REPETIR_BLOQUE", token, False)

def SEGUN_BLOQUE():
    global token
    if token.type in predictions["SEGUN_BLOQUE->segun-EXPR_NUM-hacer-CASO_LISTA-SEGUN_BLOQUE1"]:
        match("segun")
        EXPR_NUM()
        match("hacer")
        CASO_LISTA()
        SEGUN_BLOQUE1()
    else:
        print syntax_error("SEGUN_BLOQUE", token, False)

def SEGUN_BLOQUE1():
    global token
    if token.type in predictions["SEGUN_BLOQUE1->finsegun"]:
        match("finsegun")
    elif token.type in predictions["SEGUN_BLOQUE1->de-otro-modo-token_dosp-BLOQUE-finsegun"]:
        match("de")
        match("otro")
        match("modo")
        match("token_dosp")
        BLOQUE()
        match("finsegun")
    else:
        print syntax_error("SEGUN_BLOQUE1", token, False)

def CASO_LISTA():
    global token
    if token.type in predictions["CASO_LISTA->caso-EXPR_NUM-token_dosp-BLOQUE-CASO_LISTA"]:
        match("caso")
        EXPR_NUM()
        match("token_dosp")
        BLOQUE()
        CASO_LISTA()
    elif token.type in predictions["CASO_LISTA->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("CASO_LISTA", token, False)

def OTRO_BLOQUE():
    global token
    if token.type in predictions["OTRO_BLOQUE->borrar-pantalla"]:
        match("borrar")
        match("pantalla")
    elif token.type in predictions["OTRO_BLOQUE->ESCRIBIR"]:
        ESCRIBIR()
    elif token.type in predictions["OTRO_BLOQUE->ESPERAR_BLOQUE"]:
        ESPERAR_BLOQUE()
    elif token.type in predictions["OTRO_BLOQUE->LEER"]:
        LEER()
    elif token.type in predictions["OTRO_BLOQUE->limpiar-pantalla"]:
        match("limpiar")
        match("pantalla")
    else:
        print syntax_error("OTRO_BLOQUE", token, False)

def LISTA_EXPR():
    global token
    if token.type in predictions["LISTA_EXPR->EXPRESION-LISTA_EXPR1"]:
        EXPRESION()
        LISTA_EXPR1()
    else:
        print syntax_error("LISTA_EXPR", token, False)

def LISTA_EXPR1():
    global token
    if token.type in predictions["LISTA_EXPR1->token_coma-LISTA_EXPR1"]:
        match("token_coma")
        LISTA_EXPR1()
    elif token.type in predictions["LISTA_EXPR1->EXPRESION"]:
        EXPRESION()
    else:
        print syntax_error("LISTA_EXPR1", token, False)

def LISTA_ID():
    global token
    if token.type in predictions["LISTA_ID->id-LISTA_ID1"]:
        match("id")
        LISTA_ID1()
    else:
        print syntax_error("LISTA_ID", token, False)

def LISTA_ID1():
    global token
    if token.type in predictions["LISTA_ID1->token_coma-LISTA_ID1"]:
        match("token_coma")
        LISTA_ID1()
    elif token.type in predictions["LISTA_ID1->id"]:
        match("id")
    else:
        print syntax_error("LISTA_ID1", token, False)

def ESCRIBIR():
    global token
    if token.type in predictions["ESCRIBIR->escribir-LISTA_EXPR-token_pyc"]:
        match("escribir")
        LISTA_EXPR()
        match("token_pyc")
    else:
        print syntax_error("ESCRIBIR", token, False)

def ESPERAR_BLOQUE():
    global token
    if token.type in predictions["ESPERAR_BLOQUE->esperar-ESPERAR_BLOQUE1"]:
        match("esperar")
        ESPERAR_BLOQUE1()
    else:
        print syntax_error("ESPERAR_BLOQUE", token, False)

def ESPERAR_BLOQUE1():
    global token
    if token.type in predictions["ESPERAR_BLOQUE1->tecla-token_pyc"]:
        match("tecla")
        match("token_pyc")
    elif token.type in predictions["ESPERAR_BLOQUE1->EXPR_NUM-MEDIDA_TIEMPO-token_pyc"]:
        EXPR_NUM()
        MEDIDA_TIEMPO()
        match("token_pyc")
    else:
        print syntax_error("ESPERAR_BLOQUE1", token, False)

def MEDIDA_TIEMPO():
    global token
    if token.type in predictions["MEDIDA_TIEMPO->segundos"]:
        match("segundos")
    elif token.type in predictions["MEDIDA_TIEMPO->milisegundos"]:
        match("milisegundos")
    else:
        print syntax_error("MEDIDA_TIEMPO", token, False)

def LEER():
    global token
    if token.type in predictions["LEER->leer-LISTA_ID-token_pyc"]:
        match("leer")
        LISTA_ID()
        match("token_pyc")
    else:
        print syntax_error("LEER", token, False)

def EXPRESION():
    global token
    if token.type in predictions["EXPRESION->EXPR_NUM"]:
        EXPR_NUM()
    elif token.type in predictions["EXPRESION->EXPR_CAD"]:
        EXPR_CAD()
    elif token.type in predictions["EXPRESION->EXPR_BOOL"]:
        EXPR_BOOL()
    else:
        print syntax_error("EXPRESION", token, False)

def EXPR_NUM():
    global token
    if token.type in predictions["EXPR_NUM->TERMINO_NUM-LISTA_EXPR_NUM"]:
        TERMINO_NUM()
        LISTA_EXPR_NUM()
    else:
        print syntax_error("EXPR_NUM", token, False)

def LISTA_EXPR_NUM():
    global token
    if token.type in predictions["LISTA_EXPR_NUM->OPARITMETICO-TERMINO_NUM-LISTA_EXPR_NUM"]:
        OPARITMETICO()
        TERMINO_NUM()
        LISTA_EXPR_NUM()
    elif token.type in predictions["LISTA_EXPR_NUM->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_EXPR_NUM", token, False)

def TERMINO_NUM():
    global token
    if token.type in predictions["TERMINO_NUM->FACTOR_NUM-LISTA_FACTOR_NUM"]:
        FACTOR_NUM()
        LISTA_FACTOR_NUM()
    else:
        print syntax_error("TERMINO_NUM", token, False)

def LISTA_FACTOR_NUM():
    global token
    if token.type in predictions["LISTA_FACTOR_NUM->OPARITMETICO-FACTOR_NUM-LISTA_FACTOR_NUM"]:
        OPARITMETICO()
        FACTOR_NUM()
        LISTA_FACTOR_NUM()
    elif token.type in predictions["LISTA_FACTOR_NUM->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_FACTOR_NUM", token, False)

def FACTOR_NUM():
    global token
    if token.type in predictions["FACTOR_NUM->token_par_izq-EXPR_NUM-token_par_der"]:
        match("token_par_izq")
        EXPR_NUM()
        match("token_par_der")
    elif token.type in predictions["FACTOR_NUM->LLAMADA_PROC"]:
        LLAMADA_PROC()
    elif token.type in predictions["FACTOR_NUM->token_real"]:
        match("token_real")
    elif token.type in predictions["FACTOR_NUM->token_entero"]:
        match("token_entero")
    else:
        print syntax_error("FACTOR_NUM", token, False)

def EXPR_CAD():
    global token
    if token.type in predictions["EXPR_CAD->TERMINO_CAD-LISTA_EXPR_CAD"]:
        TERMINO_CAD()
        LISTA_EXPR_CAD()
    else:
        print syntax_error("EXPR_CAD", token, False)

def LISTA_EXPR_CAD():
    global token
    if token.type in predictions["LISTA_EXPR_CAD->OPCADENA-TERMINO_CAD-LISTA_EXPR_CAD"]:
        OPCADENA()
        TERMINO_CAD()
        LISTA_EXPR_CAD()
    elif token.type in predictions["LISTA_EXPR_CAD->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_EXPR_CAD", token, False)

def TERMINO_CAD():
    global token
    if token.type in predictions["TERMINO_CAD->token_par_izq-EXPR_CAD-token_par_der"]:
        match("token_par_izq")
        EXPR_CAD()
        match("token_par_der")
    elif token.type in predictions["TERMINO_CAD->LLAMADA_PROC"]:
        LLAMADA_PROC()
    elif token.type in predictions["TERMINO_CAD->token_cadena"]:
        match("token_cadena")
    else:
        print syntax_error("TERMINO_CAD", token, False)

def EXPR_BOOL():
    global token
    if token.type in predictions["EXPR_BOOL->TERMINO_BOOL-LISTA_EXPR_BOOL"]:
        TERMINO_BOOL()
        LISTA_EXPR_BOOL()
    else:
        print syntax_error("EXPR_BOOL", token, False)

def LISTA_EXPR_BOOL():
    global token
    if token.type in predictions["LISTA_EXPR_BOOL->OPBOOL-TERMINO_BOOL-LISTA_EXPR_BOOL"]:
        OPBOOL()
        TERMINO_BOOL()
        LISTA_EXPR_BOOL()
    elif token.type in predictions["LISTA_EXPR_BOOL->epsilon"]:
        match("epsilon")
    else:
        print syntax_error("LISTA_EXPR_BOOL", token, False)

def TERMINO_BOOL():
    global token
    if token.type in predictions["TERMINO_BOOL->token_par_izq-EXPR_BOOL-token_par_der"]:
        match("token_par_izq")
        EXPR_BOOL()
        match("token_par_der")
    elif token.type in predictions["TERMINO_BOOL->LLAMADA_PROC"]:
        LLAMADA_PROC()
    elif token.type in predictions["TERMINO_BOOL->verdadero"]:
        match("verdadero")
    elif token.type in predictions["TERMINO_BOOL->falso"]:
        match("falso")
    elif token.type in predictions["TERMINO_BOOL->token_neg-EXPR_BOOL"]:
        match("token_neg")
        EXPR_BOOL()
    else:
        print syntax_error("TERMINO_BOOL", token, False)

def LLAMADA_PROC():
    global token
    if token.type in predictions["LLAMADA_PROC->id-ARG_PROC"]:
        match("id")
        ARG_PROC()
    else:
        print syntax_error("LLAMADA_PROC", token, False)

def TIPO_DATO():
    global token
    if token.type in predictions["TIPO_DATO->numero"]:
        match("numero")
    elif token.type in predictions["TIPO_DATO->numerico"]:
        match("numerico")
    elif token.type in predictions["TIPO_DATO->entero"]:
        match("entero")
    elif token.type in predictions["TIPO_DATO->real"]:
        match("real")
    elif token.type in predictions["TIPO_DATO->caracter"]:
        match("caracter")
    elif token.type in predictions["TIPO_DATO->texto"]:
        match("texto")
    elif token.type in predictions["TIPO_DATO->cadena"]:
        match("cadena")
    elif token.type in predictions["TIPO_DATO->logico"]:
        match("logico")
    else:
        print syntax_error("TIPO_DATO", token, False)

def OPARITMETICO():
    global token
    if token.type in predictions["OPARITMETICO->token_mas"]:
        match("token_mas")
    elif token.type in predictions["OPARITMETICO->token_menos"]:
        match("token_menos")
    elif token.type in predictions["OPARITMETICO->token_div"]:
        match("token_div")
    elif token.type in predictions["OPARITMETICO->token_mul"]:
        match("token_mul")
    elif token.type in predictions["OPARITMETICO->token_mod"]:
        match("token_mod")
    elif token.type in predictions["OPARITMETICO->token_pot"]:
        match("token_pot")
    else:
        print syntax_error("OPARITMETICO", token, False)

def OPCADENA():
    global token
    if token.type in predictions["OPCADENA->token_mas"]:
        match("token_mas")
    else:
        print syntax_error("OPCADENA", token, False)

def OPBIN():
    global token
    if token.type in predictions["OPBIN->token_igual"]:
        match("token_igual")
    elif token.type in predictions["OPBIN->token_dif"]:
        match("token_dif")
    elif token.type in predictions["OPBIN->token_menor"]:
        match("token_menor")
    elif token.type in predictions["OPBIN->token_mayor"]:
        match("token_mayor")
    elif token.type in predictions["OPBIN->token_menor_igual"]:
        match("token_menor_igual")
    elif token.type in predictions["OPBIN->token_mayor_igual"]:
        match("token_mayor_igual")
    else:
        print syntax_error("OPBIN", token, False)

def OPBOOL():
    global token
    if token.type in predictions["OPBOOL->token_y"]:
        match("token_y")
    elif token.type in predictions["OPBOOL->token_o"]:
        match("token_o")
    else:
        print syntax_error("OPBOOL", token, False)

grammar = "" \
        "PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC:epsilon,funcion,subproceso;" \
        "FUNCION_SUBPROC->PROC-FUNCION_SUBPROC:funcion,subproceso;" \
        "FUNCION_SUBPROC->epsilon:epsilon;" \
        "PROCESO->INICIO_PROCESO-id-BLOQUE-FIN_PROCESO:proceso,algoritmo;" \
        "INICIO_PROCESO->proceso:proceso;" \
        "INICIO_PROCESO->algoritmo:algoritmo;" \
        "FIN_PROCESO->finproceso:finproceso;" \
        "FIN_PROCESO->finalgoritmo:finalgoritmo;" \
        "PROC->INICIO_PROC-id-FIRMA-BLOQUE-FIN_PROC:funcion,subproceso;" \
        "INICIO_PROC->funcion:funcion;" \
        "INICIO_PROC->subproceso:subproceso;" \
        "FIN_PROC->finfuncion:finfuncion;" \
        "FIN_PROC->finsubproceso:finsubproceso;" \
        "FIRMA->token_asig-id-ARG_PROC:token_asig;" \
        "FIRMA->ARG_PROC:token_par_izq,epsilon;" \
        "ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der:token_par_izq;" \
        "ARG_PROC->epsilon:epsilon;" \
        "LISTA_ARG_PROC->id-LISTA_ARG_PROC1:id;" \
        "LISTA_ARG_PROC->epsilon:epsilon;" \
        "LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1:token_coma;" \
        "LISTA_ARG_PROC1->epsilon:epsilon;" \
        "BLOQUE->DECLARACION-BLOQUE:definir;" \
        "BLOQUE->ASIGNACION-BLOQUE:id;" \
        "BLOQUE->DIMENSION-BLOQUE:dimension;" \
        "BLOQUE->SI_BLOQUE-BLOQUE:si;" \
        "BLOQUE->PARA_BLOQUE-BLOQUE:para;" \
        "BLOQUE->MIENTRAS_BLOQUE-BLOQUE:mientras;" \
        "BLOQUE->REPETIR_BLOQUE-BLOQUE:repetir;" \
        "BLOQUE->SEGUN_BLOQUE-BLOQUE:segun;" \
        "BLOQUE->OTRO_BLOQUE-BLOQUE:borrar,limpiar,escribir,leer,esperar;" \
        "BLOQUE->epsilon:epsilon;" \
        "DECLARACION->definir-LISTA_ID-como-TIPO_DATO-token_pyc:definir;" \
        "ASIGNACION->id-ASIGNACION1:id;" \
        "ASIGNACION1->token_cor_izq-LISTA_EXPR-token_cor_der-token_asig-EXPRESION-token_pyc:token_cor_izq;" \
        "ASIGNACION1->token_asig-EXPRESION-token_pyc:token_asig;" \
        "DIMENSION->dimension-id-token_cor_izq-LISTA_EXPR-token_cor_der-token_pyc:dimension;" \
        "SI_BLOQUE->si-EXPR_BOOL-entonces-BLOQUE-SI_BLOQUE1:si;" \
        "SI_BLOQUE1->sino-BLOQUE-finsi:sino;" \
        "SI_BLOQUE1->finsi:finsi;" \
        "PARA_BLOQUE->para-id-token_asig-EXPR_NUM-hasta-EXPR_NUM-con-paso-EXPR_NUM-hacer-BLOQUE-finpara:para;" \
        "MIENTRAS_BLOQUE->mientras-EXPR_BOOL-hacer-BLOQUE-finmientras:mientras;" \
        "REPETIR_BLOQUE->repetir-BLOQUE-hasta-que-EXPR_BOOL:repetir;" \
        "SEGUN_BLOQUE->segun-EXPR_NUM-hacer-CASO_LISTA-SEGUN_BLOQUE1:segun;" \
        "SEGUN_BLOQUE1->finsegun:finsegun;" \
        "SEGUN_BLOQUE1->de-otro-modo-token_dosp-BLOQUE-finsegun:de;" \
        "CASO_LISTA->caso-EXPR_NUM-token_dosp-BLOQUE-CASO_LISTA:caso;" \
        "CASO_LISTA->epsilon:epsilon;" \
        "OTRO_BLOQUE->borrar-pantalla:borrar;" \
        "OTRO_BLOQUE->ESCRIBIR:escribir;" \
        "OTRO_BLOQUE->ESPERAR_BLOQUE:esperar;" \
        "OTRO_BLOQUE->LEER:leer;" \
        "OTRO_BLOQUE->limpiar-pantalla:limpiar;" \
        "LISTA_EXPR->EXPRESION-LISTA_EXPR1:token_par_izq,token_real,token_entero,id,verdadero,falso,token_neg,token_cadena;" \
        "LISTA_EXPR1->token_coma-LISTA_EXPR1:token_coma;" \
        "LISTA_EXPR1->EXPRESION:token_par_izq,token_real,token_entero,id,verdadero,falso,token_neg,token_cadena;" \
        "LISTA_ID->id-LISTA_ID1:id;" \
        "LISTA_ID1->token_coma-LISTA_ID1:token_coma;" \
        "LISTA_ID1->id:id;" \
        "ESCRIBIR->escribir-LISTA_EXPR-token_pyc:escribir;" \
        "ESPERAR_BLOQUE->esperar-ESPERAR_BLOQUE1:esperar;" \
        "ESPERAR_BLOQUE1->tecla-token_pyc:tecla;" \
        "ESPERAR_BLOQUE1->EXPR_NUM-MEDIDA_TIEMPO-token_pyc:token_par_izq,token_real,token_entero,id;" \
        "MEDIDA_TIEMPO->segundos:segundos;" \
        "MEDIDA_TIEMPO->milisegundos:milisegundos;" \
        "LEER->leer-LISTA_ID-token_pyc:leer;" \
        "EXPRESION->EXPR_NUM:token_par_izq,token_real,token_entero,id;" \
        "EXPRESION->EXPR_CAD:token_par_izq,token_cadena,id;" \
        "EXPRESION->EXPR_BOOL:token_par_izq,verdadero,falso,token_neg,id;" \
        "EXPR_NUM->TERMINO_NUM-LISTA_EXPR_NUM:token_par_izq,token_real,token_entero,id;" \
        "LISTA_EXPR_NUM->OPARITMETICO-TERMINO_NUM-LISTA_EXPR_NUM:token_mas,token_menos,token_div,token_mul,token_mod,token_pot;" \
        "LISTA_EXPR_NUM->epsilon:epsilon;" \
        "TERMINO_NUM->FACTOR_NUM-LISTA_FACTOR_NUM:token_par_izq,token_real,token_entero,id;" \
        "LISTA_FACTOR_NUM->OPARITMETICO-FACTOR_NUM-LISTA_FACTOR_NUM:token_mas,token_menos,token_div,token_mul,token_mod,token_pot;" \
        "LISTA_FACTOR_NUM->epsilon:epsilon;" \
        "FACTOR_NUM->token_par_izq-EXPR_NUM-token_par_der:token_par_izq;" \
        "FACTOR_NUM->LLAMADA_PROC:id;" \
        "FACTOR_NUM->token_real:token_real;" \
        "FACTOR_NUM->token_entero:token_entero;" \
        "EXPR_CAD->TERMINO_CAD-LISTA_EXPR_CAD:token_par_izq,token_cadena,id;" \
        "LISTA_EXPR_CAD->OPCADENA-TERMINO_CAD-LISTA_EXPR_CAD:token_mas;" \
        "LISTA_EXPR_CAD->epsilon:epsilon;" \
        "TERMINO_CAD->token_par_izq-EXPR_CAD-token_par_der:token_par_izq;" \
        "TERMINO_CAD->LLAMADA_PROC:id;" \
        "TERMINO_CAD->token_cadena:token_cadena;" \
        "EXPR_BOOL->TERMINO_BOOL-LISTA_EXPR_BOOL:token_par_izq,verdadero,falso,token_neg,id;" \
        "LISTA_EXPR_BOOL->OPBOOL-TERMINO_BOOL-LISTA_EXPR_BOOL:token_y,token_o;" \
        "LISTA_EXPR_BOOL->epsilon:epsilon;" \
        "TERMINO_BOOL->token_par_izq-EXPR_BOOL-token_par_der:token_par_izq;" \
        "TERMINO_BOOL->LLAMADA_PROC:id;" \
        "TERMINO_BOOL->verdadero:verdadero;" \
        "TERMINO_BOOL->falso:falso;" \
        "TERMINO_BOOL->token_neg-EXPR_BOOL:token_neg;" \
        "LLAMADA_PROC->id-ARG_PROC:id;" \
        "TIPO_DATO->numero:numero;" \
        "TIPO_DATO->numerico:numerico;" \
        "TIPO_DATO->entero:entero;" \
        "TIPO_DATO->real:real;" \
        "TIPO_DATO->caracter:caracter;" \
        "TIPO_DATO->texto:texto;" \
        "TIPO_DATO->cadena:cadena;" \
        "TIPO_DATO->logico:logico;" \
        "OPARITMETICO->token_mas:token_mas;" \
        "OPARITMETICO->token_menos:token_menos;" \
        "OPARITMETICO->token_div:token_div;" \
        "OPARITMETICO->token_mul:token_mul;" \
        "OPARITMETICO->token_mod:token_mod;" \
        "OPARITMETICO->token_pot:token_pot;" \
        "OPCADENA->token_mas:token_mas;" \
        "OPBIN->token_igual:token_igual;" \
        "OPBIN->token_dif:token_dif;" \
        "OPBIN->token_menor:token_menor;" \
        "OPBIN->token_mayor:token_mayor;" \
        "OPBIN->token_menor_igual:token_menor_igual;" \
        "OPBIN->token_mayor_igual:token_mayor_igual;" \
        "OPBOOL->token_y:token_y;" \
        "OPBOOL->token_o:token_o"
expected = {}
predictions = {}
generate_prediction_sets(grammar)

tokens = []
keywords = {}
operators = {}

initialize_keywords()
initialize_operators()
row = 0
col = 0

examples = 2
for i in range(2,examples + 1):
    stdin = open("ejemplos/" + str(i) + ".in", "r")
    output_file = str(i) + ".out"
    stdout = open("output/" + output_file, "w")

    row = 0
    col = 0
    read_data()

    token = get_next_token()
    PSEINT()

    stdout.close()

    assert join_file("ejemplos/" + output_file) == join_file("output/" + output_file), "Error in file " + output_file






