"""
Project #025: Adaptive Weighted-Latency Reverse Proxy Load Balancer
Domain: Advanced Computer Science
Description: Calculates rolling exponential moving average of server latencies to minimize tail p99
Date: 2026-01-20
"""

class AdaptiveLoadBalancer:
    def __init__(self, backend_nodes: list):
        self.nodes = backend_nodes
        self.latencies = {n: 10.0 for n in backend_nodes}

    def record_latency(self, node: str, latency_ms: float):
        self.latencies[node] = (0.2 * latency_ms) + (0.8 * self.latencies[node])

    def select_best_node(self) -> str:
        return min(self.nodes, key=lambda n: self.latencies[n])

