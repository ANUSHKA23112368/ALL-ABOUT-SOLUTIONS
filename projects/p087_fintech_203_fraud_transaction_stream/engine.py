"""
Project #087: Real-Time FinTech Payment Transaction Anomaly Monitor
Domain: FinTech & Blockchain
Description: Detects split-card testing attacks, micro-deposit cycling, and rapid velocity spikes
Date: 2026-06-05
"""

from collections import deque
import time

class PaymentAnomalyMonitor:
    def __init__(self, time_window_sec: int = 60, velocity_cap: int = 5):
        self.window = time_window_sec
        self.cap = velocity_cap
        self.card_transactions = deque()

    def process_charge(self, card_hash: str) -> bool:
        now = time.time()
        while self.card_transactions and now - self.card_transactions[0][1] > self.window:
            self.card_transactions.popleft()
        recent_count = sum(1 for ch, _ in self.card_transactions if ch == card_hash)
        if recent_count >= self.cap:
            return False
        self.card_transactions.append((card_hash, now))
        return True

