#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

Implement a `get_hyper_index` method with two integer arguments:
`index` with a None default value and `page_size` with default value
of 10.

The method should return a dictionary with the following key-value pairs:
    - `index`: the current start index of the return page. That is the
    index of the first item in the current page. For example if requesting
    page 3 with `page_size` 20, and no data was removed form the dataset.
    The current index should be 60.
    - `next_index`: the next index of the query with. That should be the
    index of the first item after the last item on the current page.
    - `page_size`: the current page size.
    - `data`: the actual page of the dataset.
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index
        indexed_dataset = self.indexed_dataset()
        indexes = indexed_dataset.keys()
        assert min(indexes) <= index <= max(indexes)

        page_data = []
        current_index = index

        count = 0
        found_start_index = False
        for idx, data in indexed_dataset.items():
            if count == page_size:
                next_index = idx
                break

            if idx >= index:
                if not found_start_index:
                    current_index = idx
                    found_start_index = True
                count += 1
                page_data.append(data)

        page_info = {
            "index": current_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
        return page_info
