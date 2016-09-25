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
            self.type = title
            self.lexema = lexema
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

    tokens.append(Token("token_eof", "token_eof", row + 1, col + 1))

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
        token = get_next_token()
    else:
        print syntax_error(expected_token, token, True)

def PSEINT():
    global token
    if token.type in predictions["PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC"]:
        FUNCION_SUBPROC()
        PROCESO()
        FUNCION_SUBPROC()
    elif "PSEINT->epsilon" in predictions:
        return
    else:
        print syntax_error("PSEINT", token, False)

def FUNCION_SUBPROC():
    global token
    if token.type in predictions["FUNCION_SUBPROC->PROC-FUNCION_SUBPROC"]:
        PROC()
        FUNCION_SUBPROC()
    elif "FUNCION_SUBPROC->epsilon" in predictions:
        return
    else:
        print syntax_error("FUNCION_SUBPROC", token, False)

def PROCESO():
    global token
    if token.type in predictions["PROCESO->INICIO_PROCESO-id-BLOQUE-FIN_PROCESO"]:
        INICIO_PROCESO()
        match("id")
        BLOQUE()
        FIN_PROCESO()
    elif "PROCESO->epsilon" in predictions:
        return
    else:
        print syntax_error("PROCESO", token, False)

def INICIO_PROCESO():
    global token
    if token.type in predictions["INICIO_PROCESO->proceso"]:
        match("proceso")
    elif token.type in predictions["INICIO_PROCESO->algoritmo"]:
        match("algoritmo")
    elif "INICIO_PROCESO->epsilon" in predictions:
        return
    else:
        print syntax_error("INICIO_PROCESO", token, False)

def FIN_PROCESO():
    global token
    if token.type in predictions["FIN_PROCESO->finproceso"]:
        match("finproceso")
    elif token.type in predictions["FIN_PROCESO->finalgoritmo"]:
        match("finalgoritmo")
    elif "FIN_PROCESO->epsilon" in predictions:
        return
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
    elif "PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("PROC", token, False)

def INICIO_PROC():
    global token
    if token.type in predictions["INICIO_PROC->funcion"]:
        match("funcion")
    elif token.type in predictions["INICIO_PROC->subproceso"]:
        match("subproceso")
    elif "INICIO_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("INICIO_PROC", token, False)

def FIN_PROC():
    global token
    if token.type in predictions["FIN_PROC->finfuncion"]:
        match("finfuncion")
    elif token.type in predictions["FIN_PROC->finsubproceso"]:
        match("finsubproceso")
    elif "FIN_PROC->epsilon" in predictions:
        return
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
    elif "FIRMA->epsilon" in predictions:
        return
    else:
        print syntax_error("FIRMA", token, False)

def ARG_PROC():
    global token
    if token.type in predictions["ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der"]:
        match("token_par_izq")
        LISTA_ARG_PROC()
        match("token_par_der")
    elif "ARG_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("ARG_PROC", token, False)

def LISTA_ARG_PROC():
    global token
    if token.type in predictions["LISTA_ARG_PROC->id-LISTA_ARG_PROC1"]:
        match("id")
        LISTA_ARG_PROC1()
    elif "LISTA_ARG_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_ARG_PROC", token, False)

def LISTA_ARG_PROC1():
    global token
    if token.type in predictions["LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1"]:
        match("token_coma")
        match("id")
        LISTA_ARG_PROC1()
    elif "LISTA_ARG_PROC1->epsilon" in predictions:
        return
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
    elif "BLOQUE->epsilon" in predictions:
        return
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
    elif "DECLARACION->epsilon" in predictions:
        return
    else:
        print syntax_error("DECLARACION", token, False)

def ASIGNACION():
    global token
    if token.type in predictions["ASIGNACION->id-ASIGNACION1"]:
        match("id")
        ASIGNACION1()
    elif "ASIGNACION->epsilon" in predictions:
        return
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
    elif "ASIGNACION1->epsilon" in predictions:
        return
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
    elif "DIMENSION->epsilon" in predictions:
        return
    else:
        print syntax_error("DIMENSION", token, False)

def SI_BLOQUE():
    global token
    if token.type in predictions["SI_BLOQUE->si-EXPRESION-entonces-BLOQUE-SI_BLOQUE1"]:
        match("si")
        EXPRESION()
        match("entonces")
        BLOQUE()
        SI_BLOQUE1()
    elif "SI_BLOQUE->epsilon" in predictions:
        return
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
    elif "SI_BLOQUE1->epsilon" in predictions:
        return
    else:
        print syntax_error("SI_BLOQUE1", token, False)

def PARA_BLOQUE():
    global token
    if token.type in predictions["PARA_BLOQUE->para-id-token_asig-EXPRESION-hasta-EXPRESION-con-paso-EXPRESION-hacer-BLOQUE-finpara"]:
        match("para")
        match("id")
        match("token_asig")
        EXPRESION()
        match("hasta")
        EXPRESION()
        match("con")
        match("paso")
        EXPRESION()
        match("hacer")
        BLOQUE()
        match("finpara")
    elif "PARA_BLOQUE->epsilon" in predictions:
        return
    else:
        print syntax_error("PARA_BLOQUE", token, False)

def MIENTRAS_BLOQUE():
    global token
    if token.type in predictions["MIENTRAS_BLOQUE->mientras-EXPRESION-hacer-BLOQUE-finmientras"]:
        match("mientras")
        EXPRESION()
        match("hacer")
        BLOQUE()
        match("finmientras")
    elif "MIENTRAS_BLOQUE->epsilon" in predictions:
        return
    else:
        print syntax_error("MIENTRAS_BLOQUE", token, False)

def REPETIR_BLOQUE():
    global token
    if token.type in predictions["REPETIR_BLOQUE->repetir-BLOQUE-hasta-que-EXPRESION"]:
        match("repetir")
        BLOQUE()
        match("hasta")
        match("que")
        EXPRESION()
    elif "REPETIR_BLOQUE->epsilon" in predictions:
        return
    else:
        print syntax_error("REPETIR_BLOQUE", token, False)

def SEGUN_BLOQUE():
    global token
    if token.type in predictions["SEGUN_BLOQUE->segun-EXPRESION-hacer-CASO_LISTA-SEGUN_BLOQUE1"]:
        match("segun")
        EXPRESION()
        match("hacer")
        CASO_LISTA()
        SEGUN_BLOQUE1()
    elif "SEGUN_BLOQUE->epsilon" in predictions:
        return
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
    elif "SEGUN_BLOQUE1->epsilon" in predictions:
        return
    else:
        print syntax_error("SEGUN_BLOQUE1", token, False)

def CASO_LISTA():
    global token
    if token.type in predictions["CASO_LISTA->caso-EXPRESION-token_dosp-BLOQUE-CASO_LISTA"]:
        match("caso")
        EXPRESION()
        match("token_dosp")
        BLOQUE()
        CASO_LISTA()
    elif "CASO_LISTA->epsilon" in predictions:
        return
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
    elif "OTRO_BLOQUE->epsilon" in predictions:
        return
    else:
        print syntax_error("OTRO_BLOQUE", token, False)

def LISTA_EXPR():
    global token
    if token.type in predictions["LISTA_EXPR->EXPRESION-LISTA_EXPR1"]:
        EXPRESION()
        LISTA_EXPR1()
    elif token.type in predictions["LISTA_EXPR->OPERADOR-TERMINO-LISTA_EXPR"]:
        OPERADOR()
        TERMINO()
        LISTA_EXPR()
    elif "LISTA_EXPR->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_EXPR", token, False)

def LISTA_EXPR1():
    global token
    if token.type in predictions["LISTA_EXPR1->token_coma-LISTA_EXPR1"]:
        match("token_coma")
        LISTA_EXPR1()
    elif token.type in predictions["LISTA_EXPR1->EXPRESION"]:
        EXPRESION()
    elif "LISTA_EXPR1->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_EXPR1", token, False)

def LISTA_ID():
    global token
    if token.type in predictions["LISTA_ID->id-LISTA_ID1"]:
        match("id")
        LISTA_ID1()
    elif "LISTA_ID->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_ID", token, False)

def LISTA_ID1():
    global token
    if token.type in predictions["LISTA_ID1->token_coma-id-LISTA_ID1"]:
        match("token_coma")
        match("id")
        LISTA_ID1()
    elif "LISTA_ID1->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_ID1", token, False)

def ESCRIBIR():
    global token
    if token.type in predictions["ESCRIBIR->escribir-LISTA_EXPR-token_pyc"]:
        match("escribir")
        LISTA_EXPR()
        match("token_pyc")
    elif "ESCRIBIR->epsilon" in predictions:
        return
    else:
        print syntax_error("ESCRIBIR", token, False)

def ESPERAR_BLOQUE():
    global token
    if token.type in predictions["ESPERAR_BLOQUE->esperar-ESPERAR_BLOQUE1"]:
        match("esperar")
        ESPERAR_BLOQUE1()
    elif "ESPERAR_BLOQUE->epsilon" in predictions:
        return
    else:
        print syntax_error("ESPERAR_BLOQUE", token, False)

def ESPERAR_BLOQUE1():
    global token
    if token.type in predictions["ESPERAR_BLOQUE1->tecla-token_pyc"]:
        match("tecla")
        match("token_pyc")
    elif token.type in predictions["ESPERAR_BLOQUE1->EXPRESION-MEDIDA_TIEMPO-token_pyc"]:
        EXPRESION()
        MEDIDA_TIEMPO()
        match("token_pyc")
    elif "ESPERAR_BLOQUE1->epsilon" in predictions:
        return
    else:
        print syntax_error("ESPERAR_BLOQUE1", token, False)

def MEDIDA_TIEMPO():
    global token
    if token.type in predictions["MEDIDA_TIEMPO->segundos"]:
        match("segundos")
    elif token.type in predictions["MEDIDA_TIEMPO->milisegundos"]:
        match("milisegundos")
    elif "MEDIDA_TIEMPO->epsilon" in predictions:
        return
    else:
        print syntax_error("MEDIDA_TIEMPO", token, False)

def LEER():
    global token
    if token.type in predictions["LEER->leer-LISTA_ID-token_pyc"]:
        match("leer")
        LISTA_ID()
        match("token_pyc")
    elif "LEER->epsilon" in predictions:
        return
    else:
        print syntax_error("LEER", token, False)

def EXPRESION():
    global token
    if token.type in predictions["EXPRESION->TERMINO-LISTA_EXPR"]:
        TERMINO()
        LISTA_EXPR()
    elif "EXPRESION->epsilon" in predictions:
        return
    else:
        print syntax_error("EXPRESION", token, False)

def TERMINO():
    global token
    if token.type in predictions["TERMINO->FACTOR-LISTA_FACTOR"]:
        FACTOR()
        LISTA_FACTOR()
    elif "TERMINO->epsilon" in predictions:
        return
    else:
        print syntax_error("TERMINO", token, False)

def LISTA_FACTOR():
    global token
    if token.type in predictions["LISTA_FACTOR->OPERADOR-FACTOR-LISTA_FACTOR"]:
        OPERADOR()
        FACTOR()
        LISTA_FACTOR()
    elif "LISTA_FACTOR->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_FACTOR", token, False)

def FACTOR():
    global token
    if token.type in predictions["FACTOR->token_par_izq-EXPRESION-token_par_der"]:
        match("token_par_izq")
        EXPRESION()
        match("token_par_der")
    elif token.type in predictions["FACTOR->LLAMADA_ID_PROC"]:
        LLAMADA_ID_PROC()
    elif token.type in predictions["FACTOR->token_real"]:
        match("token_real")
    elif token.type in predictions["FACTOR->token_entero"]:
        match("token_entero")
    elif token.type in predictions["FACTOR->token_cadena"]:
        match("token_cadena")
    elif token.type in predictions["FACTOR->verdadero"]:
        match("verdadero")
    elif token.type in predictions["FACTOR->falso"]:
        match("falso")
    elif token.type in predictions["FACTOR->token_neg-EXPRESION"]:
        match("token_neg")
        EXPRESION()
    elif "FACTOR->epsilon" in predictions:
        return
    else:
        print syntax_error("FACTOR", token, False)

def LLAMADA_ID_PROC():
    global token
    if token.type in predictions["LLAMADA_ID_PROC->id-LLAMADA_ID_PROC1"]:
        match("id")
        LLAMADA_ID_PROC1()
    elif "LLAMADA_ID_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("LLAMADA_ID_PROC", token, False)

def LLAMADA_ID_PROC1():
    global token
    if token.type in predictions["LLAMADA_ID_PROC1->PAR_PROC"]:
        PAR_PROC()
    elif token.type in predictions["LLAMADA_ID_PROC1->LISTA_DIM"]:
        LISTA_DIM()
    elif "LLAMADA_ID_PROC1->epsilon" in predictions:
        return
    else:
        print syntax_error("LLAMADA_ID_PROC1", token, False)

def PAR_PROC():
    global token
    if token.type in predictions["PAR_PROC->token_par_izq-LISTA_PAR_PROC-token_par_der"]:
        match("token_par_izq")
        LISTA_PAR_PROC()
        match("token_par_der")
    elif "PAR_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("PAR_PROC", token, False)

def LISTA_DIM():
    global token
    if token.type in predictions["LISTA_DIM->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1"]:
        match("token_cor_izq")
        EXPRESION()
        match("token_cor_der")
        LISTA_DIM1()
    elif "LISTA_DIM->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_DIM", token, False)

def LISTA_DIM1():
    global token
    if token.type in predictions["LISTA_DIM1->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1"]:
        match("token_cor_izq")
        EXPRESION()
        match("token_cor_der")
        LISTA_DIM1()
    elif "LISTA_DIM1->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_DIM1", token, False)

def LISTA_PAR_PROC():
    global token
    if token.type in predictions["LISTA_PAR_PROC->EXPRESION-LISTA_PAR_PROC1"]:
        EXPRESION()
        LISTA_PAR_PROC1()
    elif "LISTA_PAR_PROC->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_PAR_PROC", token, False)

def LISTA_PAR_PROC1():
    global token
    if token.type in predictions["LISTA_PAR_PROC1->token_coma-EXPRESION-LISTA_PAR_PROC1"]:
        match("token_coma")
        EXPRESION()
        LISTA_PAR_PROC1()
    elif "LISTA_PAR_PROC1->epsilon" in predictions:
        return
    else:
        print syntax_error("LISTA_PAR_PROC1", token, False)

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
    elif "TIPO_DATO->epsilon" in predictions:
        return
    else:
        print syntax_error("TIPO_DATO", token, False)

def OPERADOR():
    global token
    if token.type in predictions["OPERADOR->token_mas"]:
        match("token_mas")
    elif token.type in predictions["OPERADOR->token_menos"]:
        match("token_menos")
    elif token.type in predictions["OPERADOR->token_div"]:
        match("token_div")
    elif token.type in predictions["OPERADOR->token_mul"]:
        match("token_mul")
    elif token.type in predictions["OPERADOR->token_mod"]:
        match("token_mod")
    elif token.type in predictions["OPERADOR->token_pot"]:
        match("token_pot")
    elif token.type in predictions["OPERADOR->token_igual"]:
        match("token_igual")
    elif token.type in predictions["OPERADOR->token_dif"]:
        match("token_dif")
    elif token.type in predictions["OPERADOR->token_menor"]:
        match("token_menor")
    elif token.type in predictions["OPERADOR->token_mayor"]:
        match("token_mayor")
    elif token.type in predictions["OPERADOR->token_menor_igual"]:
        match("token_menor_igual")
    elif token.type in predictions["OPERADOR->token_mayor_igual"]:
        match("token_mayor_igual")
    elif token.type in predictions["OPERADOR->token_y"]:
        match("token_y")
    elif token.type in predictions["OPERADOR->token_o"]:
        match("token_o")
    elif "OPERADOR->epsilon" in predictions:
        return
    else:
        print syntax_error("OPERADOR", token, False)

grammar = "" \
        "PSEINT->FUNCION_SUBPROC-PROCESO-FUNCION_SUBPROC:funcion,subproceso,proceso,algoritmo;" \
        "FUNCION_SUBPROC->PROC-FUNCION_SUBPROC:funcion,subproceso;" \
        "FUNCION_SUBPROC->epsilon:proceso,algoritmo,token_eof;" \
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
        "FIRMA->ARG_PROC:token_par_izq;" \
        "ARG_PROC->token_par_izq-LISTA_ARG_PROC-token_par_der:token_par_izq;" \
        "ARG_PROC->epsilon:token_asig,token_par_izq,definir,dimension,para,repetir,id,mientras,si,borrar,limpiar,escribir,leer,esperar,segun;" \
        "LISTA_ARG_PROC->id-LISTA_ARG_PROC1:id;" \
        "LISTA_ARG_PROC->epsilon:token_par_der;" \
        "LISTA_ARG_PROC1->token_coma-id-LISTA_ARG_PROC1:token_coma;" \
        "LISTA_ARG_PROC1->epsilon:token_par_der;" \
        "BLOQUE->DECLARACION-BLOQUE:definir;" \
        "BLOQUE->ASIGNACION-BLOQUE:id;" \
        "BLOQUE->DIMENSION-BLOQUE:dimension;" \
        "BLOQUE->SI_BLOQUE-BLOQUE:si;" \
        "BLOQUE->PARA_BLOQUE-BLOQUE:para;" \
        "BLOQUE->MIENTRAS_BLOQUE-BLOQUE:mientras;" \
        "BLOQUE->REPETIR_BLOQUE-BLOQUE:repetir;" \
        "BLOQUE->SEGUN_BLOQUE-BLOQUE:segun;" \
        "BLOQUE->OTRO_BLOQUE-BLOQUE:borrar,limpiar,escribir,leer,esperar;" \
        "BLOQUE->epsilon:caso,finsegun,hasta,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "DECLARACION->definir-LISTA_ID-como-TIPO_DATO-token_pyc:definir;" \
        "ASIGNACION->id-ASIGNACION1:id;" \
        "ASIGNACION1->token_cor_izq-LISTA_EXPR-token_cor_der-token_asig-EXPRESION-token_pyc:token_cor_izq;" \
        "ASIGNACION1->token_asig-EXPRESION-token_pyc:token_asig;" \
        "DIMENSION->dimension-id-token_cor_izq-LISTA_EXPR-token_cor_der-token_pyc:dimension;" \
        "SI_BLOQUE->si-EXPRESION-entonces-BLOQUE-SI_BLOQUE1:si;" \
        "SI_BLOQUE1->sino-BLOQUE-finsi:sino;" \
        "SI_BLOQUE1->finsi:finsi;" \
        "PARA_BLOQUE->para-id-token_asig-EXPRESION-hasta-EXPRESION-con-paso-EXPRESION-hacer-BLOQUE-finpara:para;" \
        "MIENTRAS_BLOQUE->mientras-EXPRESION-hacer-BLOQUE-finmientras:mientras;" \
        "REPETIR_BLOQUE->repetir-BLOQUE-hasta-que-EXPRESION:repetir;" \
        "SEGUN_BLOQUE->segun-EXPRESION-hacer-CASO_LISTA-SEGUN_BLOQUE1:segun;" \
        "SEGUN_BLOQUE1->finsegun:finsegun;" \
        "SEGUN_BLOQUE1->de-otro-modo-token_dosp-BLOQUE-finsegun:de;" \
        "CASO_LISTA->caso-EXPRESION-token_dosp-BLOQUE-CASO_LISTA:caso;" \
        "CASO_LISTA->epsilon:finsegun,de;" \
        "OTRO_BLOQUE->borrar-pantalla:borrar;" \
        "OTRO_BLOQUE->ESCRIBIR:escribir;" \
        "OTRO_BLOQUE->ESPERAR_BLOQUE:esperar;" \
        "OTRO_BLOQUE->LEER:leer;" \
        "OTRO_BLOQUE->limpiar-pantalla:limpiar;" \
        "LISTA_EXPR->EXPRESION-LISTA_EXPR1:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
        "LISTA_EXPR->OPERADOR-TERMINO-LISTA_EXPR:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o;" \
        "LISTA_EXPR->epsilon:token_pyc,token_cor_der,token_coma,token_par_der,segundos,milisegundos,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_dosp,hacer,hasta,con,entonces,token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "LISTA_EXPR1->token_coma-LISTA_EXPR1:token_coma;" \
        "LISTA_EXPR1->EXPRESION:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
        "LISTA_EXPR1->epsilon:token_pyc,token_cor_der,token_coma,token_par_der,segundos,milisegundos,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_dosp,hacer,hasta,con,entonces,token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "LISTA_ID->id-LISTA_ID1:id;" \
        "LISTA_ID1->token_coma-id-LISTA_ID1:token_coma;" \
        "LISTA_ID1->epsilon:token_pyc,como;" \
        "ESCRIBIR->escribir-LISTA_EXPR-token_pyc:escribir;" \
        "ESPERAR_BLOQUE->esperar-ESPERAR_BLOQUE1:esperar;" \
        "ESPERAR_BLOQUE1->tecla-token_pyc:tecla;" \
        "ESPERAR_BLOQUE1->EXPRESION-MEDIDA_TIEMPO-token_pyc:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
        "MEDIDA_TIEMPO->segundos:segundos;" \
        "MEDIDA_TIEMPO->milisegundos:milisegundos;" \
        "LEER->leer-LISTA_ID-token_pyc:leer;" \
        "EXPRESION->TERMINO-LISTA_EXPR:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
        "TERMINO->FACTOR-LISTA_FACTOR:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
        "LISTA_FACTOR->OPERADOR-FACTOR-LISTA_FACTOR:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o;" \
        "LISTA_FACTOR->epsilon:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "FACTOR->token_par_izq-EXPRESION-token_par_der:token_par_izq;" \
        "FACTOR->LLAMADA_ID_PROC:id;" \
        "FACTOR->token_real:token_real;" \
        "FACTOR->token_entero:token_entero;" \
        "FACTOR->token_cadena:token_cadena;" \
        "FACTOR->verdadero:verdadero;" \
        "FACTOR->falso:falso;" \
        "FACTOR->token_neg-EXPRESION:token_neg;" \
        "LLAMADA_ID_PROC->id-LLAMADA_ID_PROC1:id;" \
        "LLAMADA_ID_PROC1->PAR_PROC:token_par_izq;" \
        "LLAMADA_ID_PROC1->LISTA_DIM:token_cor_izq;" \
        "LLAMADA_ID_PROC1->epsilon:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "PAR_PROC->token_par_izq-LISTA_PAR_PROC-token_par_der:token_par_izq;" \
        "LISTA_DIM->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1:token_cor_izq;" \
        "LISTA_DIM1->token_cor_izq-EXPRESION-token_cor_der-LISTA_DIM1:token_cor_izq;" \
        "LISTA_DIM1->epsilon:token_mas,token_menos,token_div,token_mul,token_mod,token_pot,token_igual,token_dif,token_menor,token_mayor,token_menor_igual,token_mayor_igual,token_y,token_o,token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id,token_coma,token_cor_der,token_par_der,segundos,milisegundos,token_dosp,hacer,hasta,con,entonces,token_pyc,definir,dimension,para,repetir,mientras,si,borrar,limpiar,escribir,leer,esperar,segun,caso,finsegun,finmientras,finpara,finsi,sino,finfuncion,finsubproceso,finproceso,finalgoritmo,de;" \
        "LISTA_PAR_PROC->EXPRESION-LISTA_PAR_PROC1:token_par_izq,token_real,token_entero,token_cadena,verdadero,falso,token_neg,id;" \
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


tokens = []
keywords = {}
operators = {}

initialize_keywords()
initialize_operators()
row = 0
col = 0

examples = 7
for i in range(7,examples + 1):
    stdin = open("ejemplos2/" + str(i) + ".in", "r")
    output_file = str(i) + ".out"
    stdout = open("output/" + output_file, "w")

    row = 0
    col = 0
    read_data()

    print "EXAMPLE", i

    token = get_next_token()
    PSEINT()

    stdout.close()

    #assert join_file("ejemplos/" + output_file) == join_file("output/" + output_file), "Error in file " + output_file




