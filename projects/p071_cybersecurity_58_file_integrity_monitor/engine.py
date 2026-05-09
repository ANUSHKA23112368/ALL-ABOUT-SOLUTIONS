"""
Project #071: Real-Time Cryptographic File Integrity Monitor (FIM)
Domain: Cybersecurity
Description: SHA-256 tree hashing watcher detecting unauthorized modifications, additions, and file tampering
Date: 2026-05-09
"""

import hashlib
from typing import Dict

class FileIntegrityMonitor:
    def __init__(self):
        self.baseline = {}

    def compute_hash(self, content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()

    def record_baseline(self, filepath: str, content: bytes):
        self.baseline[filepath] = self.compute_hash(content)

    def verify(self, filepath: str, current_content: bytes) -> Dict[str, str]:
        if filepath not in self.baseline:
            return {'status': 'UNTRACKED_NEW_FILE'}
        current_hash = self.compute_hash(current_content)
        if current_hash != self.baseline[filepath]:
            return {'status': 'TAMPERED_ALERT', 'expected': self.baseline[filepath], 'actual': current_hash}
        return {'status': 'VERIFIED_CLEAN'}

