# -*- coding: utf-8 -*-

import sys
import io
import nltk

def parse(s):
    grammar = """
    S -> X C | A Y | Z
    X -> "a" X "b" | "a" "b"
    C -> C "c" | "c"
    A -> "a" A | a
    Y -> "b" Y "c" | "b" "c"
    Z -> "a" B "c" | "a" Z "c"
    B -> "b" B | "b"
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
