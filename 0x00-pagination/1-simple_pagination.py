#!/usr/bin/env python3
"""a python module that returns the start and end index of a page"""
from typing import Tuple, List
import csv
import math


index_range = __import__('0-simple_helper_function').index_range


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
        """get_page method implementation"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if page * page_size > len(dataset):
            return []
        return [dataset[start_index:end_index]]
