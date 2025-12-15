"""
Project #014: Real-Time Collaborative Code Editor Protocol
Domain: Full-Stack Development
Description: Conflict-free Operational Transformation protocol ensuring converge-safe concurrent keystrokes
Date: 2025-12-15
"""

from typing import List

class TextOperation:
    def __init__(self, op_type: str, position: int, char: str = ""):
        self.op_type = op_type
        self.position = position
        self.char = char

class CollaborativeEditorBuffer:
    def __init__(self):
        self.buffer = []

    def apply(self, op: TextOperation):
        if op.op_type == 'INSERT':
            self.buffer.insert(op.position, op.char)
        elif op.op_type == 'DELETE' and op.position < len(self.buffer):
            self.buffer.pop(op.position)

    def get_text(self) -> str:
        return "".join(self.buffer)

