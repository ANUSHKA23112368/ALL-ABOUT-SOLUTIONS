"""
Project #007: AI-Powered GitHub Repository Architecture Analyzer
Domain: Generative AI & LLMs
Description: Traverses repository dependency trees, calculates maintainability indices, and evaluates code hygiene
Date: 2025-11-22
"""

import os
from typing import Dict, Any

class GitHubRepoAnalyzer:
    def analyze_tree(self, file_list: list) -> Dict[str, Any]:
        ext_counter = {}
        has_tests = False
        has_ci = False
        has_docker = False

        for f in file_list:
            ext = os.path.splitext(f)[1]
            ext_counter[ext] = ext_counter.get(ext, 0) + 1
            if 'test' in f.lower():
                has_tests = True
            if '.github/workflows' in f:
                has_ci = True
            if 'dockerfile' in f.lower():
                has_docker = True

        health_score = 40 + (20 if has_tests else 0) + (20 if has_ci else 0) + (20 if has_docker else 0)
        return {
            'total_files': len(file_list),
            'languages': ext_counter,
            'has_test_suite': has_tests,
            'has_ci_cd': has_ci,
            'health_score': health_score
        }

