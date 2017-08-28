#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Autor: Giulliano Paz
# E-mail: giulliano94@gmail.com

# Importa a Classe
from textColors import TextColors

# Instancia a Classe
cor = TextColors()

# Para usar a classe, usa-se o método print da classe, a qual recebe 4 parâmetros
# O primeiro parâmentro é o texto a ser mostrado, o segundo é a cor da fonte
# o terceiro é a cor do fundo e por último é se é em negrito ou não

# cor.print(text=None, fontcolor=None, bgcolor=None, bold=False)
# Se os parâmetros forem informados com seus marcadores, podem ser informados em ordem diferentes

# Cor do texto branca, cor do fundo vermelha e em negrito
cor.print("\n Warning:", fontcolor="white", bold=True, bgcolor="red")

# Texto normal
print(" Normal text here\n\n")

# Cor do texto ciano e em negrito
cor.print("\nSample text here", fontcolor="cyan", bold=True)

# Cor do texto verde e em negrito
cor.print(" Two colors in same row", fontcolor="green", bold=True)

# Cor do texto branco, cor do fundo rosa e em negrito
cor.print("\n\n Sample background here\n\n", fontcolor="white",bgcolor="pink", bold=True)
print("\n")
