"""
Project #048: Infrastructure-as-Code Configuration Drift Detection Engine
Domain: Cloud & DevOps
Description: Compares live cloud state against declarative Terraform/OpenTofu AST specs to detect deviations
Date: 2026-03-21
"""

from typing import Dict, List, Any

class DriftDetector:
    def compare(self, state_expected: Dict[str, Any], state_actual: Dict[str, Any]) -> List[Dict]:
        drifts = []
        for res_id, expected_props in state_expected.items():
            if res_id not in state_actual:
                drifts.append({'resource': res_id, 'type': 'MISSING_IN_CLOUD'})
                continue
            actual = state_actual[res_id]
            for key, val in expected_props.items():
                if actual.get(key) != val:
                    drifts.append({'resource': res_id, 'key': key, 'expected': val, 'actual': actual.get(key)})
        return drifts

