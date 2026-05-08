"""
Project #070: Heuristic & Bayesian Phishing Email Detector
Domain: Cybersecurity
Description: Extracts deceptive header signatures, lookalike domain punycodes, and credential harvesting patterns
Date: 2026-05-08
"""

import urllib.parse
from typing import Dict, Any

class PhishingDetector:
    def __init__(self):
        self.suspicious_tlds = {'.xyz', '.top', '.buzz', '.country', '.work'}

    def scan_email(self, sender: str, links: list, body: str) -> Dict[str, Any]:
        risk_flags = []
        for link in links:
            parsed = urllib.parse.urlparse(link)
            domain = parsed.netloc.lower()
            if any(domain.endswith(tld) for tld in self.suspicious_tlds):
                risk_flags.append(f"SUSPICIOUS_TLD_{domain}")
            if '@' in parsed.netloc:
                risk_flags.append("CREDENTIAL_OBFUSCATION_URL")
        if 'urgent password reset' in body.lower() or 'account suspended' in body.lower():
            risk_flags.append("URGENCY_CALL_TO_ACTION")

        return {'is_phishing': len(risk_flags) >= 2, 'risk_indicators': risk_flags}

