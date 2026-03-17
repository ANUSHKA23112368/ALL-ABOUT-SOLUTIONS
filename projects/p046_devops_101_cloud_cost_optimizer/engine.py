"""
Project #046: Automated Cloud Resource & Cost Optimization Platform
Domain: Cloud & DevOps
Description: Analyzes AWS/GCP utilization metrics, discovers orphaned volumes, and recommends rightsizing
Date: 2026-03-17
"""

from typing import List, Dict, Any

class CloudCostOptimizer:
    def analyze_instances(self, instances: List[Dict]) -> Dict[str, Any]:
        idle_instances = []
        potential_savings = 0.0

        for inst in instances:
            avg_cpu = inst.get('avg_cpu_pct', 0.0)
            hourly_cost = inst.get('cost_hourly', 0.0)
            if avg_cpu < 5.0:
                idle_instances.append(inst['id'])
                potential_savings += (hourly_cost * 24 * 30)

        return {
            'idle_count': len(idle_instances),
            'orphaned_candidates': idle_instances,
            'monthly_savings_usd': round(potential_savings, 2)
        }

