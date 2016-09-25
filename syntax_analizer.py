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
        for p in pred:
            expected[left_part][p] = True

def syntax_error(expec, token, error_syntax_in_match):
    error = ""
    error += "Error sintactico: se encontro \"" + token + "\"; se esperaba: "
    return error

def match(expected_token):
    global token
    if token == expected_token:
        print token, "matched"
        token = next_token()
    else:
        print syntax_error(expected_token, token, True)

def A():
    global token
    if token in predictions["A->B-uno"]:
        B()
        match("uno")
    elif token in predictions["A->dos"]:
        match("dos")
    else:
        print syntax_error("A", token, False)

def B():
    global token
    if token in predictions["B->tres"]:
        match("tres")
    elif token in predictions["B->cuatro"]:
        match("cuatro")
    else:
        print syntax_error("B", token, False)

cont = 0
def next_token():
    global cont
    cont += 1
    if cont == 1:
        return "cuatro"
    if cont == 2:
        return "un"

grammar = "" \
        "A->B-uno:tres,cuatro;" \
        "A->dos:dos;" \
        "B->tres:tres;" \
        "B->cuatro:cuatro"
expected = {}
predictions = {}
generate_prediction_sets(grammar)
token = next_token()
A()
