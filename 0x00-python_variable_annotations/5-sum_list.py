#!/usr/bin/env python3
"""Define a  sum_list type-annotated function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of float as argument and returns their sum as a float"""
    return sum(input_list)
