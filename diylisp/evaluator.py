# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""

def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""

    

    if is_list(ast):

        evald = []
        for exp in ast:
            evald.append(evaluate(exp, env))
            if ast[0] == "quote":
                return ast[1]

        if ast[0] == "atom":
            return is_atom(evald[1])

        if ast[0] == "eq":
            if not is_atom(evald[1]) or not is_atom(evald[2]):
                return False
            return evald[1] == evald[2]

        try:
            if ast[0] == "+":
                return evald[1] + evald[2]
            if ast[0] == "-":
                return evald[1] - evald[2]
            if ast[0] == "/":
                return evald[1] / evald[2]
            if ast[0] == "*":
                return evald[1] * evald[2]
            if ast[0] == "mod":
                return evald[1] % evald[2]
            if ast[0] == "<":
                return evald[1] < evald[2]
            if ast[0] == ">":
                return evald[1] > evald[2]
        except TypeError:
            raise LispError("TypeError")


    return ast
    raise NotImplementedError("DIY")
