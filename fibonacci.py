# -*- coding: utf-8 -*-
"""
Muhammet Furkan MUŞTU
160403041

"""

""" Function for nth fibonacci number """
  
def Fibonacci(n): 
    if n<0: 
        return ("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)