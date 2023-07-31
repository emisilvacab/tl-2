# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.tree import Tree
import nltk.tree
from nltk import CFG


def parse(s):
    # V verbos
    # GF es grupo nominal femenino
    # GM es grupo nominal masculino
    # NPF nombres propios femenino
    # NPM nombres propios masculino
    # DF determinantes femeninos
    # DM determinantes masculinos
    # NF nominales femeninos #revienta aca
    # NM nominales masculinos
    grammar = """
    S -> G V GM | G V GF
    V -> 'come' | 'descubre' | 'aplasta'  | 'salta' | 'trepa'
    G -> NPF | NPM | DF  NF | DM  NM
    GF -> NPF | DF  NF
    GM -> NPM | DM  NM
    NPF -> 'Julia' | 'Marta'
    NPM -> 'Pedro' | 'Juan'
    DF -> 'la' | 'una' | 'esa' | 'tu'
    DM -> 'el' | 'un' | 'ese' | 'tu'
    NF -> 'manzana' | 'banana' | 'naranja' | 'pera' | 'frutilla' | 'perra' | 'gata' | 'elefante'
    NM -> 'kiwi' | 'mango' | 'perro' | 'gato' | 'elefante' | 'hueso' | 'pescado'
    """
    grammar = nltk.CFG.fromstring(grammar)
    s = s.strip()
    s_tokenized = s.split(" ")
    parser = nltk.LeftCornerChartParser(grammar)
    ini = list(parser.parse(s_tokenized))[:1]
    if list(ini):
        return devolverVozPasiva(parser.parse(s_tokenized))
    else:
        return list()


def devolverVozPasiva(tree):
    principio = ""
    final = ""
    medio = ""
    for S in tree:
        for child in S:
            if child.label() == "G":
                for node in child:
                    if node.label() == "NPF" or node.label() == "NPM" or node.label() == "DF" or node.label() == "DM":
                        for i in node:
                            final = final + i
                    else:
                        if node.label() == "NF" or node.label() == "NM":
                            final = final + " "
                            for i in node:
                                final = final + i
            else:
                if child.label() == "V":
                    for node in child:
                        medio = medio + node
                else:
                    if child.label() == "GF":
                        match medio:
                            case "come":
                                medio = "es comida por"
                            case "descubre":
                                medio = "es descubierta por"
                            case "aplasta":
                                medio = "es aplastada por"
                            case "salta":
                                medio = "es saltada por"
                            case _:
                                medio = "es trepada por"
                        for node in child:
                            if node.label() == "NPF" or node.label() == "DF":
                                for i in node:
                                    principio = principio + i
                            else:
                                principio = principio + " "
                                for i in node:
                                    principio = principio + i
                    else:
                        if child.label() == "GM":
                            match medio:
                                case "come":
                                    medio = "es comido por"
                                case "descubre":
                                    medio = "es descubierto por"
                                case "aplasta":
                                    medio = "es aplastado por"
                                case "salta":
                                    medio = "es saltado por"
                                case _:
                                    medio = "es trepado por"
                            for node in child:
                                if node.label() == "NPM" or node.label() == "DM":
                                    for i in node:
                                        principio = principio + i
                                else:
                                    principio = principio + " "
                                    for i in node:
                                        principio = principio + i
    res = principio + " " + medio + " " + final
    return list(res)


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
