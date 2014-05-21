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
        if ast[0] == "quote":
            return ast[1]

        if ast[0] == "define":
            if not len(ast) == 3:
                raise LispError("Wrong number of arguments")
            if not is_symbol(ast[1]):
                raise LispError("non-symbol")
            env.set(ast[1], evaluate(ast[2], env))
            return

        if ast[0] == "if":
            if evaluate(ast[1], env):
                return evaluate(ast[2], env)
            else:
                return evaluate(ast[3], env)

        if ast[0] == "atom":
            return is_atom(evaluate(ast[1], env))

        if ast[0] == "eq":
            if not is_atom(evaluate(ast[1], env)) or not is_atom(evaluate(ast[2], env)):
                return False
            return evaluate(ast[1], env) == evaluate(ast[2], env)

        try:
            if ast[0] == "+":
                return evaluate(ast[1], env) + evaluate(ast[2], env)
            if ast[0] == "-":
                return evaluate(ast[1], env) - evaluate(ast[2], env)
            if ast[0] == "/":
                return evaluate(ast[1], env) / evaluate(ast[2], env)
            if ast[0] == "*":
                return evaluate(ast[1], env) * evaluate(ast[2], env)
            if ast[0] == "mod":
                return evaluate(ast[1], env) % evaluate(ast[2], env)
            if ast[0] == "<":
                return evaluate(ast[1], env) < evaluate(ast[2], env)
            if ast[0] == ">":
                return evaluate(ast[1], env) > evaluate(ast[2], env)
        except TypeError:
            raise LispError("TypeError")


    if is_symbol(ast):
        return env.lookup(ast)
    else:
        return ast
