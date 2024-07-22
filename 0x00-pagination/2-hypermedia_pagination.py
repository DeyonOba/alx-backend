#!/usr/bin/env python3
"""
Implements a `get_hyper` method that takes the same arguments as
the `get_page` method in 1_simple_pagination.py and returns a
dictionary containing the following key-value pairs:

    - `page_size`: the length of the returned dataset page
    - `page`: the current page number
    - `data`: the dataset page
    - `next_page`: number of the next page, None if no next page
    - `prev_page`: number of the previous page, None if no previous page
    - `total_pages`: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List, Dict, Union, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the content of a page using the current page number and
        the page size.

        Args:
            page (int, optional): current page number. Defaults to 1.
            page_size (int, optional): number of content in page.
            Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        page_content = self.dataset()
        self.length_of_dataset = len(page_content)

        self.start_index, self.end_index = index_range(page, page_size)
        # If the end index i.e. the last content to be displayed
        # is less than or equal to the length of database content stored
        # return page content
        if self.end_index <= self.length_of_dataset:
            return page_content[self.start_index: self.end_index]
        return []

    def get_hyper(
        self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Union[int, List[list], None]]:
        """Gets the current page details.

        Args:
            page (int, optional): current page number. Defaults to 1.
            page_size (int, optional): number of content in page.
            Defaults to 10.

        Returns:
            Dict[str, Union[int, List[list], None]]: page details
        """

        page_content = self.get_page(page, page_size)

        total_pages = math.ceil(self.length_of_dataset / page_size)
        current_page_size = len(page_content)
        next_page = page + 1 if page_content else None
        prev_page = None if page == 1 else page - 1

        page_details = {
            "page_size": current_page_size,
            "page": page,
            "data": page_content,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return page_details
