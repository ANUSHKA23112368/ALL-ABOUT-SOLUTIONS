"""
Project #090: AI Model Demographic Parity & Fairness Auditor
Domain: Emerging Technologies
Description: Audits predictions across protected attributes, calculating equalized odds and disparate impact
Date: 2026-06-10
"""

from typing import List, Dict

class FairnessAuditor:
    def calculate_disparate_impact(self, group_a_preds: List[int], group_b_preds: List[int]) -> Dict[str, float]:
        rate_a = sum(group_a_preds) / max(1, len(group_a_preds))
        rate_b = sum(group_b_preds) / max(1, len(group_b_preds))
        ratio = rate_a / rate_b if rate_b > 0 else 1.0

        return {
            'group_a_acceptance': round(rate_a, 3),
            'group_b_acceptance': round(rate_b, 3),
            'disparate_impact_ratio': round(ratio, 3),
            'meets_four_fifths_rule': 0.8 <= ratio <= 1.25
        }

