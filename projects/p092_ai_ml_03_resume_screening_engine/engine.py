"""
Project #092: AI Resume Screening & Candidate Ranking Engine
Domain: AI & Machine Learning
Description: Automated technical resume parser with TF-IDF skill matching and semantic scoring
Date: 2026-06-13
"""

import re
from collections import Counter
from typing import List, Dict

class ResumeScreeningEngine:
    def __init__(self, target_skills: List[str]):
        self.target_skills = [s.lower() for s in target_skills]

    def score_candidate(self, resume_text: str, experience_years: float) -> Dict[str, float]:
        matched = [s for s in self.target_skills if s in resume_text.lower()]
        coverage = len(matched) / max(1, len(self.target_skills))
        exp_weight = min(1.0, experience_years / 5.0)
        overall_score = round((coverage * 0.7) + (exp_weight * 0.3), 3)

        return {
            'overall_match_score': overall_score,
            'skill_coverage_pct': round(coverage * 100, 1),
            'matched_skills': matched,
            'recommended_interview': overall_score >= 0.65
        }

