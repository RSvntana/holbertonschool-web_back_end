#!/usr/bin/env python3
""" simple helper function """
from typing import Tuple


def index_range(page, page_size):
    """ index range """
    idx = (page - 1) * page_size
    index = idx + page_size
    return (idx, index)
