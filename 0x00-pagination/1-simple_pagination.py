#!/usr/bin/env python3
"""
Implement a method in the Server class named `get_page` that takes two
integers arguments page with the default value 1 and page_size with the
default value 10.

    - You have to use the CSV file "Popular_Baby_Names.csv".
    - Use `assert` to verify that both arguments are integers greater
    than 0.
    - Use `index_range` to find the correct indexes to paginate the
    dataset correctly and return the appropriate page of the dataset
    (i.e. the correct list of rows).
    - If the input arguments are out of range for the dataset, an empty
    list should be returned.
"""
import csv
import math
from typing import List, Tuple


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
        dataset = self.dataset()
        length_of_dataset = len(dataset)

        start_index, end_index = index_range(page, page_size)
        # If the end index i.e. the last content to be displayed
        # is less than or equal to the length of database content stored
        # return page content
        if end_index <= length_of_dataset:
            return dataset[start_index: end_index]
        return []
