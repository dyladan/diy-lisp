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

    if is_boolean(ast) or is_integer(ast):
        return ast

    if is_list(ast):
        op = ast[0]

        if is_closure(op):
            if len(ast) == 1:
                args = []
            else:
                args = ast[1:]

            eval_args = []
            for arg in args:
                if is_list(arg):
                    eval_args.append(evaluate(arg, env))
                else:
                    eval_args.append(arg)

            return evaluate(op.body, op.env.extend(dict(zip(op.params, eval_args))))


        if op == "lambda":
            if not len(ast) == 3:
                msg = "number of arguments"
                raise LispError(msg)
            closure = Closure(env, ast[1], ast[2])
            if not is_list(ast[1]):
                raise LispError
            return closure

        if op == "quote":
            assert_exp_length(ast, 2)
            return ast[1]


        if op == "atom":
            assert_exp_length(ast, 2)
            arg = evaluate(ast[1], env)
            return is_atom(arg)

        if op == "eq":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_atom(arg1) or not is_atom(arg2):
                return False

            return arg1 == arg2

        if op == "+":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 + arg2

        if op == "-":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 - arg2

        if op == "/":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 / arg2

        if op == "*":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 * arg2

        if op == "mod":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 % arg2

        if op == ">":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 > arg2

        if op == "<":
            assert_exp_length(ast, 3)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            if not is_integer(arg1):
                raise LispError
            if not is_integer(arg2):
                raise LispError
            return arg1 < arg2

        if op == "if":
            assert_exp_length(ast, 4)
            arg1 = evaluate(ast[1], env)
            arg2 = evaluate(ast[2], env)
            arg3 = evaluate(ast[3], env)

            if arg1:
                return evaluate(arg2, env)
            else:
                return evaluate(arg3, env)

        if op == "define":
            assert_valid_definition(ast[1:])
            arg1 = ast[1]
            arg2 = evaluate(ast[2], env)
            env.set(arg1, arg2)


    else:
        return env.lookup(ast)


    return(ast)
