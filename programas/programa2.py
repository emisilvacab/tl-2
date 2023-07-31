# -*- coding: utf-8 -*-
import sys
import io
import nltk
from nltk.tree import Tree
from nltk import CFG

def parse(s):
    grammar = """
    S -> S 'a''n''d' S | S 'o''r' S | 'n''o''t' S | L | '(' S ')' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' 
    """
    grammar = nltk.CFG.fromstring(grammar)
    s = s.strip()
    s_tokenized = list(s.replace(" ", ""))
    parser = nltk.LeftCornerChartParser(grammar)
    ini = list(parser.parse(s_tokenized))[:1]
    if list(ini):
        return devolverFormaPrefija(list(parser.parse(s_tokenized)))
    else:
        return list()


def devolverFormaPrefija(tree):
    cont = 0
    for child in tree:
        if isinstance(child, Tree):
            cont = cont + 1
    if cont>0:
        if tree[0][0] == '(':
            return devolverFormaPrefija2(list(tree[0][1]))
        else:
            if tree[0][0] == 'n' and tree[0][1] == 'o' and tree[0][2] == 't':
                aux = ['not', '(']
                aux.extend(devolverFormaPrefija2(list(tree[0][3])))
                aux.append(')')
                return aux
            else:
                if tree[0][1] == 'o' and tree[0][2] == 'r':
                    aux = ['or(']
                    aux.extend(devolverFormaPrefija2(list(tree[0][0])))
                    aux.append(',')
                    aux.extend(devolverFormaPrefija2(list(tree[0][3])))
                    aux.append(')')
                    return aux
                else:
                    if tree[0][1] == 'a' and tree[0][2] == 'n' and tree[0][3] == 'd':
                        aux = ['and(']
                        aux.extend(devolverFormaPrefija2(list(tree[0][0])))
                        aux.append(',')
                        aux.extend(devolverFormaPrefija2(list(tree[0][4])))
                        aux.append(')')
                        return aux
    else:
        return tree


def devolverFormaPrefija2(tree):
    cont = 0
    for child in tree:
        if isinstance(child, Tree):
            cont = cont + 1
    if cont > 0:
        if tree[0] == '(':
            return devolverFormaPrefija2(list(tree[1]))
        else:
            if tree[0] == 'n' and tree[1] == 'o' and tree[2] == 't':
                aux = ['not', '(']
                aux.extend(devolverFormaPrefija2(list(tree[3])))
                aux.append(')')
                return aux
            else:
                if tree[1] == 'o' and tree[2] == 'r':
                    aux = ['or(']
                    aux.extend(devolverFormaPrefija2(list(tree[0])))
                    aux.append(',')
                    aux.extend(devolverFormaPrefija2(list(tree[3])))
                    aux.append(')')
                    return aux
                else:
                    if tree[1] == 'a' and tree[2] == 'n' and tree[3] == 'd':
                        aux = ['and(']
                        aux.extend(devolverFormaPrefija2(list(tree[0])))
                        aux.append(',')
                        aux.extend(devolverFormaPrefija2(list(tree[4])))
                        aux.append(')')
                        return aux
    else:
        return tree


if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
        lista = parse(s)
        salida = "".join(lista)
        if len(lista) == 0:
            salida = "NO PERTENECE"
    except ValueError:
        salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
