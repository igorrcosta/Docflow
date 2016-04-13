#!/usr/bin/env python
# -*- coding: utf-8 -*-
# construct.py

'''Create a simple docflow.'''

from model import *

def construct(phrases):
    doc = Docflow()
    stage = Stages()
    for phrase in phrases:
        stage.add_phrase(phrase)
    doc.add_stage(stage)
    doc.construct(drra)

if __name__ == '__main__':
    phrases = [
        'Olá!',
        'Mais uma frase.',
        'Última...']
    construct(phrases)
