#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

print(inspect.getsource(enclosing_funcion))