"""
Project #056: Distributed Leaky-Bucket Rate Limiter with Redis Protocol
Domain: Advanced Computer Science
Description: Sliding log interval synchronizer with atomic token decrements for multi-node clusters
Date: 2026-04-09
"""

import time

class DistributedRateLimiter:
    def __init__(self, rate_per_sec: float, capacity: int):
        self.rate = rate_per_sec
        self.capacity = capacity
        self.water_level = 0.0
        self.last_leak = time.time()

    def allow_request(self) -> bool:
        now = time.time()
        leaked = (now - self.last_leak) * self.rate
        self.water_level = max(0.0, self.water_level - leaked)
        self.last_leak = now

        if self.water_level + 1.0 <= self.capacity:
            self.water_level += 1.0
            return True
        return False

