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

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict[str, int]:
        """
        Self updates users page content even when some indexes
        has been deleted.

        Args:
            index (int, optional): Current start index. Defaults to None.
            page_size (int, optional): page content size. Defaults to 10.

        Returns:
            Dict[str, int]: Returns content based on the start index, if
            the start index is not found then return the next index with the
            same amount of page content.

        ALGORITHM
        ---------

        1. Check if the `index` still contains the default argument None, if
        yes raise an AssertionError. You can also return an empty dictionary.
        2. Retrieve and store the indexed dataset with the variable name
        `indexed_dataset`.
        3. Get the list of indexes from the indexed dataset using the
        dictionary `keys` method.
        4. Verify that the index passed in as an argument falls into the range
        of the minimum index and the maximum index.
        5. Create an empty list with the variable name `page_data`, this would
        store the contents of the page requested for by the user.
        6. Set the `index` as the `current_index`, this might change if the
        index pass upon method call is not found within the `indexed_dataset`.
        7. Create a variable `count` that is assigned 0 at the begining of the
        loop. This `count` variable would act as a control flow/ control
        logic that enables
        the while loop to end if the required page content has be retrieved.
        8. Because the database might be update at each page call,
        we would need to find the start index of each page content call,
        using the variable `found_start_index` we can easily find the
        first index that meet the condition in code line 123.
        9. Using the dictionary method `.items()` we get the key and value pair
        within a tuple.
        10. If the content count is equal to page size do this:
            i. Save the next_index using the key(i.e. idx).
            ii. End the for loop.
        11. If the current loop key value is equal to or greater than the index
        argument then:
            i. Check if the starting index has been found, if it has continue,
            if it has not then update the current index to the key value,
            and assign `found_start_index` to be true.
        12. Update the page content add count.
        13. Finally add the retrieved data to `page_data`.
        """
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
