#! /usr/bin/python
# -*- coding: UTF-8 -*-

# Autor: Giulliano Paz
# E-mail: giulliano94@gmail.com

# Classe para troca de cores de fontes e fundos
# para uma melhor destaque em execuções de código
class TextColors(object):

    ################ Método para trocar cores de fontes ###############
    def __init__(self):
        # Variável para deixar fonte em negrito
        self.bold = '\33[1m'

        self.default = '\33[0;0m'

        self.reverse = '\33[2m'

        # Dicionário de cores para o texto
        self.font = {
            #cores em inglês
            'black': '\33[30m',
            'red': '\33[31m',
            'green': '\33[32m',
            'yellow': '\33[33m',
            'blue': '\33[34m',
            'pink': '\33[35m',
            'cyan': '\33[36m',
            'white': '\33[37m',
            None: ''
        }
        # Dicionário de cores para fundo
        self.background = {
            #cores em inglês
            'black': '\33[40m',
            'red': '\33[41m',
            'green': '\33[42m',
            'yellow': '\33[43m',
            'blue': '\33[44m',
            'pink': '\33[45m',
            'cyan': '\33[46m',
            'white': '\33[47m',
            None: ''
        }

    #################### Método para informar erro ######################
    def error(self, arg):

        if arg == 'fontcolor': arg = 'Fonte'
        if arg == 'bgcolor': arg = 'Fundo'

        msg1 = "\n >> Cor não disponível para {}!".format(arg)
        msg2 = "\n\n >> Lista de cores: [black, red, green, yellow, blue, pink, cyan, white]\n\n"

        print("{}{}{}{}{}".format(self.bold, self.font['white'], self.background['red'], msg1, self.default), end='')
        print("{}{}{}{}{}".format(self.bold, self.font['white'], self.background['red'], msg2, self.default), end='')

    ############## Método para imprimir texto e fundos colorido ############
    def print(self, text=None, fontcolor=None, bgcolor=None, bold=False):

        # Verifica se fontcolor foi informada
        if fontcolor != None: fontcolor = fontcolor.rstrip("\n").strip("\n").rstrip(" ").strip(" ")
        # Verifica se fontcolor foi informada de forma correta
        if fontcolor not in self.font: self.error('fontcolor')

        # Verifica se bgcolor foi informado
        if bgcolor != None: bgcolor = bgcolor.rstrip("\n").strip("\n").rstrip(" ").strip(" ")
        # Verifica se bgcolor foi informado corretamente
        if bgcolor not in self.background: self.error('bgcolor')

        if bold != False: bold = self.bold

        # Imprime na tela o texto passado por parâmetro com as cores especificadas também por parâmetro
        # A sequência é imprimir  <bold> <fontcolor> <bgcolor> <text> <default>
        # <bold> deixa o texto em negrito, <fontcolor> muda a cor da fonte, <bgcolor> muda a cor do fundo
        # <text> é o texto informado pelo usuário e <default> faz voltar para as configuraçõe de cores padrão(Para não ficar sempre colorido)
        print("{}{}{}{}{}".format(bold, self.font[fontcolor], self.background[bgcolor], text, self.default), end='')