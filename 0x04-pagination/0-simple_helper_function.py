#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page: page number int
        page_size: page size int
    Returns:
        The function should return a tuple
        of size two containing a start index and an end index
    """
    idx_start = (page - 1) * page_size
    idx_end = idx_start + page_size
    return (idx_start, idx_end)
