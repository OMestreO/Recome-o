import ast

expressao = "2 + 3 * (4 - 1)"
arvore_sintatica = ast.parse(expressao, mode='eval')
print(ast.dump(arvore_sintatica))