from compiler.tokenizer import Tokenizer
from compiler.parser import Parser
from compiler.interpreter import Interpreter

f = open('../examples/vars', 'r')
code = f.read()
f.close()

tokenizer = Tokenizer()
tokens = tokenizer.tokenize(code)

"""
for line in tokens:
    for token in line:
        print TOKENS[token[0]]
    print
"""

parser = Parser()
ast = parser.parse(tokens)

"""
for a in ast:
    print a
"""
 
interpreter = Interpreter()
interpreter.interpret(ast)