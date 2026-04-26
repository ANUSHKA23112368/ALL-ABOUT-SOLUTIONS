"""
Project #063: Automated Bug & Vulnerability Detection in Source Code
Domain: AI & Machine Learning
Description: Abstract syntax tree static analyzer identifying anti-patterns and memory safety risks
Date: 2026-04-26
"""

import ast
from typing import List, Dict

class ASTBugDetector(ast.NodeVisitor):
    def __init__(self):
        self.issues: List[Dict[str, str]] = []

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.issues.append({'line': node.lineno, 'type': 'BareExcept', 'severity': 'HIGH', 'message': 'Bare except catches SystemExit and KeyboardInterrupt'})
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'eval':
            self.issues.append({'line': node.lineno, 'type': 'DangerousEval', 'severity': 'CRITICAL', 'message': 'Use of eval introduces remote code execution vulnerability'})
        self.generic_visit(node)

    def scan(self, code: str) -> List[Dict[str, str]]:
        self.issues.clear()
        tree = ast.parse(code)
        self.visit(tree)
        return list(self.issues)

