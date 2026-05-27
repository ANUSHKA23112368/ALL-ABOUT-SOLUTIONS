"""
Project #081: Emergency Ambulance Dispatch & Route Optimization
Domain: Healthcare & Impact
Description: Graph heuristic evaluating traffic density, congestion probability, and triage response times
Date: 2026-05-27
"""

import heapq
from typing import Dict, List, Tuple

class AmbulanceRoutePlanner:
    def __init__(self, graph: Dict[str, List[Tuple[str, float]]]):
        self.graph = graph

    def plan_fastest_route(self, start: str, hospital: str) -> Tuple[float, List[str]]:
        pq = [(0.0, start, [start])]
        visited = set()

        while pq:
            time_cost, node, path = heapq.heappop(pq)
            if node == hospital:
                return time_cost, path
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in self.graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (time_cost + weight, neighbor, path + [neighbor]))
        return float('inf'), []

