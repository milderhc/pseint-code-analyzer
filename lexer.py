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
