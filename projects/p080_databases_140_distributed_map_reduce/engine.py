"""
Project #080: Distributed Map-Reduce Streaming Pipeline Framework
Domain: Data Science & Databases
Description: Lightweight multi-stage mapping, partitioning, and reduction engine for large datasets
Date: 2026-05-25
"""

from collections import defaultdict
from typing import Callable, List, Tuple

class MapReduceEngine:
    def execute(self, data: List, mapper: Callable, reducer: Callable) -> List[Tuple]:
        intermediate = defaultdict(list)
        for item in data:
            for k, v in mapper(item):
                intermediate[k].append(v)
        output = []
        for k, values in intermediate.items():
            output.append((k, reducer(k, values)))
        return output

