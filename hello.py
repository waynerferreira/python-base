#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua congfigurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:
  export LANG=pt_br

execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Wayner Ferreira"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "es_US")[:5]

#if __name__ == "__name__":
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"        

print(msg)