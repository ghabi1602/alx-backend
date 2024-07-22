#!/usr/bin/env python3
"""a python module that returns the start and end index of a page"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """a function that returns a tuple"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
