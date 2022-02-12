# -*- coding: utf-8 -*-
from . import helpers

def hello():
    """Returns the answer"""
    if helpers.get_answer():
        print('42')
