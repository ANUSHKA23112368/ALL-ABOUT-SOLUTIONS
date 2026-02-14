"""
Project #034: Real-Time Fraudulent Transaction Detection Engine
Domain: AI & Machine Learning
Description: Streaming outlier scoring engine utilizing rolling z-scores and geolocation anomaly checks
Date: 2026-02-14
"""

import math
from collections import deque
from typing import Dict, Any

class FraudTransactionDetector:
    def __init__(self, history_window: int = 50):
        self.amounts = deque(maxlen=history_window)
        self.known_locations = {}

    def ingest_and_score(self, user_id: str, amount: float, location: str) -> Dict[str, Any]:
        flags = []
        if self.amounts:
            mean = sum(self.amounts) / len(self.amounts)
            variance = sum((x - mean) ** 2 for x in self.amounts) / len(self.amounts)
            std_dev = math.sqrt(variance) if variance > 0 else 1.0
            z_score = (amount - mean) / std_dev
            if z_score > 3.0:
                flags.append('STATISTICAL_AMOUNT_OUTLIER')
        self.amounts.append(amount)

        if user_id in self.known_locations and self.known_locations[user_id] != location:
            flags.append('IMPOSSIBLE_TRAVEL_SPEED')
        self.known_locations[user_id] = location

        fraud_prob = min(1.0, len(flags) * 0.45)
        return {'is_fraud': fraud_prob > 0.4, 'risk_score': round(fraud_prob, 2), 'reasons': flags}

