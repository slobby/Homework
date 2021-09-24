#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect

a = "I am global variable!"


def enclosing_funcion1():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)
    
    return inner_function

def enclosing_funcion2_1():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        print(a)
    
    return inner_function

def enclosing_funcion2_2():
    a = "I am variable from enclosed function!"

    def inner_function():

        print(a)
    
    return inner_function

if __name__ == "__main__":
    enclosing_funcion1()()
    enclosing_funcion2_1()()
    enclosing_funcion2_2()()