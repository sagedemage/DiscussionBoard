# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:00:28 2022

@author: salsa
"""

def utility_processor():
    def format_price(amount, currency="$"):
        return f"{amount:.2f}{currency}"
    
    return dict(format_price=format_price)