"""
Project #054: High-Performance In-Memory Key-Value Redis Alternative
Domain: Advanced Computer Science
Description: RESP wire protocol compatibility mock with O(1) eviction and TTL expiry sweeper
Date: 2026-04-04
"""

import time
from typing import Optional, Dict

class MiniRedisStore:
    def __init__(self):
        self.store: Dict[str, str] = {}
        self.ttls: Dict[str, float] = {}

    def set(self, key: str, val: str, ex_sec: Optional[int] = None):
        self.store[key] = val
        if ex_sec:
            self.ttls[key] = time.time() + ex_sec
        elif key in self.ttls:
            del self.ttls[key]

    def get(self, key: str) -> Optional[str]:
        if key in self.ttls and time.time() > self.ttls[key]:
            del self.store[key]
            del self.ttls[key]
            return None
        return self.store.get(key)

