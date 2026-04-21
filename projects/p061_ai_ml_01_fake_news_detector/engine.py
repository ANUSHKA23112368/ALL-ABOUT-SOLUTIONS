"""
Project #061: AI-Powered Fake News Detection System
Domain: AI & Machine Learning
Description: Linguistic feature extractor and ensemble classifier for misinformation detection
Date: 2026-04-21
"""

import re
from typing import Dict

class FakeNewsDetector:
    def __init__(self):
        self.sensationalist_terms = {
            'shocking', 'unbelievable', 'you won\'t believe', 'miracle cure', 'secret exposed',
            'conspiracy', 'hidden truth', 'explosive', 'urgent alert', 'total blackout'
        }
        self.credibility_boosters = {'source:', 'reuters', 'peer-reviewed', 'associated press', 'official report'}

    def evaluate(self, headline: str, body: str) -> Dict[str, float]:
        text = (headline + ' ' + body).lower()
        sensational_hits = sum(1 for term in self.sensationalist_terms if term in text)
        credibility_hits = sum(1 for term in self.credibility_boosters if term in text)
        exclamation_ratio = headline.count('!') / max(1, len(headline.split()))
        caps_ratio = sum(1 for c in headline if c.isupper()) / max(1, len(headline))

        risk_score = min(1.0, (sensational_hits * 0.25) + (exclamation_ratio * 0.3) + (caps_ratio * 0.4) - (credibility_hits * 0.2))
        risk_score = max(0.0, risk_score)

        return {
            'credibility_score': round(1.0 - risk_score, 3),
            'sensationalism_index': round(risk_score, 3),
            'flagged_markers': sensational_hits,
            'is_high_risk': risk_score > 0.55
        }

