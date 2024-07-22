#!/usr/bin/env python3
"""
Module contains function name `index_range` that takes two integers `page`
and `page_size`.

The function should return a tuple of size of two containing a start index
and an end index corresponding to the range of indexes to return in a list
for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

Func prototype: index_range(page: int, page_size: int) -> Tuple[int, int]

Alogorithm
-----------

1. index_range(page, page_size) => (start_index, end_index)
2. index_range(3, 15) =>
3. start_index = (page - 1) * page_size => (3 - 1) * 15 => 30
4. end_index = (page * page_size) => (3 * 15) => 45
5. (start_index, end_index) => (30, 45)
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Get the start index and end index based on the current page number,
    and the page size.

    Args:
        page (int): The current page
        page_size (int): The size on content in the page

    Returns:
        Tuple[int, int]: Tuple containing the start index, and end index
    """
    start_index = (page - 1) * page_size
    end_index = (page * page_size)
    return start_index, end_index
