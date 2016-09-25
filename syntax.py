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
    write_line("error += \"<\" + str(token.row) + \",\" + str(token.col) + \"> Error sintactico: "\
               "se encontro \\\"\" + token.lexema + \"\\\"; se esperaba: \"", 1)
    write_line("if error_syntax_in_match:", 1)
    write_line("error += \"\\\"\" + expec + \"\\\".\"", 2)
    write_line("else:", 1)
    write_line("for e in expected[expec]:", 2)
    write_line("error += \"\\\"\" + e + \"\\\",\"", 3)
    write_line("return error", 1)
    write_line("", 0)

def generate_match():
    write_line("def match(expected_token):", 0)
    write_line("global token", 1)
    write_line("if token.type == expected_token:", 1)
    write_line("print token.type, \"matched\"", 2)
    write_line("token = get_next_token()", 2)
    write_line("else:", 1)
    write_line("print syntax_error(expected_token, token, True)", 2)
    write_line("", 0)

def generate_syntax_analyzer_code (grammar):
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
        else:
            write_line("elif token.type in predictions[\"" + string_rule(rule) + "\"]:", 1)

        for a in right_part:
            if is_terminal(a):
                write_line("match(\"" + a + "\")", 2)
            else:
                write_line(a + "()", 2)

        if i + 1 < len(grammar):
            if left_part != grammar[i + 1][0][0]:
                write_line("else:", 1)
                write_line("print syntax_error(\"" + left_part + "\", token, False)", 2)
                write_line("", 0)
        else:
            write_line("else:", 1)
            write_line("print syntax_error(\"" + left_part + "\", token, False)", 2)
            write_line("", 0)

        for prediction in pred:
            expected[prediction] = True

    generate_grammar_string(grammar)
    write_line("expected = {}", 0)
    write_line("predictions = {}", 0)
    write_line("generate_prediction_sets(grammar)", 0)
    write_line("token = get_next_token()", 0)
    write_line(grammar[0][0][0] + "()", 0)
    #write_line("if token != token_eof:", 0)
    #write_line("print syntax_error(\"eof\")", 1)


stdout = open("syntax_analizer.py", "w")
generate_syntax_analyzer_code(read_grammar("grammars/grammar1.txt"))
stdout.close()
