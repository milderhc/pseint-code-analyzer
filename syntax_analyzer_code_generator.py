#####################################################################################################
################################ SYNTAX ANALYZER CODE GENERATOR #####################################
#####################################################################################################

def join_file (file):
    str = ""
    with open(file) as f:
        str += ";".join(line.strip() for line in f)
    return str

def read_grammar (grammar_file):
    txt_grammar = join_file(grammar_file)

    lines = txt_grammar.split(";")

    grammar = []

    for line in lines:
        rule_and_pred = line.split("|")

        rule = rule_and_pred[1]
        pred = rule_and_pred[2].strip().split(",")

        temp = rule.split(":")
        left_part = temp[0].strip()
        right_part = temp[1].strip().split()

        rule = (left_part, right_part)
        grammar.append((rule, pred))

    return grammar

def write_line(str, tabs):
    global stdout
    for i in xrange(tabs):
        stdout.write("    ")
    stdout.write(str + "\n")

def string_rule(rule):
    return rule[0] + "->" + "-".join(rule[1])

def is_terminal(a):
    return a.lower() == a

def generate_prediction_sets(grammar):
    write_line("def generate_prediction_sets(grammar):", 0)
    write_line("global expected", 1)
    write_line("grammar_array = grammar.split(\";\")", 1)
    write_line("for g in grammar_array:", 1)
    write_line("temp = g.split(\":\")", 2)
    write_line("rule = temp[0]", 2)
    write_line("left_part = rule.split(\"->\")[0]", 2)
    write_line("pred = temp[1]", 2)
    write_line("predictions[rule] = pred.split(\",\")", 2)
    write_line("if left_part not in expected:", 2)
    write_line("expected[left_part] = {}", 3)
    write_line("for p in predictions[rule]:", 2)
    write_line("expected[left_part][p] = True", 3)
    write_line("", 0)

def generate_grammar_string(grammar):
    write_line("grammar = \"\" \\", 0)
    for i in xrange(len(grammar)):
        rule = grammar[i][0]
        pred = grammar[i][1]
        write_line("\"" + string_rule(rule) + ":" + ",".join(line.strip() for line in pred) + (";\" \\" if i + 1 < len(grammar) else "\""), 2)

def generate_syntax_error():
    write_line("def syntax_error(expec, token, error_syntax_in_match):", 0)
    write_line("error = \"\"", 1)
    write_line("error += \"<\" + str(token.row) + \":\" + str(token.col) + \"> Error sintactico: "\
               "se encontro: \\\"\" + token.lexema + \"\\\"; se esperaba: \"", 1)
    write_line("if error_syntax_in_match:", 1)
    write_line("for e in alias:", 2)
    write_line("if e[0] in expec:", 3)
    write_line("error += \"\\\"\" + e[1] + \"\\\". \"", 4)
    write_line("break", 4)
    write_line("else:", 1)
    write_line("for e in alias:", 2)
    write_line("if e[0] in expected[expec]:", 3)
    write_line("error += \"\\\"\" + e[1] + \"\\\", \"", 4)

    write_line("return error[:-2] + \".\"", 1)
    write_line("", 0)

def generate_match():
    write_line("def match(expected_token):", 0)
    write_line("global token", 1)
    write_line("if token.type == expected_token:", 1)
    write_line("token = get_next_token()", 2)
    write_line("else:", 1)
    write_line("print syntax_error(expected_token, token, True)", 2)
    write_line("return False", 2)
    write_line("return True", 1)
    write_line("", 0)

def copy_lexer(lexer):
    global stdout
    stdin = open(lexer, "r")
    for line in stdin:
        stdout.write(line)

def generate_run_syntax_analyzer(grammar):
    write_line("def run_syntax_analyzer(input = None, output = None):", 0)
    write_line("global token", 1)
    write_line("if output != None:", 1)
    write_line("stdout = open(input,\"r\")", 2)
    write_line("", 0)
    write_line("generate_tokens(input)", 1)
    write_line("process_missing_error = True", 1)
    write_line("for t in tokens:", 1)
    write_line("if t.type == \"proceso\" or t.type == \"algoritmo\":", 2)
    write_line("process_missing_error = False", 3)
    write_line("break", 3)
    write_line("if process_missing_error:", 1)
    write_line("print \"Error sintactico: falta proceso.\"", 2)
    write_line("return", 2)
    write_line("token = get_next_token()", 1)
    write_line("if " + grammar[0][0][0] + "():", 1)
    write_line("print \"El analisis sintactico ha finalizado exitosamente.\"", 2)
    write_line("if output != None:", 2)
    write_line("stdout.write(\"El analisis sintactico ha finalizado exitosamente.\" + \"\\n\")", 3)
    # write_line("if token != token_eof:", 0)
    # write_line("print syntax_error(\"eof\")", 1)
    write_line("", 0)


def set_title():
    write_line("", 0)
    write_line("#####################################################################################################", 0)
    write_line("######################################### SYNTAX ANALYZER ###########################################", 0)
    write_line("#####################################################################################################", 0)
    write_line("", 0)


def generate_syntax_analyzer_code (grammar, lexer = "lexer.py"):
    copy_lexer(lexer)
    set_title()
    generate_prediction_sets(grammar)
    generate_syntax_error()
    generate_match()

    left_parts = {}
    expected = {}
    for i in xrange(len(grammar)):
        rule = grammar[i][0]
        pred = grammar[i][1]

        left_part = rule[0]
        right_part = rule[1]

        if left_part not in left_parts:
            write_line("def " +  left_part + "():", 0)
            write_line("global token", 1)
            write_line("if token.type in predictions[\"" + string_rule(rule) + "\"]:", 1)
            left_parts[left_part] = True

            for a in right_part:
                if is_terminal(a):
                    write_line("if not match(\"" + a + "\"):", 2)
                    write_line("return False", 3)
                else:
                    write_line("if not " + a + "():", 2)
                    write_line("return False", 3)
        else:
            if (len(right_part) == 1 and right_part[0] == "epsilon") == False:
                write_line("elif token.type in predictions[\"" + string_rule(rule) + "\"]:", 1)

                for a in right_part:
                    if is_terminal(a):
                        write_line("if not match(\"" + a + "\"):", 2)
                        write_line("return False", 3)
                    else:
                        write_line("if not " + a + "():", 2)
                        write_line("return False", 3)

        if i + 1 < len(grammar):
            if left_part != grammar[i + 1][0][0]:
                write_line("elif \"" + left_part + "->epsilon\" in predictions:", 1)
                write_line("return True", 2)
                write_line("else:", 1)
                write_line("print syntax_error(\"" + left_part + "\", token, False)", 2)
                write_line("return False", 2)
                write_line("return True", 1)
                write_line("", 0)
        else:
            write_line("elif \"" + left_part + "->epsilon\" in predictions:", 1)
            write_line("return True", 2)
            write_line("else:", 1)
            write_line("print syntax_error(\"" + left_part + "\", token, False)", 2)
            write_line("return False", 2)
            write_line("return True", 1)
            write_line("", 0)

        for prediction in pred:
            expected[prediction] = True

    generate_run_syntax_analyzer(grammar)
    generate_grammar_string(grammar)
    write_line("expected = {}", 0)
    write_line("predictions = {}", 0)
    write_line("generate_prediction_sets(grammar)", 0)
    write_line("", 0)

    write_line("token = Token()", 0)
    write_line("run_syntax_analyzer(\"test-cases/E/L_P2_E2.in\")", 0)

    write_line("", 0)


stdout = open("syntax_analyzer.py", "w")
generate_syntax_analyzer_code(read_grammar("grammars/pseint_grammar.txt"))
stdout.close()
