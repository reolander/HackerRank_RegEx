import re

d = {'C': 1, 'CPP': 1, 'JAVA': 1, 'PYTHON': 1, 'PERL': 1,'PHP': 1, 'RUBY': 1,'CSHARP': 1,'HASKELL': 1, 'CLOJURE': 1, 'BASH': 1, 'SCALA': 1, 'ERLANG': 1,'CLISP': 1, 'LUA': 1, 'BRAINFUCK': 1, 'JAVASCRIPT': 1, 'GO': 1, 'D': 1, 'OCAML': 1, 'R': 1,'PASCAL': 1,'SBCL': 1, 'DART': 1, 'GROOVY': 1, 'OBJECTIVEC':1}

for _ in range(int(input())):
  s = input().split()
  if d.get(s[1]):
    print('VALID')
  else:
    print('INVALID')

