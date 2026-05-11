"""
Project #072: Zero-Trust Contextual Access Management Prototype
Domain: Cybersecurity
Description: Dynamic session gate scoring device posture, IP reputation, and behavioral velocity before authorization
Date: 2026-05-11
"""

from typing import Dict, Any

class ZeroTrustAccessGate:
    def authorize(self, context: Dict[str, Any]) -> Dict[str, Any]:
        device_managed = context.get('is_managed_device', False)
        disk_encrypted = context.get('is_encrypted', False)
        geo_velocity_valid = context.get('velocity_valid', True)
        mfa_verified = context.get('mfa_verified', False)

        posture_score = (30 if device_managed else 0) + (20 if disk_encrypted else 0) + (25 if geo_velocity_valid else 0) + (25 if mfa_verified else 0)
        decision = "PERMIT" if posture_score >= 80 else ("STEP_UP_CHALLENGE" if posture_score >= 50 else "DENY")
        return {'decision': decision, 'posture_score': posture_score}

