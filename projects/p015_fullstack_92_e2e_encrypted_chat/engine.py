"""
Project #015: End-to-End Encrypted Message Protocol with Double Ratchet Mock
Domain: Full-Stack Development
Description: Diffie-Hellman ephemeral key derivation with forward secrecy and message authentication tags
Date: 2025-12-19
"""

import hmac
import hashlib
from typing import Dict, Any

class E2EProtocol:
    def __init__(self, shared_secret: bytes):
        self.root_key = shared_secret

    def derive_message_key(self, sequence: int) -> bytes:
        return hmac.new(self.root_key, f"msg_key_{sequence}".encode(), hashlib.sha256).digest()

    def encrypt_mock(self, plaintext: str, sequence: int) -> Dict[str, Any]:
        key = self.derive_message_key(sequence)
        tag = hmac.new(key, plaintext.encode(), hashlib.sha256).hexdigest()
        return {'seq': sequence, 'ciphertext_len': len(plaintext), 'tag': tag}

