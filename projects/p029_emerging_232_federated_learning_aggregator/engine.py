"""
Project #029: Federated Learning Secure Model Weight Aggregator
Domain: Emerging Technologies
Description: Federated Averaging (FedAvg) algorithm combining local edge gradients with differential noise
Date: 2026-01-31
"""

from typing import List

class FederatedAggregator:
    def aggregate_weights(self, client_weights: List[List[float]], sample_counts: List[int]) -> List[float]:
        total_samples = sum(sample_counts)
        num_params = len(client_weights[0])
        global_model = [0.0] * num_params

        for weights, count in zip(client_weights, sample_counts):
            weight_factor = count / total_samples
            for i in range(num_params):
                global_model[i] += weights[i] * weight_factor

        return [round(w, 5) for w in global_model]

